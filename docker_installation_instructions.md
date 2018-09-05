## Registering for an account on dockerhub
- Go to https://hub.docker.com and register yourself (you can use any username and email address that you wish)
- Login to https://hub.docker.com

## Installing Docker and docker-compose
**Mac Users**:
- Download and Install: https://download.docker.com/mac/stable/Docker.dmg

**Windows 10 PRO**
- Download and Install: https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe
> If the above installer fails, try one form this link: https://docs.docker.com/docker-for-windows/release-notes/#stable-releases-of-2018

**Debian based OS (Linux Users)**
``` bash
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
$ sudo apt-get update
$ sudo apt-get install docker-ce
$ sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```

## Verify the installation was successful and login
``` bash
docker --version
docker-compose --version
docker login
```

## Running the container
- Clone the github repo (to run container using docker-compose. For other ways of running, checkout the README file in the repo)
``` bash
git clone https://github.com/Mohitsharma44/ucsl-image
cd ucsl-image/image/
```

**even if you cannot get this far due to installation issues, make sure you download both the docker image and the docker software**

- Edit docker-compose to point to the correct volume where you have the notebooks or want the notebooks to persist
``` yaml
version: '2.3'

services:
  ucsl:
    container_name: ucsl-container
    build:
      context: .
      args:
        NB_USER: ${NB_USER}
    image: mohitsharma44/ucsl-image:latest
    ports:
      - "8888:8888"
    volumes:
      - type: bind
        source: <relative or absolute path to your notebooks directory>
        target: /home/${NB_USER}/puinotebooks/
```
- Run the container
``` bash
$ cd ucsl-image/image
$ docker-compose up
```
> you can pass the -d flag to `docker-compose up` if you want to run this as a daemon

## Stopping the container
``` bash
docker stop ucsl-container
```
*OR*
``` bash
cd ucsl-image/image
docker-compose down
```
> To stop and delete the container
``` bash
docker rm -f ucsl-container
```
