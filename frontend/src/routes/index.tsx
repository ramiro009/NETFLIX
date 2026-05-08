import { createFileRoute, Link } from "@tanstack/react-router";
import { perfiles } from "@/lib/mock-data";
import { Plus, Pencil } from "lucide-react";
import { useState } from "react";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "¿Quién está viendo? — Streamio" },
      { name: "description", content: "Elegí tu perfil para empezar a ver." },
    ],
  }),
  component: ProfileSelect,
});

function ProfileSelect() {
  const [editing, setEditing] = useState(false);

  // ============================================================
  // ENDPOINT FastAPI sugerido:
  // GET /api/cuentas/{cuenta_id}/perfiles
  // Devuelve: Perfil[] (id, cuenta_id, nombre, es_infantil, avatar)
  //
  // useEffect(() => {
  //   fetch(`${API_URL}/cuentas/${cuentaId}/perfiles`, {
  //     headers: { Authorization: `Bearer ${token}` }
  //   })
  //     .then(r => r.json())
  //     .then(setPerfiles);
  // }, [cuentaId]);
  // ============================================================

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-6">
      <h1 className="text-4xl md:text-6xl font-light mb-12 text-center">
        ¿Quién está viendo?
      </h1>
      <div className="flex flex-wrap gap-6 md:gap-10 justify-center max-w-4xl">
        {perfiles.map((p) => (
          <Link
            key={p.id}
            to="/browse"
            className="group flex flex-col items-center gap-3 cursor-pointer"
          >
            <div className="relative">
              <div className="size-24 md:size-36 rounded-md bg-surface-elevated flex items-center justify-center text-5xl md:text-7xl border-2 border-transparent group-hover:border-foreground transition-all">
                {p.avatar}
              </div>
              {editing && (
                <div className="absolute inset-0 bg-background/70 rounded-md flex items-center justify-center">
                  <Pencil className="size-8" />
                </div>
              )}
              {p.es_infantil && (
                <span className="absolute -top-2 -right-2 bg-primary text-primary-foreground text-xs px-2 py-0.5 rounded-full font-semibold">
                  KIDS
                </span>
              )}
            </div>
            <span className="text-muted-foreground group-hover:text-foreground transition-colors text-sm md:text-base">
              {p.nombre}
            </span>
          </Link>
        ))}
        <button className="group flex flex-col items-center gap-3">
          <div className="size-24 md:size-36 rounded-md bg-surface flex items-center justify-center text-muted-foreground group-hover:text-foreground border-2 border-dashed border-border group-hover:border-foreground transition-all">
            <Plus className="size-12" />
          </div>
          <span className="text-muted-foreground text-sm md:text-base">Agregar</span>
        </button>
      </div>
      <button
        onClick={() => setEditing((v) => !v)}
        className="mt-12 px-6 py-2 border border-muted-foreground text-muted-foreground hover:text-foreground hover:border-foreground transition-colors tracking-widest text-sm uppercase"
      >
        {editing ? "Listo" : "Administrar perfiles"}
      </button>
    </div>
  );
}
