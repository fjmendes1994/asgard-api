
NETWORK_NAME="asgard"
ZK_1_IP=172.18.0.2
ZK_2_IP=172.18.0.3
ZK_3_IP=172.18.0.4
ZK_CLUSTER_IPS=${ZK_1_IP}:2181,${ZK_2_IP}:2181,${ZK_3_IP}:2181

MESOS_MASTER_1_IP=172.18.0.11
MESOS_MASTER_2_IP=172.18.0.12
MESOS_MASTER_3_IP=172.18.0.13
MESOS_SLAVE_IP=172.18.0.21
MESOS_SLAVE_IPS_ACCOUNT_ASGARD_INFRA="172.18.0.51 172.18.0.52 172.18.0.53 172.18.0.54 172.18.0.55"
MESOS_SLAVE_IPS_ACCOUNT_ASGARD_DEV="172.18.0.61 172.18.0.62 172.18.0.63 172.18.0.64 172.18.0.65"
MARATHON_IP=172.18.0.31

POSTGRES_IP=172.18.0.41