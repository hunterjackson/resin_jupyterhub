import os
from oauthenticator.google import LocalGoogleOAuthenticator

if os.environ.get('RESIN_DEVICE_UUID'): 
    auth_uri = 'https://' + os.environ['RESIN_DEVICE_UUID'] + '.resindevice.io'
    callback_uri = auth_uri + '/hub/oauth_callback'

    if not (os.environ.get('OAUTH_CLIENT_ID') and os.environ.get('OAUTH_CLIENT_SECRET')): 
        print('\n' * 3 + '''
      Environment Variables OAUTH_CLIENT_ID & OAUTH_CLIENT_SECRET need to be set
      If not already done create an OAuth credential for this device using
      the google console here https://console.developers.google.com
      
      Authorized Javascript origins ->  {}
      Authorized redirect URIs -> {}
      
      Then from the information generated after creating the OAuth credential set
      the environment variables in the resin dashboard for the device accordingly

      OAUTH_CLIENT_ID <- Client ID
      OAUTH_CLIENT_SECRET <- Client secret

      for more information please see the readme 
      https://github.com/hunterjackson/resin_jupyterhub/blob/master/README.md\n'''.format(auth_uri, callback_uri) + '\n' * 3)
                
        exit(1)

    c.JupyterHub.authenticator_class = LocalGoogleOAuthenticator
    
    c.LocalGoogleOAuthenticator.hosted_domain = 'sightmachine.com'
    c.LocalGoogleOAuthenticator.login_service = 'Sight Machine'
    
    c.LocalGoogleOAuthenticator.add_user_cmd = ['adduser', '--system', '-q', '--gecos', '""', '--disabled-password', '--ingroup', 'sudo']
    c.LocalGoogleOAuthenticator.create_system_users = True
    c.LocalGoogleOAuthenticator.oauth_callback_url = callback_uri
else:
    print('#' * 25 +  '\n'* 5 + '''This container instance of jupyterhub is only for resin devices!''' + '\n'* 5 + '#' * 25)
    exit(1)

c.LocalGoogleOAuthenticator.auto_login = True
c.Spawner.default_url = '/lab'  # sets to launch jupyterlab instead of notebooks
c.Spawner.notebook_dir = '/'
# c.LocalProcessSpawner.default_url = '/data/notebooks'

from os import mkdir 
def setup_user_dirs(spawner):
    username = spawner.user.name
    try:
        os.mkdir('/data/home/' + username)
    except FileExistsError:
        pass

    for root, dirs, files in os.walk('/data/home'):  
        for momo in dirs:  
            os.chmod(os.path.join(root, momo), 0o777)
        for momo in files:
            os.chmod(os.path.join(root, momo), 0o777)

c.Spawner.pre_spawn_hook = setup_user_dirs 
