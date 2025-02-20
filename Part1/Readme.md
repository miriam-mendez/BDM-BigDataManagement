# Instructions to execute the code

1. Install the requirements:
```
pip install -r requirements.txt
```

2. Connect your computer to the UPC link
3. Run virtech - the virtual machine they provided us
4. Execute the following commands in the virtual machine console:
```
/home/bdm/BDM_Software/hadoop/sbin/start-dfs.sh
BDM_Software/hbase/bin/start-hbase.sh
BDM_Software/hbase/bin/hbase-daemon.sh start thrift
```
5. Run in your computer the landing temporal zone
```
python3 temporal_zone.py
```
6. Run in your computer the landing persistent zone. There are two ways to execute it:
    
   1. Execute one by one the persistence loaders:

    ```
    python3 persistent_foreigners.py
    python3 persistent_idealista.py
    python3 persistent_income.py
    python3 persistent_lookup.py
    ```
   2. Execute all at once:
    ```
    python3 persistent_zone.py
    ```