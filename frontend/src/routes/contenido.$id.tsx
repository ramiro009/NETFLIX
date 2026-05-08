import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import { Navbar } from "@/components/navbar";
import {
  getContenido,
  getTemporadasDe,
  miLista,
  calificaciones,
  episodiosTerminados,
  contenidos,
  type Contenido,
} from "@/lib/mock-data";
import { Play, Plus, Check, Star, ArrowLeft } from "lucide-react";
import { useState } from "react";
import { ContentRow } from "@/components/content-row";

export const Route = createFileRoute("/contenido/$id")({
  loader: ({ params }) => {
    const c = getContenido(Number(params.id));
    if (!c) throw notFound();
    return c;
  },
  head: ({ loaderData }) => ({
    meta: [
      { title: `${loaderData?.titulo ?? "Contenido"} — Streamio` },
      { name: "description", content: loaderData?.descripcion ?? "" },
      { property: "og:image", content: loaderData?.backdrop ?? "" },
    ],
  }),
  notFoundComponent: () => (
    <div className="min-h-screen flex items-center justify-center">
      <p className="text-muted-foreground">Contenido no encontrado.</p>
    </div>
  ),
  errorComponent: ({ error }) => <div className="p-12">{error.message}</div>,
  component: ContenidoDetalle,
});

function ContenidoDetalle() {
  const c = Route.useLoaderData() as Contenido;
  const [enMiLista, setEnMiLista] = useState(miLista.has(c.id));
  const [puntaje, setPuntaje] = useState<number>(calificaciones.get(c.id) ?? 0);
  const temporadas = getTemporadasDe(c.id);
  const [tempActiva, setTempActiva] = useState(temporadas[0]?.id);

  // ============================================================
  // ENDPOINTS FastAPI sugeridos para esta pantalla:
  //
  // GET /api/contenidos/{id}
  //   -> Contenido + generos (JOIN contenido_generos) + rating promedio
  //
  // GET /api/contenidos/{id}/temporadas
  //   -> Temporada[] con sus Episodio[] anidados
  //   SQL: SELECT t.*, e.* FROM temporadas t
  //        LEFT JOIN episodios e ON e.temporada_id = t.id
  //        WHERE t.contenido_id = $1
  //        ORDER BY t.numero, e.numero;
  //
  // GET /api/perfiles/{perfil_id}/vistas?contenido_id={id}
  //   -> Vista[] para marcar episodios ya vistos
  //
  // POST /api/perfiles/{perfil_id}/mi-lista     body: { contenido_id }
  // DELETE /api/perfiles/{perfil_id}/mi-lista/{contenido_id}
  //
  // POST /api/perfiles/{perfil_id}/calificaciones
  //   body: { contenido_id, puntaje }
  //   -> upsert sobre tabla calificaciones
  //
  // POST /api/perfiles/{perfil_id}/vistas
  //   body: { episodio_id, segundos_vistos, terminado }
  // ============================================================

  const toggleMiLista = () => {
    setEnMiLista((v) => !v);
    // fetch(`${API}/perfiles/${perfilId}/mi-lista`, {
    //   method: enMiLista ? 'DELETE' : 'POST',
    //   body: JSON.stringify({ contenido_id: c.id })
    // });
  };

  const calificar = (n: number) => {
    setPuntaje(n);
    // fetch(`${API}/perfiles/${perfilId}/calificaciones`, {
    //   method: 'POST',
    //   body: JSON.stringify({ contenido_id: c.id, puntaje: n })
    // });
  };

  const similares = contenidos.filter(
    (x) => x.id !== c.id && x.generos.some((g) => c.generos.some((cg) => cg.id === g.id))
  );

  return (
    <div className="min-h-screen pb-20">
      <Navbar />

      <section className="relative min-h-[70vh]">
        <img src={c.backdrop} alt={c.titulo} className="absolute inset-0 h-full w-full object-cover" />
        <div className="absolute inset-0 bg-gradient-to-t from-background via-background/70 to-background/30" />
        <Link
          to="/browse"
          className="absolute top-20 left-4 md:left-12 z-10 flex items-center gap-2 px-3 py-2 bg-surface/80 rounded hover:bg-surface transition-colors backdrop-blur"
        >
          <ArrowLeft className="size-4" /> Volver
        </Link>
        <div className="relative pt-32 md:pt-40 px-4 md:px-12 grid md:grid-cols-[260px_1fr] gap-8 max-w-6xl">
          <img
            src={c.poster}
            alt={c.titulo}
            className="w-44 md:w-full rounded-lg shadow-2xl"
            style={{ boxShadow: "var(--shadow-card)" }}
          />
          <div>
            <h1 className="text-3xl md:text-5xl font-bold mb-3">{c.titulo}</h1>
            <div className="flex flex-wrap items-center gap-3 text-sm text-muted-foreground mb-4">
              <span className="text-foreground font-semibold">{c.anio}</span>
              <span className="px-2 py-0.5 border border-border rounded">{c.clasificacion_edad}</span>
              <span>{c.duracion_min} min</span>
              <span className="uppercase">{c.tipo}</span>
              {c.rating_promedio && (
                <span className="flex items-center gap-1 text-gold">
                  <Star className="size-4 fill-current" /> {c.rating_promedio}
                </span>
              )}
            </div>
            <p className="text-foreground/90 mb-6 max-w-2xl">{c.descripcion}</p>

            <div className="flex flex-wrap gap-2 mb-6">
              {c.generos.map((g) => (
                <span key={g.id} className="px-3 py-1 bg-surface-elevated rounded-full text-xs">
                  {g.nombre}
                </span>
              ))}
            </div>

            <div className="flex flex-wrap gap-3 mb-6">
              <button className="flex items-center gap-2 px-6 py-3 bg-foreground text-background font-semibold rounded hover:bg-foreground/85 transition-colors">
                <Play className="size-5 fill-current" /> Reproducir
              </button>
              <button
                onClick={toggleMiLista}
                className="flex items-center gap-2 px-6 py-3 bg-surface-elevated text-foreground font-semibold rounded hover:bg-surface-elevated/80 transition-colors"
              >
                {enMiLista ? <Check className="size-5" /> : <Plus className="size-5" />}
                {enMiLista ? "En tu lista" : "Mi lista"}
              </button>
            </div>

            <div>
              <p className="text-sm text-muted-foreground mb-2">Tu calificación:</p>
              <div className="flex gap-1">
                {[1, 2, 3, 4, 5].map((n) => (
                  <button key={n} onClick={() => calificar(n)} aria-label={`${n} estrellas`}>
                    <Star
                      className={`size-7 transition-colors ${
                        n <= puntaje ? "text-gold fill-current" : "text-muted-foreground hover:text-gold"
                      }`}
                    />
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* TEMPORADAS / EPISODIOS */}
      {temporadas.length > 0 && (
        <section className="px-4 md:px-12 max-w-5xl mt-12 space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-2xl font-bold">Episodios</h2>
            <select
              value={tempActiva}
              onChange={(e) => setTempActiva(Number(e.target.value))}
              className="bg-surface-elevated border border-border rounded px-4 py-2 text-sm"
            >
              {temporadas.map((t) => (
                <option key={t.id} value={t.id}>
                  Temporada {t.numero}
                </option>
              ))}
            </select>
          </div>
          <ul className="divide-y divide-border">
            {temporadas
              .find((t) => t.id === tempActiva)
              ?.episodios.map((ep) => {
                const visto = episodiosTerminados.has(ep.id);
                return (
                  <li
                    key={ep.id}
                    className="py-4 flex items-center gap-4 hover:bg-surface/50 px-3 rounded transition-colors group"
                  >
                    <span className="text-2xl text-muted-foreground w-8 text-center">{ep.numero}</span>
                    <div className="size-12 rounded bg-surface-elevated flex items-center justify-center group-hover:bg-primary transition-colors">
                      <Play className="size-5 fill-current" />
                    </div>
                    <div className="flex-1">
                      <h3 className="font-semibold flex items-center gap-2">
                        {ep.titulo}
                        {visto && <Check className="size-4 text-primary" />}
                      </h3>
                      {ep.descripcion && (
                        <p className="text-sm text-muted-foreground line-clamp-1">{ep.descripcion}</p>
                      )}
                    </div>
                    <span className="text-sm text-muted-foreground">{ep.duracion_min}m</span>
                  </li>
                );
              })}
          </ul>
        </section>
      )}

      {similares.length > 0 && (
        <div className="mt-16">
          <ContentRow titulo="Títulos similares" items={similares} />
        </div>
      )}
    </div>
  );
}
