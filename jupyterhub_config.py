import os

c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.hub_port = int(os.environ.get('JUPYTERHUB_API_PORT', 8080))
c.JupyterHub.hub_connect_ip = os.environ['JUPYTERHUB_API_IP']

c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

c.JupyterHub.spawner_class = 'marathonspawner.MarathonSpawner'

c.Spawner.start_timeout = 3600

c.MarathonSpawner.app_image = os.environ['NOTEBOOK_IMAGE']
c.MarathonSpawner.app_prefix = 'jupyter'
c.MarathonSpawner.marathon_host = os.environ.get('MARATHON_HOST', None)
c.MarathonSpawner.cpu = 1
c.MarathonSpawner.max_cpu = 4
c.MarathonSpawner.mem = 256
c.MarathonSpawner.max_mem = 1024
c.MarathonSpawner.disk = 1000
c.MarathonSpawner.max_disk = 5000
c.MarathonSpawner.gpu = 0
c.MarathonSpawner.max_gpu = 0
c.MarathonSpawner.container_type = 'MESOS'
c.MarathonSpawner.env_keep = []
c.MarathonSpawner.autotimeout = 1800
c.MarathonSpawner.mesos_user = os.environ['MESOS_USER']
c.MarathonSpawner.debug = True
