from hdfs import *
import os

# Connect to HDFS
client = InsecureClient('http://10.4.41.35:9870/', user='bdm')


base_directory = 'temporal_zone'
directories = {'idealista': f'{base_directory}/idealista',
               'opendatabcn-income': f'{base_directory}/opendatabcn-income',
               'lookup_tables': f'{base_directory}/lookup_tables',
               'opendatabcn-foreigners': f'{base_directory}/opendatabcn-foreigners'}

# Create folders for the different data sources
for key,value in directories.items():
    client.makedirs(value)

# Upload all the files in their respective folder
for key, value in directories.items():
    for filename in os.listdir(f'../data/{key}'):
        local_f = os.path.join(f'../data/{key}', filename)
        hdfs_f = os.path.join(f'./{value}', filename)
        x = client.status(hdfs_f, strict=False)
        if x is None:
            client.upload(hdfs_f, local_f)
            

# chaking that all is uploaded well
print(client.list('.'))
print(client.list('temporal_zone'))
print(client.list('temporal_zone/idealista'))
print(client.list('temporal_zone/opendatabcn-income'))
print(client.list('temporal_zone/lookup_tables'))
print(client.list('temporal_zone/opendatabcn-foreigners'))