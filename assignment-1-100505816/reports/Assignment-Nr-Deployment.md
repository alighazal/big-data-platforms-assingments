# Guide for installing the cassandra cluster:

## install cassandra on a single machine 

### getting cassandra packages:

```
echo "deb http://www.apache.org/dist/cassandra/debian 40x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list

wget -q -O - https://www.apache.org/dist/cassandra/KEYS | sudo tee /etc/apt/trusted.gpg.d/cassandra.asc

sudo apt update

sudo apt install cassandra
```

### Monitoring Cassandra:

```
sudo nodetool status

```

## connecting a multi-node cluster

I was mainly following this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-cassandra-and-run-a-multi-node-cluster-on-ubuntu-22-04)


### stop and  cassandra

```

sudo systemctl stop cassandra

sudo rm -rf /var/lib/cassandra/*

```

### adjusting the config

```
    sudo nano /etc/cassandra/cassandra.yaml

```

### modification inside cassandra.yaml

change the following fields on each machine in the cluster

```
...
cluster_name: 'CassandraDOCluster'
...
seed_provider:
  - class_name: org.apache.cassandra.locator.SimpleSeedProvider
    parameters:
         - seeds: "seed-internal-ip-address"
...
listen_address: "targetnode-internal-ip-address"
...
rpc_address: "targetnode-internal-ip-address"
...
endpoint_snitch: GossipingPropertyFileSnitch
...
auto_bootstrap: false

```



