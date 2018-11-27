const gulp = require('gulp');
const plumber = require('gulp-plumber');
const rename = require('gulp-rename');
const autoprefixer = require('gulp-autoprefixer');
const uglify = require('gulp-uglify-es').default;
const minifycss = require('gulp-minify-css');
const sass = require('gulp-sass');
const ts = require('gulp-typescript');
const sourcemaps = require('gulp-sourcemaps');
const tsProject = ts.createProject('tsconfig.json');

gulp.task('styles', () => {
    gulp.src(['scss/**/*.scss'])
        .pipe(plumber({
            errorHandler(error) {
                console.log(error.message);
                this.emit('end');
            },
        }))
        .pipe(sass())
        .pipe(autoprefixer('last 2 versions'))
        .pipe(gulp.dest('../static/css/'))
        .pipe(rename({ suffix: '.min' }))
        .pipe(minifycss())
        .pipe(gulp.dest('../static/css/'));
});

gulp.task('scripts', () => gulp.src('typescript/**/*.ts')
    .pipe(plumber({
        errorHandler(error) {
            console.log(error.message);
            this.emit('end');
        },
    }))
    .pipe(sourcemaps.init())
    .pipe(tsProject())
    .pipe(rename(p => {
        if(p.dirname === 'core') {
            p.dirname = '';
            p.basename = 'core';
        }
    }))
    .pipe(gulp.dest('tmp'))
    .pipe(uglify())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('../static/js/')));

gulp.task('default', () => {
    gulp.watch('scss/**/*.scss', ['styles']);
    gulp.watch('ts/**/*.js', ['scripts']);
});
