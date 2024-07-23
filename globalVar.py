import os

accountdata = os.getenv('gcp_json','').replace("\\\"", '"').replace("'", "").replace(",",",\n").replace('{', '{\n').replace('}', '\n}')
for root, dirs, files in os.walk(os.getcwd()+'/auth'):
  for file in files:
      if file.endswith('.json'):
          file_path = os.path.join(root, file)
          with open(file_path, 'r') as f:
              accountdata += f.read()