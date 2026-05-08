import { Link } from "@tanstack/react-router";
import type { Contenido } from "@/lib/mock-data";
import { Star } from "lucide-react";

export function ContentCard({ contenido }: { contenido: Contenido }) {
  return (
    <Link
      to="/contenido/$id"
      params={{ id: String(contenido.id) }}
      className="group relative flex-shrink-0 w-44 md:w-52 overflow-hidden rounded-md bg-surface transition-all duration-300 hover:scale-105 hover:z-10"
      style={{ boxShadow: "var(--shadow-card)" }}
    >
      <div className="aspect-[2/3] overflow-hidden">
        <img
          src={contenido.poster}
          alt={contenido.titulo}
          loading="lazy"
          className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110"
        />
      </div>
      <div className="absolute inset-0 bg-gradient-to-t from-background via-background/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-3">
        <h3 className="font-semibold text-sm line-clamp-2">{contenido.titulo}</h3>
        <div className="flex items-center gap-2 mt-1 text-xs text-muted-foreground">
          <span>{contenido.anio}</span>
          <span>•</span>
          <span className="uppercase">{contenido.tipo}</span>
          {contenido.rating_promedio && (
            <>
              <span>•</span>
              <span className="flex items-center gap-0.5 text-gold">
                <Star className="size-3 fill-current" />
                {contenido.rating_promedio}
              </span>
            </>
          )}
        </div>
      </div>
    </Link>
  );
}
