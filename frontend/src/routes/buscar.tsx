import { createFileRoute } from "@tanstack/react-router";
import { Navbar } from "@/components/navbar";
import { ContentCard } from "@/components/content-card";
import { contenidos } from "@/lib/mock-data";
import { Search } from "lucide-react";
import { useState, useMemo } from "react";

export const Route = createFileRoute("/buscar")({
  head: () => ({
    meta: [
      { title: "Buscar — Streamio" },
      { name: "description", content: "Buscá películas, series y géneros." },
    ],
  }),
  component: Buscar,
});

function Buscar() {
  const [q, setQ] = useState("");

  // ============================================================
  // ENDPOINT FastAPI:
  // GET /api/contenidos/buscar?q={texto}
  //   -> Contenido[] (búsqueda full-text en titulo y descripcion)
  //   SQL: SELECT * FROM contenidos
  //        WHERE titulo ILIKE '%' || $1 || '%'
  //           OR descripcion ILIKE '%' || $1 || '%'
  //        LIMIT 50;
  //
  // Para búsqueda más avanzada usar pg_trgm o tsvector.
  // ============================================================

  const resultados = useMemo(() => {
    if (!q.trim()) return [];
    const t = q.toLowerCase();
    return contenidos.filter(
      (c) =>
        c.titulo.toLowerCase().includes(t) ||
        c.descripcion.toLowerCase().includes(t) ||
        c.generos.some((g) => g.nombre.toLowerCase().includes(t))
    );
  }, [q]);

  return (
    <div className="min-h-screen pt-24 pb-20 px-4 md:px-12">
      <Navbar />
      <div className="max-w-2xl mb-10">
        <div className="relative">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 size-5 text-muted-foreground" />
          <input
            type="text"
            autoFocus
            placeholder="Buscar películas, series, géneros..."
            value={q}
            onChange={(e) => setQ(e.target.value)}
            className="w-full pl-12 pr-4 py-4 bg-surface-elevated border border-border rounded-lg text-lg focus:outline-none focus:border-primary transition-colors"
          />
        </div>
      </div>

      {q.trim() && (
        <p className="text-muted-foreground mb-6">
          {resultados.length} resultado{resultados.length !== 1 && "s"} para "{q}"
        </p>
      )}

      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4">
        {resultados.map((c) => (
          <ContentCard key={c.id} contenido={c} />
        ))}
      </div>
    </div>
  );
}
