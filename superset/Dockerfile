FROM python:3.6-jessie

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

RUN useradd --user-group --create-home --no-log-init --shell /bin/bash superset \
    && mkdir -p /home/superset/src \
    && mkdir -p /home/superset/db \
    && chown superset /home/superset

COPY superset_init superset_run /bin/
COPY superset_config.py /home/superset/config/superset_config.py

RUN chmod +x /bin/superset_init \
    && chmod +x /bin/superset_run \
    && apt-get update -y \
    && apt-get install -y apt-transport-https apt-utils curl \
    && apt-get install -y build-essential libssl-dev libffi-dev python3-dev libsasl2-dev libldap2-dev libxi-dev \
    && apt-get install -y libpython3-dev unixodbc-dev python-pyodbc alien \
    && curl -O https://download.dremio.com/odbc-driver/1.4.2.1003/dremio-odbc-1.4.2.1003-1.x86_64.rpm \
    && alien --scripts --to-deb dremio-odbc-1.4.2.1003-1.x86_64.rpm \
    && dpkg -i dremio-odbc_1.4.2.1003-2_amd64.deb \
    && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN wget -O /tmp/incubator-superset-master.zip https://github.com/kunaldawn/incubator-superset/archive/master.zip \
    && unzip incubator-superset-master.zip \
    && rm incubator-superset-master.zip \
    && mv /tmp/incubator-superset-master/* /home/superset/src/

WORKDIR /home/superset/src/superset-frontend
RUN npm ci \
    && npm run build \
    && rm -rf node_modules

WORKDIR /home/superset/src
RUN pip install --upgrade setuptools pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir -r requirements-dev.txt \
    && pip install --no-cache-dir sqlalchemy_dremio \
    && pip install --no-cache-dir . \
    && flask fab babel-compile --target superset/translations \ 
    && rm -rf /tmp/*

WORKDIR /home/superset
COPY dremio.py /home/superset/src/superset/db_engine_specs/
RUN chown -R superset:superset /home/superset

ENV GUNICORN_BIND=0.0.0.0:8088 \
    GUNICORN_LIMIT_REQUEST_FIELD_SIZE=0 \
    GUNICORN_LIMIT_REQUEST_LINE=0 \
    GUNICORN_TIMEOUT=60 \
    GUNICORN_WORKERS=3 \
    GUNICORN_THREADS=4 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONPATH=/home/superset/src:/home/superset/config:$PYTHONPATH \
    FLASK_ENV=production \
    FLASK_APP="superset.app:create_app()"

ENV GUNICORN_CMD_ARGS="--workers ${GUNICORN_WORKERS} --threads ${GUNICORN_THREADS} --timeout ${GUNICORN_TIMEOUT} --bind ${GUNICORN_BIND} --limit-request-line ${GUNICORN_LIMIT_REQUEST_LINE} --limit-request-field_size ${GUNICORN_LIMIT_REQUEST_FIELD_SIZE}"

EXPOSE 8088
HEALTHCHECK CMD ["curl", "-f", "http://localhost:8088/health"]
CMD ["gunicorn", "superset.app:create_app()"]
USER superset
