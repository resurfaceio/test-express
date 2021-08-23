// Imports
import { GraphQLObjectType } from "graphql";
// App Imports
import * as news from "./news/fields/query";

// Query
const query = new GraphQLObjectType({
  name: "query",
  description: "...",

  fields: () => ({
    ...news,
  }),
});

export default query;
