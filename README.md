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