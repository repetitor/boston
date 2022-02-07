#!/bin/bash

Help()
{
  echo "Usage ./bro.sh [OPTION]"
  echo
  echo "Syntax: ./bro.sh [-h|r]"
  echo "options:"
  echo "h     Print this Help."
  echo "r     Remove gitignore-artefacts from other branches."
  echo
}

RemoveArtefacts()
{
  pathCurrentScript=$(dirname "$0")
  sudo rm -rf  "$pathCurrentScript"/kuber/ && \
    rm -rf  "$pathCurrentScript"/laradock/ && \
    rm -rf  "$pathCurrentScript"/laradock220204/ && \
    rm -rf  "$pathCurrentScript"/laravel/ && \
    rm -rf  "$pathCurrentScript"/minilaradock/
}

while getopts ":hr" option; do
   # shellcheck disable=SC2220
   case $option in
      h) Help
         exit;;
      r) RemoveArtefacts
         exit;;
   esac
done
