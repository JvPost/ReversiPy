const gulp = require('gulp');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
const minify = require('gulp-minify');
const order = require('gulp-order');
const concat = require('gulp-concat');
const cleanCss = require('gulp-clean-css');
const browserSync = require('browser-sync');
const {series, parallel} = require('gulp');


const src = 'UI/src';
const dist = 'UI/dist';


'use strict'

gulp.task('sass', (done) => {
    return gulp.src(src+"/sass/**/*.scss") 
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer())
        .pipe(gulp.dest(src+"/css"));
}); 

gulp.task('watch',() => {
    browserSync.init({
        notify: false,
        proxy:  "localhost:5000"
    });
    // gulp.watch(src+"/sass/**/*.scss", series('sass'));

    gulp.watch(src+"/*.html", series('build-html'));
    gulp.watch(src+"/js/**/*.js", series('build-js'));
    gulp.watch(src+"/sass/**/*.scss", series('build-css'));

    // TODO: add templates

    gulp.watch(src+"/sass/**/*.scss").on('change', browserSync.reload);
    gulp.watch(src+"/js/**/*.js").on('change', browserSync.reload);
    gulp.watch(src+'/**/*.html').on('change', browserSync.reload);
});

gulp.task('build-js', (done) => {
    gulp.src(src+"/js/*.js")
        .pipe(order([
            'SPA.js',
            '*.js'
        ]))
        .pipe(concat("/app.js"))
        .pipe(minify())
        .pipe(gulp.dest(dist));
    done();
});
    
gulp.task('build-css', (done) => {
    gulp.src(src+'/sass/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer())
        .pipe(concat('/app.css'))
        .pipe(cleanCss({compatability: 'ie8'}))
        .pipe(gulp.dest(dist));
    done();
});

gulp.task('build-html', (done) => {
    gulp.src(src+'/*.html')
        .pipe(gulp.dest(dist))    
    done();
});

gulp.task('build', series(['build-js', 'build-css', 'build-html'])); // TODO add templates