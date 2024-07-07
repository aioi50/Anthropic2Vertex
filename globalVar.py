import os

accountdata = os.environ['gcp_json'].replace("\\n", "\n").replace("\\", '').replace("'","")