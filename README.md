# JupyterHub for Resin.io

## JupyterHub

In case you don't know what JupyterHub is, it's a way to run multiple instances
of Jupyter Notebooks or JupyterLab. In this case we are hosting JupyterHub on a
a resin.io device so that multiple people can easily access the environment the
resin.io device is in.

More information on JupyterHub: https://github.com/jupyterhub/jupyterhub


## Things to be aware of

1. You are dropped into the root of the directory tree by default, however
please store all files relevant to you in `/data/home/<username>` other wise
bad things will happen.
2. Users are managed by the linux system and as such you may find yourself unable
to view or edit files or directories. To over come this see step 3.
3. Your user is added to the group "sudo" meaning that you have the ability to
use sudo, and it is enabled with no need for a password. If you break something
see step 4.
4. All changes made to any file outside of `/data/` will be blown away on if the
container is restarted or redeployed. This includes python libraries.
5. To preserve python libraries setup a virtualenv and activate it for jupyter
use. [Instructions forthcoming](#oauth)

## How to Deploy

Instructions belowe assume you are deploying onto a mutli-container device
and that you'll be deploying this with a docker-compose file.

1. Add an entry to the docker-compose.yml file for
hunterjackson/resin_jupyterhub under services, it should look similar to the
following.

  ```  
  services:
    jupyter:
      privileged: true  # needed as per https://docs.resin.io/learn/develop/multicontainer/#resin-io-settings
      restart: always
      network_mode: host
      container_name: jupyterlab
      image: hunterjackson/resin_jupyterhub
      expose:
        - '80'
      volumes:
        - 'resin-data:/data'

  ```
2. Deploy to desired device
https://docs.resin.io/learn/deploy/deployment/#how-to-deploy

3. Go to the resin logs for the relevant container. There should be a block of
code being repeated that looks similar to this.

  ```
  07.05.18 11:25:40 (-0700)  jupyter        Environment Variables OAUTH_CLIENT_ID & OAUTH_CLIENT_SECRET need to be set
  07.05.18 11:25:40 (-0700)  jupyter        If not already done create an OAuth credential for this device using
  07.05.18 11:25:40 (-0700)  jupyter        the google console here https://console.developers.google.com
  07.05.18 11:25:40 (-0700)  jupyter
  07.05.18 11:25:40 (-0700)  jupyter        Authorized Javascript origins ->  https://edd8ad947e560c5e97f157165e3f5f56.resindevice.io
  07.05.18 11:25:40 (-0700)  jupyter        Authorized redirect URIs -> https://edd8ad947e560c5e97f157165e3f5f56.resindevice.io/hub/oauth_callback
  07.05.18 11:25:40 (-0700)  jupyter
  07.05.18 11:25:40 (-0700)  jupyter        Then from the information generated after creating the OAuth credential set
  07.05.18 11:25:40 (-0700)  jupyter        the environment variables in the resin dashboard for the device accordingly
  07.05.18 11:25:40 (-0700)  jupyter
  07.05.18 11:25:40 (-0700)  jupyter        OAUTH_CLIENT_ID <- Client ID
  07.05.18 11:25:40 (-0700)  jupyter        OAUTH_CLIENT_SECRET <- Client secret
  ```

4. Use the information found in the logs to setup a Google OAuth credential,
instructions can be found [here](#oauth).

5. Use the client id and client secret to set the environtment variables,
OAUTH_CLIENT_ID and OAUTH_CLIENT_SECRET. If unsure of how to setup environment
variables for a resin device https://docs.resin.io/learn/manage/serv-vars/#device-environment-and-service-variables

6. At this you should see the logs stop repeating the help message. If not
already done enable your devices public url and navigate there.

## How to setup Google OAuth <a name="oauth">#</a>

1. #TODO

## Setting up virtualenv for personal jupyter use <a name="venv">#</a>

1. #TODO
