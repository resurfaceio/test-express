// Imports
import Sequelize from "sequelize";
// App Imports
import databaseConnection from "../setup/db";

const models = {
  News: databaseConnection.import("./news"),
};

Object.keys(models).forEach((modelName) => {
  if ("associate" in models[modelName]) {
    models[modelName].associate(models);
  }
});

models.sequelize = databaseConnection;
models.Sequelize = Sequelize;

export default models;
