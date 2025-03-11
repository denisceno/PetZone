import path from "path";

export default {
  mode: "development", // or "production"
  entry: {
    main: "./static/js/main.js",
    appointments_home: "./static/js/appointments_home.js",
    products_detail: "./static/js/products_detail.js",
  },
  output: {
    filename: "[name].bundle.js",
    path: path.resolve(process.cwd(), "static/js"),
  },
};
