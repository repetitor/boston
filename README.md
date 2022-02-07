# boston (laradock)

## up
```shell
chmod +x script.sh
./script.sh -h
```

## troubles
### PHPREDIS
> docker-compose build workspace
>> Step 101/305 : RUN if [ ${INSTALL_PHPREDIS} = true ]; then     apt-get install -yqq php${LARADOCK_PHP_VERSION}-redis ;fi

solution: WORKSPACE_INSTALL_PHPREDIS=false

### MEMCACHED
>> Step 231/305 : RUN if [ ${INSTALL_MEMCACHED} = true ]; then   apt-get -y install php${LARADOCK_PHP_VERSION}-igbinary   && apt-get -y install php${LARADOCK_PHP_VERSION}-memcached ;fi

solution: WORKSPACE_INSTALL_MEMCACHED=false

### port is already allocated
> docker-compose up nginx mariadb

if:
```
Creating laradock_workspace_1        ... error

ERROR: for laradock_workspace_1  Cannot start service workspace: driver failed programming external connectivity on endpoint laradock_workspace_1 (a0e69adc2d153e924d6c8b431c87d18bd5efcddf4eac17ce32e59f8d877cf43a): Bind for 0.0.0.0:3000 failed: port is already allocated

ERROR: for workspace  Cannot start service workspace: driver failed programming external connectivity on endpoint laradock_workspace_1 (a0e69adc2d153e924d6c8b431c87d18bd5efcddf4eac17ce32e59f8d877cf43a): Bind for 0.0.0.0:3000 failed: port is already allocated
ERROR: Encountered errors while bringing up the project.
```

then:
```
WORKSPACE_BROWSERSYNC_HOST_PORT=30000
```

if:
```
Creating laradock_nginx_1       ... error

ERROR: for laradock_nginx_1  Cannot start service nginx: driver failed programming external connectivity on endpoint laradock_nginx_1 (05258db447edfcb766cb16b3895772c972128c4e68608317783257081467492a): Bind for 0.0.0.0:443 failed: port is already allocated

ERROR: for nginx  Cannot start service nginx: driver failed programming external connectivity on endpoint laradock_nginx_1 (05258db447edfcb766cb16b3895772c972128c4e68608317783257081467492a): Bind for 0.0.0.0:443 failed: port is already allocated
ERROR: Encountered errors while bringing up the project.
```

then:
```
NGINX_HOST_HTTPS_PORT=4430
```

if:
```
Recreating laradock_nginx_1 ... error

ERROR: for laradock_nginx_1  Cannot start service nginx: driver failed programming external connectivity on endpoint laradock_nginx_1 (60fe8fcd043577064431039ac9424d2a05c434deb198d9aa070aca4e9f223315): Bind for 0.0.0.0:80 failed: port is already allocated

ERROR: for nginx  Cannot start service nginx: driver failed programming external connectivity on endpoint laradock_nginx_1 (60fe8fcd043577064431039ac9424d2a05c434deb198d9aa070aca4e9f223315): Bind for 0.0.0.0:80 failed: port is already allocated
ERROR: Encountered errors while bringing up the project.
```

then:
```
NGINX_HOST_HTTP_PORT=800
```

## dockerhub
```shell
docker tag laradock_nginx:latest repetitor202/nginx:1.21.6-laradock-alpine3.15.0
docker login
docker push repetitor202/nginx:1.21.6-laradock-alpine3.15.0
```