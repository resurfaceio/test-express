// Imports
import { GraphQLInt, GraphQLList } from "graphql";
import { getAll, getById } from "../resolvers";
// App Imports
import { NewsType } from "../type";

// News All
export const allNews = {
  type: new GraphQLList(NewsType),
  resolve: getAll,
};

// Thought By ID
export const news = {
  type: NewsType,
  args: {
    id: { type: GraphQLInt },
  },
  resolve: getById,
};
