import json

# 从文件中读取 JSON 数据
with open('alpaca_data.json', 'r') as file:
    data = json.load(file)

# 'data' 现在包含了从 JSON 文件中读取的数据，它通常是一个字典或列表
for d in data:
  d['output'] = len(d['output'])

# 将数据写入 JSON 文件
with open('alpaca_data_len.json', 'w') as file:
    json.dump(data, file, indent=4) 