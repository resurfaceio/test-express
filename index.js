// Imports
import express from "express";
import { HttpLoggerForExpress } from "resurfaceio-logger";
import setupGraphQL from "./setup/graphql";
// App Imports
import setupLoadModules from "./setup/loader";
import setupStartServer from "./setup/server";
// Create express server
const server = express();

HttpLoggerForExpress.add(server, {
  rules: "include debug",
});

server.get("/ping", function (request, response) {
  response.status(200).json({ msg: "pong" });
});

// Setup load modules
setupLoadModules(server);

// Setup GraphQL
setupGraphQL(server);

// Start server
setupStartServer(server);
