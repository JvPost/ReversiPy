const gulp = require('gulp');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
const minify = require('gulp-minify');
const uglify = require('gulp-uglify-es').default;
const order = require('gulp-order');
const concat = require('gulp-concat');
const cleanCss = require('gulp-clean-css');
const browserSync = require('browser-sync');
const {series, parallel} = require('gulp');
const useref = require('gulp-useref');

const handlebars = require('gulp-handlebars');
const declare = require('gulp-declare');
const wrap = require('gulp-wrap');

const src = 'UI/src';
const dist = 'UI/dist';


'use strict'

gulp.task('templates', (done) => {
    return gulp.src(src+"/templates/**/*.hbs")
        .pipe(handlebars())
        .pipe(wrap('Handlebars.template(<%= contents %>)'))
        .pipe(declare({
            namespace: 'Handlebars.spa', // used in html files
            noRedeclare: true, // Avoid duplicat declarations
        }))
        .pipe(concat('templates.js'))
        .pipe(gulp.dest(src+"/js"));
});

gulp.task('sass', (done) => {
    return gulp.src(src+"/sass/**/*.scss") 
        .pipe(sass().on('error', sass.logError))
        .pipe(cleanCss({compatability: 'ie8'}))
        .pipe(autoprefixer())
        .pipe(gulp.dest(src+"/css"));
}); 

gulp.task('watch',() => {
    browserSync.init({
        notify: false,
        proxy:  "localhost:5000"
    });

    gulp.watch(src+"/sass/**/*.scss", series('sass'));
    gulp.watch(src+"/templates/**/*.hbs", series('templates'));

    gulp.watch(src+"/css/**/*.css").on('change', browserSync.reload);
    gulp.watch(src+"/js/**/*.js").on('change', browserSync.reload);
    gulp.watch(src+'/**/*.html').on('change', browserSync.reload);
    gulp.watch(src+"/templates/**/*.hbs").on('change', browserSync.reload);
});

gulp.task('build-js', (done) => {
    gulp.src([
        src+"/js/*.js",
        '!'+src+'/js/templates.js'
        ])
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
    gulp.src(src+'/css/**/*.css')
        .pipe(concat('/app.css'))
        .pipe(gulp.dest(dist));
    done();
});

gulp.task('build-html', (done) => {
    gulp.src(src+'/*.html')
        .pipe(useref({
            noAssets:true
        }))
        .pipe(gulp.dest(dist))    
    done();
});

gulp.task('build-templates', (done) => {
    gulp.src(src+'/js/templates.js')
        .pipe(gulp.dest(dist));
    done();
});

gulp.task('build', series(['build-js', 'build-css', 'build-html', 'build-templates']));