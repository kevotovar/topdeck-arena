const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
  context: __dirname,
  entry: {
    main: path.resolve('./static/js/main.js'),
    styles: path.resolve('./static/js/styles.js'),
  },
  output: {
    path: path.resolve('./static/bundle/'),
    filename: '[name].js',
    publicPath: 'static/bundle/',
  },
  plugins: [
    new BundleTracker({ filename: './webpack-stats.json' }),
    new CleanWebpackPlugin(['./static/bundle/']),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader'],
      },
      {
        test: /\.(scss)$/,
        use: [
          'style-loader',
          'css-loader',
          {
            loader: 'postcss-loader',
            options: {
              plugins: function() {
                return [require('precss'), require('autoprefixer')];
              },
            },
          },
          'sass-loader',
        ],
      },
      {
        test: /\.(png|jpg)$/,
        use: ['file-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['*', '.js', '.jsx'],
  },
};
