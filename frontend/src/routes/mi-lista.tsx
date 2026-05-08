import { createFileRoute } from "@tanstack/react-router";
import { Navbar } from "@/components/navbar";
import { ContentCard } from "@/components/content-card";
import { contenidos, miLista } from "@/lib/mock-data";

export const Route = createFileRoute("/mi-lista")({
  head: () => ({
    meta: [
      { title: "Mi Lista — Streamio" },
      { name: "description", content: "Tu lista personal para ver más tarde." },
    ],
  }),
  component: MiLista,
});

function MiLista() {
  const items = contenidos.filter((c) => miLista.has(c.id));

  // ============================================================
  // ENDPOINT FastAPI:
  // GET /api/perfiles/{perfil_id}/mi-lista
  //   -> Contenido[] (JOIN mi_lista con contenidos)
  //   SQL: SELECT c.* FROM contenidos c
  //        JOIN mi_lista m ON m.contenido_id = c.id
  //        WHERE m.perfil_id = $1
  //        ORDER BY m.fecha_agregada DESC;
  // ============================================================

  return (
    <div className="min-h-screen pt-24 pb-20 px-4 md:px-12">
      <Navbar />
      <h1 className="text-3xl md:text-5xl font-bold mb-8">Mi Lista</h1>
      {items.length === 0 ? (
        <p className="text-muted-foreground">
          Tu lista está vacía. Agregá títulos desde la página de detalle.
        </p>
      ) : (
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4">
          {items.map((c) => (
            <ContentCard key={c.id} contenido={c} />
          ))}
        </div>
      )}
    </div>
  );
}
