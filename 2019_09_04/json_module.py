import json

# 反序列化
json_str = '{"name": "python_json"}'
result = json.loads(json_str)   # 把json串转换成python的dict类型
print(type(result)) # dict
print(result['name'])


# 序列化 对象转换成json串
json_array = [
    { 'name': 'python_name'}
]

json_str = json.dumps(json_array)
print(json_str)