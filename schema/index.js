// Imports
import { GraphQLSchema } from "graphql";
import mutation from "./mutation";
// App Imports
import query from "./query";

// Schema
const schema = new GraphQLSchema({
  query,
  mutation,
});

export default schema;
