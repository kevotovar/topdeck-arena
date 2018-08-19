const path = require('path');
const merge = require('webpack-merge');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

const common = require('./webpack.common.js');

module.exports = merge(common, {
  mode: 'production',
  output: {
    path: path.resolve('./static/bundle/'),
    filename: '[name]-[hash].js'
  },
  optimization: {
    minimizer: [
      new UglifyJsPlugin()
    ]
  }
});
