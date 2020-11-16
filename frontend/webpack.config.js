const path = require("path");
const HTMLWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: {
        main: "./src/index.js",
    },
    module: {
        rules: [
            {
                test: /\.js|.jsx$/,
                use: "babel-loader",
                resolve: {
                    extensions: [".js", ".jsx"]
                },
            },
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
        ],
    },
    plugins: [new HTMLWebpackPlugin({ template: "./src/index.html" })],
    output: {
        path: path.resolve(__dirname, "../backend/static/"),
        filename: "main.bundle.js",
    },
    devServer: {
        contentBase: [
            path.join(__dirname, "../backend/static"),
        ],
        port: 3000,
        watchOptions: {
            poll: true,
            ignored: ['node_modules/**']
        },
        sockPort: 3000,
    },
};
