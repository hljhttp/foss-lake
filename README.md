# foss-lake
Lake Incubating

- Status - In Development
- Type - Cloud Native Data Lake & BI 

# What?
It's based on following foss tools:
- PostgreSQL (data warehouse) for analytics OLAP data storage.
- Dremio (data lake) for query accelerator, data source management, virtual data sources, powerful joins etc.
- Apache Superset (BI Tool) for easy data access for business people.

# How?
#### Prerequisite
- kubernetes cluster
- kubectl
- helm

#### Deploy
```bash
$ git clone https://github.com/kunaldawn/foss-lake.git
$ cd foss-lake
$ helm install redis redis
$ helm install postgresql postgresql
$ helm install dremio dremio
$ helm install superset superset
$ helm list
```

#### Access Lake & BI
1. Dremio
Access dremio dashboard from http://localhost:9047.

2. Superset
Access superset dashboard from http://localhost:8088.

#### Access DB to load data
###### Console
```bash
$ kubectl port-forward --namespace default svc/postgresql 5432:5432 &
$ PGPASSWORD=admin123 psql --host 127.0.0.1 -U postgres -d postgres -p 5432
```

## Customization
#### Changing Workers

1. Inroder to change workers for superset you have to edit values.yaml in that workers will be there please specify the value according to your need.

#### Ram and CPU usage.

1. Fractional values are allowed. A Container that requests 0.5 CPU is guaranteed half as much CPU as a Container that requests 1 CPU. You can use the suffix m to mean milli. For example 100m CPU, 100 milliCPU, and 0.1 CPU are all the same. Precision finer than 1m is not allowed. CPU is always requested as an absolute quantity, never as a relative quantity; 0.1 is the same amount of CPU on a single-core, dual-core, or 48-core machine.
2. The memory resource is measured in bytes. You can express memory as a plain integer or a fixed-point integer with one of these suffixes: E, P, T, G, M, K, Ei, Pi, Ti, Gi, Mi, Ki.
3. The CPU and Memory value can be edited in values.yaml file of each(redis/dremio/postgresql/superset)

#### Replication/Slave 

1. PostgreSQL -> Replication is enabled by default in the scripts if it is not needed you can disable in values.yaml (replication.enabled)
2. Redis -> Redis has slaves enabled by default in the scripts if it is not needed you can disable in values.yaml (cluster.slaveCount)
