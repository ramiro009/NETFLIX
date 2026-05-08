// Datos mock que simulan respuestas del backend FastAPI + PostgreSQL.
// Reemplazá estos valores por llamadas reales a tus endpoints.

export type Genero = { id: number; nombre: string };

export type Contenido = {
  id: number;
  titulo: string;
  tipo: "pelicula" | "serie";
  anio: number;
  descripcion: string;
  duracion_min: number;
  clasificacion_edad: string;
  poster: string;
  backdrop: string;
  generos: Genero[];
  rating_promedio?: number;
};

export type Temporada = {
  id: number;
  contenido_id: number;
  numero: number;
  anio: number;
  episodios: Episodio[];
};

export type Episodio = {
  id: number;
  temporada_id: number;
  numero: number;
  titulo: string;
  duracion_min: number;
  descripcion?: string;
};

export type Perfil = {
  id: number;
  cuenta_id: number;
  nombre: string;
  es_infantil: boolean;
  avatar: string;
};

export const generos: Genero[] = [
  { id: 1, nombre: "Acción" },
  { id: 2, nombre: "Drama" },
  { id: 3, nombre: "Ciencia Ficción" },
  { id: 4, nombre: "Comedia" },
  { id: 5, nombre: "Suspenso" },
  { id: 6, nombre: "Animación" },
];

export const perfiles: Perfil[] = [
  { id: 1, cuenta_id: 1, nombre: "Martín", es_infantil: false, avatar: "🦊" },
  { id: 2, cuenta_id: 1, nombre: "Lucía", es_infantil: false, avatar: "🐼" },
  { id: 3, cuenta_id: 1, nombre: "Mateo", es_infantil: true, avatar: "🦁" },
  { id: 4, cuenta_id: 1, nombre: "Invitado", es_infantil: false, avatar: "👤" },
];

const img = (seed: string, w = 600, h = 900) =>
  `https://picsum.photos/seed/${seed}/${w}/${h}`;

export const contenidos: Contenido[] = [
  {
    id: 1, titulo: "Horizonte Cero", tipo: "serie", anio: 2024,
    descripcion: "En un futuro donde la inteligencia artificial gobierna las ciudades, un grupo de hackers lucha por recuperar la humanidad perdida.",
    duracion_min: 52, clasificacion_edad: "16+",
    poster: img("horizonte", 600, 900), backdrop: img("horizonte-bg", 1600, 900),
    generos: [generos[2], generos[4]], rating_promedio: 4.7,
  },
  {
    id: 2, titulo: "La Última Tormenta", tipo: "pelicula", anio: 2023,
    descripcion: "Una piloto retirada debe enfrentar el huracán más grande de la historia para salvar a su familia.",
    duracion_min: 128, clasificacion_edad: "13+",
    poster: img("tormenta", 600, 900), backdrop: img("tormenta-bg", 1600, 900),
    generos: [generos[0], generos[1]], rating_promedio: 4.3,
  },
  {
    id: 3, titulo: "Brigada Nocturna", tipo: "serie", anio: 2025,
    descripcion: "Detectives en una ciudad sin sol resuelven crímenes imposibles bajo luces de neón.",
    duracion_min: 45, clasificacion_edad: "16+",
    poster: img("brigada", 600, 900), backdrop: img("brigada-bg", 1600, 900),
    generos: [generos[4], generos[1]], rating_promedio: 4.5,
  },
  {
    id: 4, titulo: "Reír es Vivir", tipo: "pelicula", anio: 2024,
    descripcion: "Una comedia luminosa sobre tres hermanos que heredan un viejo teatro.",
    duracion_min: 102, clasificacion_edad: "ATP",
    poster: img("reir", 600, 900), backdrop: img("reir-bg", 1600, 900),
    generos: [generos[3]], rating_promedio: 4.1,
  },
  {
    id: 5, titulo: "Reino de Estrellas", tipo: "serie", anio: 2024,
    descripcion: "Una odisea espacial sobre el descubrimiento de un planeta gemelo.",
    duracion_min: 58, clasificacion_edad: "13+",
    poster: img("reino", 600, 900), backdrop: img("reino-bg", 1600, 900),
    generos: [generos[2]], rating_promedio: 4.8,
  },
  {
    id: 6, titulo: "El Bosque Azul", tipo: "pelicula", anio: 2022,
    descripcion: "Una aventura animada para toda la familia sobre amistad y coraje.",
    duracion_min: 95, clasificacion_edad: "ATP",
    poster: img("bosque", 600, 900), backdrop: img("bosque-bg", 1600, 900),
    generos: [generos[5], generos[3]], rating_promedio: 4.6,
  },
  {
    id: 7, titulo: "Sombras del Pasado", tipo: "serie", anio: 2023,
    descripcion: "Un thriller psicológico sobre memorias que regresan tras 20 años.",
    duracion_min: 50, clasificacion_edad: "16+",
    poster: img("sombras", 600, 900), backdrop: img("sombras-bg", 1600, 900),
    generos: [generos[4], generos[1]], rating_promedio: 4.4,
  },
  {
    id: 8, titulo: "Velocidad Máxima", tipo: "pelicula", anio: 2025,
    descripcion: "El mejor piloto del mundo enfrenta a su rival más feroz en una carrera mortal.",
    duracion_min: 115, clasificacion_edad: "13+",
    poster: img("velocidad", 600, 900), backdrop: img("velocidad-bg", 1600, 900),
    generos: [generos[0]], rating_promedio: 4.0,
  },
  {
    id: 9, titulo: "Pequeños Héroes", tipo: "serie", anio: 2024,
    descripcion: "Animación infantil sobre amigos que descubren superpoderes en su barrio.",
    duracion_min: 22, clasificacion_edad: "ATP",
    poster: img("heroes", 600, 900), backdrop: img("heroes-bg", 1600, 900),
    generos: [generos[5]], rating_promedio: 4.5,
  },
  {
    id: 10, titulo: "Ciudad Eterna", tipo: "pelicula", anio: 2023,
    descripcion: "Drama romántico ambientado en una Roma soñada y nostálgica.",
    duracion_min: 134, clasificacion_edad: "13+",
    poster: img("ciudad", 600, 900), backdrop: img("ciudad-bg", 1600, 900),
    generos: [generos[1]], rating_promedio: 4.2,
  },
];

export const temporadas: Temporada[] = [
  {
    id: 1, contenido_id: 1, numero: 1, anio: 2024,
    episodios: [
      { id: 1, temporada_id: 1, numero: 1, titulo: "Despertar", duracion_min: 54, descripcion: "Todo comienza en una madrugada cualquiera." },
      { id: 2, temporada_id: 1, numero: 2, titulo: "El Código", duracion_min: 51, descripcion: "Una pista oculta cambia las reglas del juego." },
      { id: 3, temporada_id: 1, numero: 3, titulo: "Resistencia", duracion_min: 49, descripcion: "El grupo enfrenta su primera gran prueba." },
    ],
  },
  {
    id: 2, contenido_id: 1, numero: 2, anio: 2025,
    episodios: [
      { id: 4, temporada_id: 2, numero: 1, titulo: "Nuevo Mundo", duracion_min: 55 },
      { id: 5, temporada_id: 2, numero: 2, titulo: "Aliados", duracion_min: 52 },
    ],
  },
];

// Estado local para "Mi Lista", calificaciones y vistas (mock).
// En tu backend esto vendría de las tablas mi_lista, calificaciones y vistas.
export const miLista = new Set<number>([2, 5]);
export const calificaciones = new Map<number, number>([[1, 5], [3, 4]]);
export const episodiosTerminados = new Set<number>([1]);

export const getContenido = (id: number) => contenidos.find((c) => c.id === id);
export const getTemporadasDe = (contenidoId: number) =>
  temporadas.filter((t) => t.contenido_id === contenidoId);
