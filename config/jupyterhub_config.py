from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'


c.GitHubOAuthenticator.oauth_callback_url = 'http://18.218.25.149:8000/hub/oauth_callback'
c.GitHubOAuthenticator.client_id = '8b7eb03ba01537601572'
c.GitHubOAuthenticator.client_secret = '93bd4db5a30efd8895ff77799166d361e3db391b'

c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'
c.SudoSpawner.sudospawner_path = '/opt/conda/bin'

notebook_dir = '/home/notebooks/'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { '/home/jupyterhub_volumes/': notebook_dir }
"""
c.JupyterHub.ip = '172.31.34.31'
c.JupyterHub.port = 8000

c.ConfigurableHTTPProxy.api_url = 'http://18.218.25.149:5432'
c.JupyterHub.proxy_api_ip = '18.218.25.149'
c.JupyterHub.proxy_api_port = 5432
"""
c.JupyterHub.hub_ip = '18.218.25.149'
#c.JupyterHub.hub_port = 9000
c.Authenticator.create_system_users = True
c.Authenticator.whitelist = {'willyborja95'}
c.Authenticator.admin_users = {'willyborja95'}
#c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

#c.Spawner.cmd = ['/home/ec2-user/jupyterhub/bin/jupyterhub-singleuser']
#c.SudoSpawner.sudospawner_path = '/home/ec2-user/jupyterhub/lib/python3.7/site-packages/jupyterhub/spawner.py'

