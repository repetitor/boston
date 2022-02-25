#!/bin/bash

Help()
{
  echo "Usage ./script.sh [OPTION]"
  echo
  echo "Syntax: ./script.sh [-b|c|d|e|h|n|q|s|u]"
  echo "options:"
  echo "-b     Build Laravel-environment (build mariadb, nginx, php-fpm, workspace)."
  echo "-e     Prepare Laradock .env file."
  echo "-h     Print this Help."
  echo "-n     Rebuild (no-cache) Laravel-environment (build mariadb, nginx, php-fpm, workspace)."
  echo "-q     Quick-Up Laravel-environment (build mariadb, nginx, php-fpm, workspace)."
  echo "-s     Stop all containers."
  echo "-u     Up Laravel-environment (build mariadb, nginx, php-fpm, workspace)."
  echo
}

PrepareLaradockEnvFile()
{
  pathCurrentScript=$(dirname "$0")
  pathProject="$pathCurrentScript"/laradock

  cp  "$pathProject"/.env.example "$pathProject"/.env

#  PrepareLaradockEnvFileSetBuildParams
  sed -i 's@COMPOSE_PROJECT_NAME=laradock@COMPOSE_PROJECT_NAME=laradock-boston@' "$pathProject"/.env
  sed -i 's@WORKSPACE_INSTALL_PHPREDIS=true@WORKSPACE_INSTALL_PHPREDIS=false@' "$pathProject"/.env
  sed -i 's@WORKSPACE_INSTALL_MEMCACHED=true@WORKSPACE_INSTALL_MEMCACHED=false@' "$pathProject"/.env
  sed -i 's@WORKSPACE_INSTALL_XDEBUG=false@WORKSPACE_INSTALL_XDEBUG=true@' "$pathProject"/.env
  sed -i 's@PHP_FPM_XDEBUG_PORT=9003@PHP_FPM_XDEBUG_PORT=9013@' "$pathProject"/.env

#  PrepareLaradockEnvFileSetUpParams
  sed -i 's@APP_CODE_PATH_HOST=../@APP_CODE_PATH_HOST=../../_support/boston-laravel/laravel/@' "$pathProject"/.env
  sed -i 's@DATA_PATH_HOST=~/.laradock/data@DATA_PATH_HOST=~/.laradock/data-boston@' "$pathProject"/.env
  sed -i 's@PHP_IDE_CONFIG=serverName=laradock@PHP_IDE_CONFIG=serverName=laradock-boston@' "$pathProject"/.env
  sed -i 's@PHP_FPM_XDEBUG_PORT=9003@PHP_FPM_XDEBUG_PORT=9013@' "$pathProject"/.env
}

PrepareLaradockEnvFileSetBuildParams()
{
  pathCurrentScript=$(dirname "$0")
  pathProject="$pathCurrentScript"/laradock

  cp  "$pathProject"/.env.example "$pathProject"/.env

  sed -i 's@COMPOSE_PROJECT_NAME=laradock@COMPOSE_PROJECT_NAME=laradock-boston@' "$pathProject"/.env
  sed -i 's@WORKSPACE_INSTALL_PHPREDIS=true@WORKSPACE_INSTALL_PHPREDIS=false@' "$pathProject"/.env
  sed -i 's@WORKSPACE_INSTALL_MEMCACHED=true@WORKSPACE_INSTALL_MEMCACHED=false@' "$pathProject"/.env
  sed -i 's@WORKSPACE_INSTALL_XDEBUG=false@WORKSPACE_INSTALL_XDEBUG=true@' "$pathProject"/.env
  sed -i 's@PHP_FPM_XDEBUG_PORT=9003@PHP_FPM_XDEBUG_PORT=9013@' "$pathProject"/.env
}

PrepareLaradockEnvFileSetUpParams()
{
  pathCurrentScript=$(dirname "$0")
  pathProject="$pathCurrentScript"/laradock

  cp  "$pathProject"/.env.example "$pathProject"/.env

  sed -i 's@APP_CODE_PATH_HOST=../@APP_CODE_PATH_HOST=../../_support/boston-laravel/laravel/@' "$pathProject"/.env
  sed -i 's@DATA_PATH_HOST=~/.laradock/data@DATA_PATH_HOST=~/.laradock/data-boston@' "$pathProject"/.env
  sed -i 's@PHP_IDE_CONFIG=serverName=laradock@PHP_IDE_CONFIG=serverName=laradock-boston@' "$pathProject"/.env
  sed -i 's@PHP_FPM_XDEBUG_PORT=9003@PHP_FPM_XDEBUG_PORT=9013@' "$pathProject"/.env
}

BuildLaravelEnvironment()
{
  PrepareLaradockEnvFile

  pathCurrentScript=$(dirname "$0")
  pathProject="$pathCurrentScript"/laradock

  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- build -- mariadb nginx php-fpm workspace
}

RebuildNoCacheLaravelEnvironment()
{
  PrepareLaradockEnvFile

  pathCurrentScript=$(dirname "$0")
  pathProject="$pathCurrentScript"/laradock

  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- build --no-cache -- mariadb nginx php-fpm workspace
}

QuickUpLaravelEnvironment()
{
  pathCurrentScript=$(dirname "$0")
  pathProject="$pathCurrentScript"/laradock

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
    -- exec --user=laradock -- workspace  php artisan migrate
  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env \
    -- exec --user=laradock -- workspace  php artisan test
}

UpLaravelEnvironment()
{
  BuildLaravelEnvironment
  QuickUpLaravelEnvironment
}

Stop()
{
  pathCurrentScript=$(dirname "$0")
  pathProject="$pathCurrentScript"/laradock

  docker-compose -f "$pathProject"/docker-compose.yml --env-file "$pathProject"/.env -- stop
}

while getopts ":bcdehnqsu" option; do
   # shellcheck disable=SC2220
   case $option in
      b) BuildLaravelEnvironment
         exit;;
      c) PrepareLaradockEnvFileSetBuildParams
         exit;;
      d) PrepareLaradockEnvFileSetUpParams
         exit;;
      e) PrepareLaradockEnvFile
         exit;;
      h) Help
         exit;;
      n) RebuildNoCacheLaravelEnvironment
         exit;;
      q) QuickUpLaravelEnvironment
         exit;;
      s) Stop
         exit;;
      u) UpLaravelEnvironment
         exit;;
   esac
done

Help