-- ==========================================================
-- 1. LIMPIEZA, EXTENSIONES Y TIPOS
-- ==========================================================
DROP VIEW IF EXISTS reporte_visualizacion;
DROP TABLE IF EXISTS descargas, contenido_idiomas, idiomas, calificaciones, mi_lista, vistas, episodios, temporadas, contenido_generos, contenidos, generos, perfiles, cuentas CASCADE;
DROP TYPE IF EXISTS tipo_plan, tipo_contenido, tipo_clasificacion, tipo_audio_sub CASCADE;

CREATE EXTENSION IF NOT EXISTS citext;

CREATE TYPE tipo_plan AS ENUM ('basico', 'estandar', 'premium');
CREATE TYPE tipo_contenido AS ENUM ('pelicula', 'serie');
CREATE TYPE tipo_clasificacion AS ENUM ('ATP', '+13', '+16', '+18');
CREATE TYPE tipo_audio_sub AS ENUM ('audio', 'subtitulo');

-- ==========================================================
-- 2. TABLAS DE ESTRUCTURA (CUENTAS Y PERFILES)
-- ==========================================================

CREATE TABLE cuentas (
    id SERIAL PRIMARY KEY,
    email CITEXT UNIQUE NOT NULL,
    plan tipo_plan NOT NULL,
    pin CHAR(4) CHECK (pin ~ '^[0-9]{4}$'),
    fecha_alta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE perfiles (
    id SERIAL PRIMARY KEY,
    cuenta_id INTEGER REFERENCES cuentas(id) ON DELETE CASCADE,
    nombre VARCHAR(50) NOT NULL,
    es_infantil BOOLEAN DEFAULT FALSE,
    avatar VARCHAR(255),
    bloqueado_hasta TIMESTAMP DEFAULT NULL,
    intentos_fallidos_pin INTEGER DEFAULT 0,
    UNIQUE(cuenta_id, nombre)
);

-- ==========================================================
-- 3. TABLAS DE CONTENIDO (CATÁLOGO)
-- ==========================================================

CREATE TABLE generos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE contenidos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    tipo tipo_contenido NOT NULL,
    anio INTEGER,
    descripcion TEXT,
    duracion_min INTEGER, 
    clasificacion_edad tipo_clasificacion NOT NULL,
    CONSTRAINT check_duracion_por_tipo CHECK (
        (tipo = 'pelicula' AND duracion_min IS NOT NULL) OR 
        (tipo = 'serie' AND duracion_min IS NULL)
    )
);

CREATE TABLE contenido_generos (
    contenido_id INTEGER REFERENCES contenidos(id) ON DELETE CASCADE,
    genero_id INTEGER REFERENCES generos(id) ON DELETE CASCADE,
    PRIMARY KEY (contenido_id, genero_id)
);

CREATE TABLE temporadas (
    id SERIAL PRIMARY KEY,
    contenido_id INTEGER REFERENCES contenidos(id) ON DELETE CASCADE,
    numero INTEGER NOT NULL,
    anio INTEGER,
    UNIQUE(contenido_id, numero)
);

CREATE TABLE episodios (
    id SERIAL PRIMARY KEY,
    temporada_id INTEGER REFERENCES temporadas(id) ON DELETE CASCADE,
    numero INTEGER NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    duracion_min INTEGER NOT NULL,
    UNIQUE(temporada_id, numero)
);

-- ==========================================================
-- 4. INTERACCIONES Y ACTIVIDAD
-- ==========================================================

CREATE TABLE vistas (
    id SERIAL PRIMARY KEY,
    perfil_id INTEGER REFERENCES perfiles(id) ON DELETE CASCADE,
    contenido_id INTEGER REFERENCES contenidos(id) ON DELETE CASCADE, -- Referencia al contenido padre
    episodio_id INTEGER REFERENCES episodios(id) ON DELETE CASCADE,    -- NULL si es película
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    segundos_vistos INTEGER DEFAULT 0,
    terminado BOOLEAN DEFAULT FALSE,
    UNIQUE(perfil_id, contenido_id, episodio_id)
);

CREATE TABLE mi_lista (
    perfil_id INTEGER REFERENCES perfiles(id) ON DELETE CASCADE,
    contenido_id INTEGER REFERENCES contenidos(id) ON DELETE CASCADE,
    fecha_agregada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (perfil_id, contenido_id)
);

CREATE TABLE calificaciones (
    id SERIAL PRIMARY KEY,
    perfil_id INTEGER REFERENCES perfiles(id) ON DELETE CASCADE,
    contenido_id INTEGER REFERENCES contenidos(id) ON DELETE CASCADE,
    puntaje INTEGER CHECK (puntaje BETWEEN 1 AND 5),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(perfil_id, contenido_id)
);

CREATE TABLE idiomas (
    id SERIAL PRIMARY KEY,
    codigo CHAR(2) UNIQUE NOT NULL,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE contenido_idiomas (
    contenido_id INTEGER REFERENCES contenidos(id) ON DELETE CASCADE,
    idioma_id INTEGER REFERENCES idiomas(id) ON DELETE CASCADE,
    tipo tipo_audio_sub NOT NULL,
    PRIMARY KEY (contenido_id, idioma_id, tipo)
);

CREATE TABLE descargas (
    id SERIAL PRIMARY KEY,
    perfil_id INTEGER REFERENCES perfiles(id) ON DELETE CASCADE,
    contenido_id INTEGER REFERENCES contenidos(id) ON DELETE CASCADE,
    episodio_id INTEGER REFERENCES episodios(id) ON DELETE CASCADE,
    fecha_descarga TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    vencimiento TIMESTAMP DEFAULT (CURRENT_TIMESTAMP + INTERVAL '30 days'),
    activa BOOLEAN DEFAULT TRUE
);

-- ==========================================================
-- 5. LÓGICA DE NEGOCIO (TRIGGERS)
-- ==========================================================

-- Trigger: Límite de perfiles
CREATE OR REPLACE FUNCTION fn_validar_limite_perfiles() RETURNS TRIGGER AS $$
DECLARE
    v_plan tipo_plan; v_actual INTEGER; v_max INTEGER;
BEGIN
    SELECT plan INTO v_plan FROM cuentas WHERE id = NEW.cuenta_id;
    SELECT COUNT(*) INTO v_actual FROM perfiles WHERE cuenta_id = NEW.cuenta_id;
    v_max := CASE WHEN v_plan = 'basico' THEN 1 WHEN v_plan = 'estandar' THEN 2 ELSE 5 END;
    IF v_actual >= v_max THEN RAISE EXCEPTION 'Límite de perfiles excedido'; END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_limite_perfiles BEFORE INSERT ON perfiles FOR EACH ROW EXECUTE FUNCTION fn_validar_limite_perfiles();

-- Trigger: Progreso de vista
CREATE OR REPLACE FUNCTION fn_check_progreso() RETURNS TRIGGER AS $$
DECLARE
    v_duracion_seg INTEGER;
BEGIN
    IF NEW.episodio_id IS NOT NULL THEN
        SELECT duracion_min * 60 INTO v_duracion_seg FROM episodios WHERE id = NEW.episodio_id;
    ELSE
        SELECT duracion_min * 60 INTO v_duracion_seg FROM contenidos WHERE id = NEW.contenido_id;
    END IF;
    IF NEW.segundos_vistos >= (v_duracion_seg * 0.9) THEN NEW.terminado := TRUE; END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_actualizar_vista BEFORE INSERT OR UPDATE ON vistas FOR EACH ROW EXECUTE FUNCTION fn_check_progreso();

-- ==========================================================
-- 6. VISTA DE REPORTES (CORREGIDA)
-- ==========================================================

CREATE OR REPLACE VIEW reporte_visualizacion AS
SELECT 
    c.id AS contenido_id,
    c.titulo,
    EXTRACT(YEAR FROM v.fecha) AS anio,
    EXTRACT(MONTH FROM v.fecha) AS mes,
    SUM(v.segundos_vistos) / 60 AS minutos_totales,
    g.nombre AS genero
FROM vistas v
JOIN contenidos c ON v.contenido_id = c.id
JOIN contenido_generos cg ON c.id = cg.contenido_id
JOIN generos g ON cg.genero_id = g.id
WHERE v.terminado = TRUE 
GROUP BY 
    c.id, 
    c.titulo, 
    EXTRACT(YEAR FROM v.fecha), 
    EXTRACT(MONTH FROM v.fecha), 
    g.nombre;