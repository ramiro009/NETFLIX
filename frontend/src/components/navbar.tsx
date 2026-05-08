import { Link, useLocation, useNavigate } from "@tanstack/react-router";
import { Search, Bell, ChevronDown } from "lucide-react";
import { useEffect, useState } from "react";

const links = [
  { to: "/browse", label: "Inicio" },
  { to: "/series", label: "Series" },
  { to: "/peliculas", label: "Películas" },
  { to: "/mi-lista", label: "Mi Lista" },
];

export function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled ? "bg-background/95 backdrop-blur-md" : "bg-gradient-to-b from-background/80 to-transparent"
      }`}
    >
      <nav className="flex items-center justify-between px-4 md:px-12 h-16">
        <div className="flex items-center gap-8">
          <Link to="/browse" className="font-display text-3xl tracking-wider text-primary">
            STREAMIO
          </Link>
          <ul className="hidden md:flex items-center gap-6 text-sm">
            {links.map((l) => (
              <li key={l.to}>
                <Link
                  to={l.to}
                  className={`transition-colors hover:text-foreground ${
                    location.pathname === l.to ? "text-foreground font-semibold" : "text-muted-foreground"
                  }`}
                >
                  {l.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>
        <div className="flex items-center gap-4">
          <button
            onClick={() => navigate({ to: "/buscar" })}
            className="p-2 hover:text-primary transition-colors"
            aria-label="Buscar"
          >
            <Search className="size-5" />
          </button>
          <button className="p-2 hover:text-primary transition-colors hidden sm:block" aria-label="Notificaciones">
            <Bell className="size-5" />
          </button>
          <Link to="/" className="flex items-center gap-1 hover:text-primary transition-colors">
            <div className="size-8 rounded bg-surface-elevated flex items-center justify-center text-lg">
              🦊
            </div>
            <ChevronDown className="size-4" />
          </Link>
        </div>
      </nav>
    </header>
  );
}
