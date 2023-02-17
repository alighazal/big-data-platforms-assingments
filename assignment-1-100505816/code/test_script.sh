cassandra-stress write n=10000 -node 192.168.56.101 -rate threads=1 -log file=write_10000n_1t.log
cassandra-stress write n=10000 -node 192.168.56.101 -rate threads=10 -log file=write_10000n_10t.log
cassandra-stress write n=10000 -node 192.168.56.101 -rate threads=50 -log file=write_10000n_50t.log
cassandra-stress write n=10000 -node 192.168.56.101 -rate threads=100 -log file=write_10000n_100t.log
cassandra-stress write n=10000 -node 192.168.56.101 -rate threads=1000 -log file=write_10000n_1000t.log


cassandra-stress read n=10000 -node 192.168.56.101 -rate threads=1 -log file=read_10000n_1t.log
cassandra-stress read n=10000 -node 192.168.56.101 -rate threads=10 -log file=read_10000n_10t.log
cassandra-stress read n=10000 -node 192.168.56.101 -rate threads=50 -log file=read_10000n_50t.log
cassandra-stress read n=10000 -node 192.168.56.101 -rate threads=100 -log file=read_10000n_100t.log
cassandra-stress read n=10000 -node 192.168.56.101 -rate threads=1000 -log file=read_10000n_1000t.log
