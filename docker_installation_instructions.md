**NOTE: even if you cannot get this far due to installation issues, make sure you download both the docker image and the docker software so we do not run into issues with slow wireless tomorrow: step 1, 2, and 4.1**



## 1 Registering for an account on dockerhub
- Go to https://hub.docker.com and register yourself (you can use any username and email address that you wish)
- Login to https://hub.docker.com

## 2 Installing Docker and docker-compose
**Mac Users**:
- Download and Install: https://download.docker.com/mac/stable/Docker.dmg

**Windows 10 PRO** [For people with issues installing Docker on Windows, check FAQ below]
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

## 3 Verify the installation was successful and login
``` bash
docker --version
docker-compose --version
docker login
```

## 4 Running the container
- 4.1 Clone the github repo (to run container using docker-compose. For other ways of running, checkout the README file in the repo)
``` bash
git clone https://github.com/Mohitsharma44/ucsl-image
cd ucsl-image/image/
```

- 4.2 Edit docker-compose to point to the correct volume where you have the notebooks or want the notebooks to persist
*You don't need to run this block of code. It is the content of ucsl-image/image/docker-compose.yml file.*

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

- 4.3 Run the container (see note below to change the username)
``` bash
$ cd ucsl-image/image
$ echo NB_USER=ucsl_user > .env
$ docker-compose up
```
> - If you want to personalize your container, you can use your own username inside the container; to do that you can do the following. 
>``` bash
>$ cd ucsl-image/image
>$ echo NB_USER=<your username> > .env
>$ docker-compose up build
>```

> - you can pass the -d flag to `docker-compose up` if you want to run this as a daemon

## 5 Stopping the container
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


## FAQ

- I'm running windows and during installation I get the following error:
```
Docker for Windows requires Windows 10 PRO or Enterprise version XXXXX or Windows Server XXXX RTM to run
```
Are you running Windows 10 **PRO**? [https://support.microsoft.com/en-us/help/13443/windows-which-operating-system](How to Check Windows version)
> Make sure you are running 64bit Windows 10 Pro, Enterprise (1607 Anniversary Update, Build 14393 or later).

- I am running Windows 10 (Home or anything else) and I get the following error (or similar error about HyperV):
```
HyperV is not available on Home editions. Please use Docker Toolbox
```
As a matter of fact [proof](https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows), Windows 10 *non PRO* OSes don't have HyperV capability. Since Docker cannot run directly on Windows Machine, you need a layer of virtualization to support the container functionality.
Download [https://docs.docker.com/v17.09/toolbox/toolbox_install_windows/](Docker ToolBox) and install it.

- Still having Docker installation issues on Windows?
Try installing one of the versions mentioned on this page:
https://docs.docker.com/docker-for-windows/release-notes/

- Still no dice?
Make sure HyperV is enabled on your machine. Check [https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v](How-TO)

- Still nothing?
Switch to Linux already. SMH
(sorry, I'm all out of options right now. Try Google or come meet me after class and I can point you to last years document on running PUI in a VM on your local machine.)
