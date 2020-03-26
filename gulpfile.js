const gulp = require('gulp');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');
const uglify = require('gulp-uglify-es').default;
const pipeline = require('readable-stream').pipeline;
const concat = require('gulp-concat');
const cleanCss = require('gulp-clean-css');
const browserSync = require('browser-sync');
const htmlreplace = require('gulp-html-replace');
const {series, parallel} = require('gulp');


const reload = browserSync.reload;   
const src = 'UI/static/src';
const dist = 'UI/static/dist';


'use strict'

gulp.task('sass', (done) => {
    return gulp.src(src+"/sass/**/*.scss") 
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer())
        .pipe(gulp.dest(src+"/css"))
        .pipe(browserSync.stream());
}); 

gulp.task('watch',() => {
    browserSync.init({
        notify: false,
        proxy:  "localhost:5000"
    })
    gulp.watch(src+"/sass/**/*.scss", series('sass'));
    gulp.watch(src+"/css/**/*.css").on('change', browserSync.reload);
    gulp.watch(src+"/js/**/*.js").on('change', browserSync.reload);
    gulp.watch('UI/Templates/src/**/*.html').on('change', browserSync.reload);
});

gulp.task('build-js', (done) => {
    pipeline(
        gulp.src(src+'/js/*.js')
        .pipe(concat('/app.js')),
        uglify(),
        gulp.dest(dist)
    );
    done();
});
    
gulp.task('build-css', (done) => {
    gulp.src(src+'/css/*.css')
        .pipe(concat('/app.css'))
        .pipe(cleanCss({compatability: 'ie8'}))
        .pipe(gulp.dest(dist));
    done();
});

gulp.task('build-html', (done) => {
    // index
    gulp.src('UI/templates/src/index.html')
        .pipe(gulp.dest('UI/templates/dist/'));
    //game TODO
    gulp.src('UI/templates/src/reversi.html')
        .pipe(gulp.dest('UI/templates/dist/')); 
    done();
});

gulp.task('build', series(['build-js', 'build-css', 'build-html']));