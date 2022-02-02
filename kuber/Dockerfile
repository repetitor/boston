FROM repetitor202/php-fpm:7.4.27-laradock-debian11
#FROM repetitor202/workspace:laradock-ubuntu20.04

# RUN apt-get update
# RUN apt-get install  -yf composer

# COPY --chown=docker:docker . /var/www/html
COPY  ./laravel/ /var/www/html

# RUN composer install --quiet --optimize-autoloader --no-dev