#!/bin/bash

Help()
{
  echo "Usage ./script.sh [OPTION]"
  echo
  echo "Syntax: ./script.sh [-b|h|s|u]"
  echo "options:"
  echo "-b     Build Laravel-environment (build mariadb, nginx, php-fpm, workspace)."
  echo "-h     Print this Help."
  echo "-s     Stop Laravel-environment (build mariadb, nginx, php-fpm, workspace)."
  echo "-u     Up Laravel-environment (build mariadb, nginx, php-fpm, workspace)."
  echo
}

BuildLaravelEnvironment()
{
  pathCurrentScript=$(dirname "$0")
  pathProject="$pathCurrentScript"/laradock

  cp  "$pathProject"/.env.example "$pathProject"/.env

  sed -i 's@APP_CODE_PATH_HOST=../@APP_CODE_PATH_HOST=../../_support/boston-laravel/laravel/@' "$pathProject"/.env
  sed -i 's@DATA_PATH_HOST=~/.laradock/data@DATA_PATH_HOST=~/.laradock/data-boston@' "$pathProject"/.env
  sed -i 's@COMPOSE_PROJECT_NAME=laradock@COMPOSE_PROJECT_NAME=laradock-boston@' "$pathProject"/.env
  sed -i 's@PHP_IDE_CONFIG=serverName=laradock@PHP_IDE_CONFIG=serverName=laradock-boston@' "$pathProject"/.env
  sed -i 's@WORKSPACE_INSTALL_PHPREDIS=true@WORKSPACE_INSTALL_PHPREDIS=false@' "$pathProject"/.env
  sed -i 's@WORKSPACE_INSTALL_MEMCACHED=true@WORKSPACE_INSTALL_MEMCACHED=false@' "$pathProject"/.env

  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- build -- mariadb nginx php-fpm workspace
}

UpLaravelEnvironment()
{
  BuildLaravelEnvironment

  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- up -d -- mariadb nginx php-fpm workspace

  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- exec --user=laradock -- workspace composer install

  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- exec --user=laradock -- workspace cp .env.example .env

  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- exec --user=laradock -- workspace  sed -i 's@DB_HOST=127.0.0.1@DB_HOST=mariadb@' .env
  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- exec --user=laradock -- workspace  sed -i 's@DB_DATABASE=laravel@DB_DATABASE=default@' .env
  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- exec --user=laradock -- workspace  sed -i 's@DB_USERNAME=root@DB_USERNAME=default@' .env
  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- exec --user=laradock -- workspace  sed -i 's@DB_PASSWORD=@DB_PASSWORD=secret@' .env

  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- exec --user=laradock -- workspace  php artisan key:generate

  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- exec --user=laradock -- workspace  php artisan test
}

StopLaravelEnvironment()
{
  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- stop -- mariadb nginx php-fpm workspace
}

while getopts ":bhsu" option; do
   # shellcheck disable=SC2220
   case $option in
      b) BuildLaravelEnvironment
         exit;;
      h) Help
         exit;;
      s) StopLaravelEnvironment
         exit;;
      u) UpLaravelEnvironment
         exit;;
   esac
done

Help