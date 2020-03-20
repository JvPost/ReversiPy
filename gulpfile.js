const gulp = require('gulp');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');

const {series, parallel} = require('gulp');

'use strict'

gulp.task('sass', (done) => {
    return gulp.src("UI/static/src/sass/**/*.scss") 
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest("UI/static/src/css"));
}); 

gulp.task('watch', () => {
    gulp.watch("UI/static/src/sass/**/*.scss", series('sass'));
});


// TODO: build task