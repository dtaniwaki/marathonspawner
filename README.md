# MarathonSpawner


The JupyterHub spawner which utilizes Mesos containerizer in Marathon so that you can run GPU tasks.

The original idea of MarathonSpawner is taken from https://github.com/vigsterkr/marathonspawner which uses Docker containerizer in Marathon.

## Run JupyterHub with MarathonSpawner

Launch JupyterHub and the dependencies with MarathonSpawner in Docker.

```sh
docker-compose up
```
