const path = require('path');
const djangoStaticFilesDir = 'staticfiles';
const djangoStaticUrl = '/static/';
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = [
  {
    entry: {
      app: './js/app.js'
    },

    output: {
      path: path.resolve(__dirname, `../${djangoStaticFilesDir}`),
      publicPath: djangoStaticUrl,
      filename: '[name].js',
      chunkFilename: '[id]-[chunkhash].js'
    },

    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /(node_modules)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env']
            }
          }
        },
        {
          test: /\.(sa|sc|c)ss$/,
          use: [
            {
              loader: MiniCssExtractPlugin.loader
            },
            {
              loader: 'css-loader'
            },
            {
              loader: 'postcss-loader'
            },
            {
              loader: 'sass-loader',
              options: {
                implementation: require('sass')
              }
            }
          ]
        },
        {
          test: /\.(png|jpg|jpeg|gif|svg)$/,
          use: [
            {
              loader: 'file-loader',
              options: {
                outputPath: 'images'
              }
            }
          ]
        },
        {
          test: /\.(woff|woff2|ttf|otf|eot)$/,
          use: [
            {
              loader: 'file-loader',
              options: {
                outputPath: 'fonts'
              }
            }
          ]
        }
      ],
    },
  
    plugins: [
      new MiniCssExtractPlugin({
        filename: 'app.css'
      })
    ]
  },
];