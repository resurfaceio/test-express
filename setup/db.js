// Imports
import { Sequelize } from "sequelize";
import databaseConfig from "../config/db.json";
// App Imports
import env from "../config/env";

// Load database config
const databaseConfigEnv = databaseConfig[env];

// Create new database connection
const connection = new Sequelize(
  databaseConfigEnv.database,
  databaseConfigEnv.username,
  databaseConfigEnv.password,
  {
    host: databaseConfigEnv.host,
    dialect: databaseConfigEnv.dialect,
    logging: false,
    operatorsAliases: Sequelize.Op,
  }
);

// Test connection
console.info("SETUP - Connecting database...");

connection
  .authenticate()
  .then(() => {
    console.info("INFO - Database connected.");
  })
  .catch((err) => {
    console.error("ERROR - Unable to connect to the database:", err);
  });

export default connection;
