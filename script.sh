#!/bin/bash

Help()
{
  echo "Usage ./script.sh [OPTION]"
  echo
  echo "Syntax: ./script.sh [-h|r]"
  echo "options:"
  echo "-h     Print this Help."
  echo "-r     Remove gitignore-artefacts from other branches."
  echo
}

RemoveArtefacts()
{
  pathCurrentScript=$(dirname "$0")
  sudo rm -rf  "$pathCurrentScript"/laradock/
  rm -rf  "$pathCurrentScript"/larakube/
  rm -rf  "$pathCurrentScript"/laravel/
  sudo rm -rf  "$pathCurrentScript"/minilaradock/
  rm -rf  "$pathCurrentScript"/sandbox/
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

Help
