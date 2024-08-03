import styles from "./App.module.css";

import React from "react";

export interface AppProps {
  myProps: string;
}

export const App = ({ myProps }: AppProps) => {
  return <div className={styles.container}>MyProps {myProps}</div>;
};
