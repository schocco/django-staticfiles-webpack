# django-staticfiles-webpack

Simple StaticFilesStorage that can be used together with the assets-webpack-plugin to include hashed files.

## Why

Webpack comes with an option to hash static files for long term caching so that generated files look like:

 - Main.76def765eff56.js (entry point)
 - Bundle.1.689ef7cbade76.js (loaded on demand)
 - Bundle.2.873426ef56a5e.js (loaded on demand)

Bundle files are usually a result of code splitting. Webpack keeps track of the filename changes for you, however the
entry point files cannot be managed by Webpack easily when they need to be included in your Django templates.

When the [assets-webpack-plugin](https://github.com/sporto/assets-webpack-plugin) is added to the webpack configuration, then a json file is created which maps entry points
to generated file names.
This json file is read by the custom django staticfiles storage class to resolve the url for the entry point.


## Webpack Configuration

Install the assets plugin with `npm install --save-dev assets-webpack-plugin`
and include it in the plugins section of `webpack.conf.js`:

```javascript
AssetsPlugin = require('assets-webpack-plugin');
var entry = ['.src/app/App.js']
  
module.exports = {

    output =  {
        path: __dirname,
        filename: 'App.[name].[hash].js',
        chunkFilename: "App.[id].[chunkhash].js",
        publicPath: '/static/'
    };
plugins: [
    new AssetsPlugin() // writes webpack-assets.json file that can be read in by custom django storage class
],
    module
:
{
    loaders: [
        {test: /\.js?$/, exclude: /node_modules/, loader: 'babel-loader'},
        //your other loaders ...
    ]
}
```

When a build is completed, a `webpack-assets.json` file should be in the directory with a content like this:

```javascript
{"main":{"js":"App.main.7ebdf0b55c648ba41cc1.js"}}
```

Note that the entry point has been called 'main' as there was no name specified.
When multiple entry points are defined in a dict, then each key is reflected in the assets.json.
See the webpack [docs](https://webpack.github.io/docs/multiple-entry-points.html).


## Django Configuration

### STATICFILES_STORAGE
Name of the storage class: `webpack.storage.WebpackHashStorage`

### WEBPACK_ASSETS_FILE
A path pointing to the generated webpack-assets.json file. E.g. `"path-to-your/webpack-assets.json"`


## Need something more sophisticated?
Maybe https://github.com/owais/django-webpack-loader suits your needs.
