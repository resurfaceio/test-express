// News
export default (sequelize, DataTypes) => {
  return sequelize.define("news", {
    title: {
      type: DataTypes.STRING,
    },
    body: {
      type: DataTypes.TEXT,
    },
  });
};
