import { useRef } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import type { Contenido } from "@/lib/mock-data";
import { ContentCard } from "./content-card";

export function ContentRow({ titulo, items }: { titulo: string; items: Contenido[] }) {
  const ref = useRef<HTMLDivElement>(null);

  const scroll = (dir: "left" | "right") => {
    if (!ref.current) return;
    const amount = ref.current.clientWidth * 0.8;
    ref.current.scrollBy({ left: dir === "left" ? -amount : amount, behavior: "smooth" });
  };

  return (
    <section className="space-y-3 group/row">
      <h2 className="text-xl md:text-2xl font-bold px-4 md:px-12">{titulo}</h2>
      <div className="relative">
        <button
          onClick={() => scroll("left")}
          className="hidden md:flex absolute left-0 top-0 bottom-0 z-20 w-12 items-center justify-center bg-background/60 opacity-0 group-hover/row:opacity-100 transition-opacity"
          aria-label="Anterior"
        >
          <ChevronLeft className="size-8" />
        </button>
        <div
          ref={ref}
          className="flex gap-3 overflow-x-auto scrollbar-hide px-4 md:px-12 pb-4"
        >
          {items.map((c) => (
            <ContentCard key={c.id} contenido={c} />
          ))}
        </div>
        <button
          onClick={() => scroll("right")}
          className="hidden md:flex absolute right-0 top-0 bottom-0 z-20 w-12 items-center justify-center bg-background/60 opacity-0 group-hover/row:opacity-100 transition-opacity"
          aria-label="Siguiente"
        >
          <ChevronRight className="size-8" />
        </button>
      </div>
    </section>
  );
}
