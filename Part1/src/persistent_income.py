import os
import happybase
from hdfs import InsecureClient

DATABASE = 'databases'

def income(database = DATABASE):
    hdfs_client = InsecureClient('http://10.4.41.35:9870/', user='bdm')
    
    # Connect to HBase
    connection = happybase.Connection(host='charmander.fib.upc.es', port=9090)

    # Check if table exists and create if not
    if not connection.tables().__contains__(database.encode()):
        connection.create_table(database, {'cf1': dict()})

    table = connection.table(database)
    lookup_tables_dir = "temporal_zone/opendatabcn-income"
    for file_path in hdfs_client.list(lookup_tables_dir):
        with hdfs_client.read(os.path.join(lookup_tables_dir, file_path).replace("\\", "/")) as file:
            file_contents = file.read()
        row_key = os.path.basename(file_path)
        print(row_key)
        #if table.row(row_key) is None:
        data = {'cf1:content': file_contents}
        table.put(row_key, data)

    connection.close()
    
if __name__ == "__main__":
  income()