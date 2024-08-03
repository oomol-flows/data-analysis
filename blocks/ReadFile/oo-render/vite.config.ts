import { join } from "node:path";
import { defineConfig } from "vite";
import externalGlobals from "rollup-plugin-external-globals";

export default defineConfig(({ mode }) => ({
  server: {
    port: Number(process.env.OO_RENDER_PORT || 0) || undefined,
  },
  root: join(__dirname, "dev"),
  build: {
    emptyOutDir: true,
    outDir: join(__dirname, "dist"),
    lib: {
      entry: join(__dirname, "src", "render.tsx"),
      name: "Render",
      formats: ["es"],
      fileName: () => "render.mjs",
    },
    rollupOptions: {
      external: ["react", "react-dom"],
      plugins: [
        externalGlobals({
          react: "__OOMOL_BUILTIN.React",
          "react-dom": "__OOMOL_BUILTIN.ReactDOM",
        }),
      ],
    },
  },
  define: {
    "process.env.NODE_ENV": JSON.stringify(mode),
  },
}));
