from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator

c.GitHubOAuthenticator.oauth_callback_url = 'http://18.219.229.48:8000/hub/oauth_callback'
c.GitHubOAuthenticator.client_id = '8b7eb03ba01537601572'
c.GitHubOAuthenticator.client_secret = '93bd4db5a30efd8895ff77799166d361e3db391b'

#c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

#c.Spawner.cmd = ['/home/ec2-user/jupyterhub/bin/jupyterhub-singleuser']
#c.SudoSpawner.sudospawner_path = '/home/ec2-user/jupyterhub/lib/python3.7/site-packages/jupyterhub/spawner.py'

