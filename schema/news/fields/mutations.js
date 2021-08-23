// Imports
import { GraphQLString } from "graphql";
import { create, remove } from "../resolvers";
// App Imports
import { NewsType, okType } from "../type";

// News create
export const addNews = {
  type: NewsType,
  args: {
    title: {
      name: "title",
      type: GraphQLString,
    },

    body: {
      name: "body",
      type: GraphQLString,
    },
  },
  resolve: create,
};

// News remove
export const deleteEverything = {
  type: okType,
  args: {},

  resolve: remove,
};
