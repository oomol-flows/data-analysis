import React from "react";
import { createRoot } from "react-dom/client";

import { App } from "./App";

export default {
  // TODO 补上 Renderer Context 类型
  setup(dom: HTMLDivElement, context: any) {
    const root = createRoot(dom);
    const styleURI = context.resolveStaticResource("oo-render/dist/style.css");
    root.render(
      <>
        <link rel="stylesheet" href={styleURI} />
        <App myProps={"myProps"} />
      </>
    );

    return () => {
      root.unmount();
    };
  },
};
