from oauthenticator.google import GoogleOAuthenticator
c.JupyterHub.authenticator_class = GoogleOAuthenticator

c.GoogleOAuthenticator.hosted_domain = 'sightmachine.com'
c.GoogleOAuthenticator.login_service = 'Sightmachine'
if os.environ.get('RESIN_DEVICE_UUID'): 
    c.GoogleOAuthenticator.oauth_callback_url = 'https://' + os.environ['RESIN_DEVICE_UUID'] + '/hub/oauth_callback'
else:
    print('\n'* 20 + 'GOOGLE OAuth cannot be properly enable' + '\n'* 20)


c.Spawner.default_url = '/lab'  # sets to launch jupyterlab instead of notebooks
