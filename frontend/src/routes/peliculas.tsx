import { createFileRoute } from "@tanstack/react-router";
import { Navbar } from "@/components/navbar";
import { ContentCard } from "@/components/content-card";
import { contenidos } from "@/lib/mock-data";

export const Route = createFileRoute("/peliculas")({
  head: () => ({
    meta: [
      { title: "Películas — Streamio" },
      { name: "description", content: "Catálogo completo de películas." },
    ],
  }),
  component: Peliculas,
});

function Peliculas() {
  const pelis = contenidos.filter((c) => c.tipo === "pelicula");

  // ============================================================
  // ENDPOINT FastAPI:
  // GET /api/contenidos?tipo=pelicula
  //   -> Contenido[] paginado
  // ============================================================

  return (
    <div className="min-h-screen pt-24 pb-20 px-4 md:px-12">
      <Navbar />
      <h1 className="text-3xl md:text-5xl font-bold mb-8">Películas</h1>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4">
        {pelis.map((c) => (
          <ContentCard key={c.id} contenido={c} />
        ))}
      </div>
    </div>
  );
}
