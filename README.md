# boston (laravel)

```shell
# deployment
cd laravel
#docker-compose up -d nginx mariadb
#docker-compose exec --user=laradock workspace bash
composer install
cp .env.example .env
php artisan key:generate
php artisan test
# exit
# docker-compose stop
```