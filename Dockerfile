FROM jupyterhub/jupyterhub:0.8.1
MAINTAINER dtaniwaki

COPY . /tmp/marathonspawner/
RUN pip install /tmp/marathonspawner
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
RUN pip install jupyterhub-dummyauthenticator==0.3

ENV JUPYTERHUB_API_IP=<placeholder>
ENV JUPYTERHUB_API_PORT=<placeholder>
ENV NOTEBOOK_IMAGE=<placeholder>
ENV MARATHON_HOST=<placeholder>
ENV MESOS_USER=<placeholder>

ARG JUPYTERHUB_UID=1000

RUN adduser --system --no-create-home --uid $JUPYTERHUB_UID jupyterhub
RUN chown -R jupyterhub /srv/jupyterhub
USER jupyterhub
