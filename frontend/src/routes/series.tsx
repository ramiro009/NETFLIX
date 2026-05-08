import { createFileRoute } from "@tanstack/react-router";
import { Navbar } from "@/components/navbar";
import { ContentCard } from "@/components/content-card";
import { contenidos } from "@/lib/mock-data";

export const Route = createFileRoute("/series")({
  head: () => ({
    meta: [
      { title: "Series — Streamio" },
      { name: "description", content: "Catálogo completo de series." },
    ],
  }),
  component: Series,
});

function Series() {
  const series = contenidos.filter((c) => c.tipo === "serie");

  // ============================================================
  // ENDPOINT FastAPI:
  // GET /api/contenidos?tipo=serie&genero={genero_id}&orden=anio
  //   -> Contenido[] paginado
  //   SQL: SELECT * FROM contenidos WHERE tipo = 'serie' ORDER BY anio DESC LIMIT $1 OFFSET $2;
  // ============================================================

  return (
    <div className="min-h-screen pt-24 pb-20 px-4 md:px-12">
      <Navbar />
      <h1 className="text-3xl md:text-5xl font-bold mb-8">Series</h1>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4">
        {series.map((c) => (
          <ContentCard key={c.id} contenido={c} />
        ))}
      </div>
    </div>
  );
}
