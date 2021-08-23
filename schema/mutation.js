// Imports
import { GraphQLObjectType } from "graphql";
// App Imports
import * as news from "./news/fields/mutations";

// Mutation
const mutation = new GraphQLObjectType({
  name: "mutations",
  description: "...",

  fields: {
    ...news,
  },
});

export default mutation;
