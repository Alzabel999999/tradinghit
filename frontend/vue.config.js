const { defineConfig } = require('@vue/cli-service')
const path = require('path');
// Путь к приложению в котором храниться статика django
//const static_dir = 'public/static'
// Путь, относительно static_dir
// В него webpack положит шаблон Vue приложения
//const template_path = '../../templates/index.html'

module.exports = {
  publicPath: '/home/tradinghit/src/public/static/src/vue/dist/', // Should be STATIC_URL + path/to/build
    outputDir: '/home/tradinghit/src/public/static/src/vue/dist/', // Output to a directory in STATICFILES_DIRS
    filenameHashing: false, // Django will hash file names, not webpack
    runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
    devServer: {
      devMiddleware: {
        // см. https://github.com/webpack/webpack-dev-server/issues/2958
         writeToDisk: true,
      }
    },
}
