#!/usr/bin/python
# -*- coding: UTF-8 -*-
import boto3
import re

def fetch_emr_ip():
	boto_emr_client = boto3.client("emr")
	cluster_list = boto_emr_client.list_clusters(ClusterStates = ['RUNNING','WAITING'])['Clusters']
	cluster_name = r'Sparkmagic'

	for cluster in cluster_list:
		if re.match(cluster_name, cluster['Name']):
			cluster_id = cluster['Id']
			master_node = boto_emr_client.list_instances(ClusterId=cluster_id,
								     InstanceGroupTypes=['MASTER'],
								     InstanceStates=['RUNNING'])['Instances'][0]
			ip = master_node['PublicDnsName']
			return ip

print(fetch_emr_ip())
