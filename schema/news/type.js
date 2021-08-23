// Imports
import {
  GraphQLBoolean,
  GraphQLInt,
  GraphQLObjectType,
  GraphQLString,
} from "graphql";

const NewsType = new GraphQLObjectType({
  name: "news",
  description: "...",

  fields: () => ({
    id: { type: GraphQLInt },
    title: { type: GraphQLString },
    body: { type: GraphQLString },
    createdAt: { type: GraphQLString },
    updatedAt: { type: GraphQLString },
  }),
});

const okType = new GraphQLObjectType({
  name: "ok",
  description: "...",

  fields: () => ({
    ok: { type: GraphQLBoolean },
  }),
});
export { NewsType, okType };
