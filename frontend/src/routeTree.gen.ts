/* prettier-ignore-start */

/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file is auto-generated by TanStack Router

import { createFileRoute } from "@tanstack/react-router";

// Import Routes

import { Route as rootRoute } from "./routes/__root";
import { Route as DashboardImport } from "./routes/_dashboard";

// Create Virtual Routes

const LoginLazyImport = createFileRoute("/login")();
const DashboardIndexLazyImport = createFileRoute("/_dashboard/")();

// Create/Update Routes

const LoginLazyRoute = LoginLazyImport.update({
  path: "/login",
  getParentRoute: () => rootRoute
} as any).lazy(() => import("./routes/login.lazy").then((d) => d.Route));

const DashboardRoute = DashboardImport.update({
  id: "/_dashboard",
  getParentRoute: () => rootRoute
} as any);

const DashboardIndexLazyRoute = DashboardIndexLazyImport.update({
  path: "/",
  getParentRoute: () => DashboardRoute
} as any).lazy(() =>
  import("./routes/_dashboard/index.lazy").then((d) => d.Route)
);

// Populate the FileRoutesByPath interface

declare module "@tanstack/react-router" {
  interface FileRoutesByPath {
    "/_dashboard": {
      preLoaderRoute: typeof DashboardImport;
      parentRoute: typeof rootRoute;
    };
    "/login": {
      preLoaderRoute: typeof LoginLazyImport;
      parentRoute: typeof rootRoute;
    };
    "/_dashboard/": {
      preLoaderRoute: typeof DashboardIndexLazyImport;
      parentRoute: typeof DashboardImport;
    };
  }
}

// Create and export the route tree

export const routeTree = rootRoute.addChildren([
  DashboardRoute.addChildren([DashboardIndexLazyRoute]),
  LoginLazyRoute
]);

/* prettier-ignore-end */
