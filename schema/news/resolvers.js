// App Imports
import models from "../../models";

// Get news by ID
export async function getById(parentValue, { id }) {
  return await models.News.findOne({ where: { id } });
}

// Get all news
export async function getAll() {
  return await models.News.findAll({ order: [["createdAt", "DESC"]] });
}

// Create news
export async function create(parentValue, { title, body }) {
  return await models.News.create({ title, body });
}

// Delete news
export async function remove(parentValue, { id }) {
  const status = await models.News.destroy({
    where: {},
    truncate: true,
  });
  if (status === 0) {
    return { ok: true };
  } else return { ok: false };
}
