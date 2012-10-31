// RequireJS optimization configuration
// Full example: https://github.com/jrburke/r.js/blob/master/build/example.build.js

({
    // optiize relative to this url (i.e. the current directory)
    baseUrl: '.',
    
    // the source directory of the modules
    appDir: 'src',

    // the target directory of the optimized modules
    dir: 'min',

    optimize: 'uglify',

    optimizeCss: 'none',

    modules: []
})
