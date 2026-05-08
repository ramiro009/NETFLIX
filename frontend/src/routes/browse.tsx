import { createFileRoute, Link } from "@tanstack/react-router";
import { Navbar } from "@/components/navbar";
import { ContentRow } from "@/components/content-row";
import { contenidos, generos } from "@/lib/mock-data";
import { Play, Info } from "lucide-react";

export const Route = createFileRoute("/browse")({
  head: () => ({
    meta: [
      { title: "Inicio — Streamio" },
      { name: "description", content: "Las películas y series del momento, recomendadas para vos." },
    ],
  }),
  component: Browse,
});

function Browse() {
  const destacado = contenidos[0];

  // ============================================================
  // ENDPOINTS FastAPI sugeridos:
  //
  // GET /api/contenidos/destacado?perfil_id={id}
  //   -> Contenido (hero principal personalizado)
  //
  // GET /api/contenidos/tendencias?limit=10
  //   -> Contenido[]
  //
  // GET /api/contenidos/recomendados?perfil_id={id}
  //   -> Contenido[] (algoritmo basado en vistas y calificaciones)
  //
  // GET /api/perfiles/{perfil_id}/continuar-viendo
  //   -> Vista[] con joins a episodio + contenido
  //   SQL aprox:
  //     SELECT v.*, e.*, c.*
  //     FROM vistas v
  //     JOIN episodios e ON v.episodio_id = e.id
  //     JOIN temporadas t ON e.temporada_id = t.id
  //     JOIN contenidos c ON t.contenido_id = c.id
  //     WHERE v.perfil_id = $1 AND v.terminado = false
  //     ORDER BY v.fecha DESC LIMIT 10;
  //
  // GET /api/generos/{genero_id}/contenidos
  //   -> Contenido[] filtrados por género (JOIN con contenido_generos)
  // ============================================================

  return (
    <div className="min-h-screen pb-20">
      <Navbar />

      {/* HERO */}
      <section className="relative h-[85vh] w-full">
        <img
          src={destacado.backdrop}
          alt={destacado.titulo}
          className="absolute inset-0 h-full w-full object-cover"
        />
        <div className="absolute inset-0" style={{ background: "var(--gradient-hero)" }} />
        <div className="absolute inset-0 bg-gradient-to-r from-background/90 via-background/40 to-transparent" />
        <div className="relative h-full flex flex-col justify-end pb-24 md:pb-32 px-4 md:px-12 max-w-3xl">
          <div className="flex items-center gap-2 text-sm text-primary font-semibold uppercase tracking-widest mb-2">
            <span>★ Destacado</span>
            <span>•</span>
            <span>{destacado.tipo === "serie" ? "Serie" : "Película"}</span>
          </div>
          <h1 className="text-4xl md:text-7xl font-bold mb-4">{destacado.titulo}</h1>
          <p className="text-base md:text-lg text-foreground/90 mb-6 line-clamp-3 max-w-xl">
            {destacado.descripcion}
          </p>
          <div className="flex gap-3">
            <Link
              to="/contenido/$id"
              params={{ id: String(destacado.id) }}
              className="flex items-center gap-2 px-6 md:px-8 py-3 bg-foreground text-background font-semibold rounded hover:bg-foreground/85 transition-colors"
            >
              <Play className="size-5 fill-current" /> Reproducir
            </Link>
            <Link
              to="/contenido/$id"
              params={{ id: String(destacado.id) }}
              className="flex items-center gap-2 px-6 md:px-8 py-3 bg-surface-elevated/80 text-foreground font-semibold rounded hover:bg-surface-elevated transition-colors"
            >
              <Info className="size-5" /> Más información
            </Link>
          </div>
        </div>
      </section>

      {/* FILAS */}
      <div className="space-y-10 -mt-20 relative z-10">
        <ContentRow titulo="Tendencias ahora" items={contenidos.slice(0, 8)} />
        <ContentRow titulo="Continuar viendo" items={contenidos.slice(2, 8)} />
        {generos.slice(0, 3).map((g) => (
          <ContentRow
            key={g.id}
            titulo={g.nombre}
            items={contenidos.filter((c) => c.generos.some((gg) => gg.id === g.id))}
          />
        ))}
      </div>
    </div>
  );
}
