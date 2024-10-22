# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-21 16:32:09
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-21 18:05:09
# @github: https://github.com/longfengpili


import requests
import json
import base64

# 定义目标 URL（根据实际情况替换）
url = "http://localhost:9000/hooks/redeploy-webhook?token=421&query=qchina"

# 定义静态和动态数据
file_content = "Hello, World!"

# 将文件内容编码为 base64
encoded_file_content = base64.b64encode(file_content.encode()).decode()

# 构建 payload
payload = {
    "args": {
        "json": {
            "path": 'arg-json-path'
        }
    },
    "envs": {
        "json": {
            "path": 'env-json-path'
        }
    },
    "file": {
        "path": encoded_file_content
    }
}

# 设置自定义头部
headers = {
    "Content-Type": "application/json",
    "X-Example-Header": "it works",
    'Token': 'header-token',
}

# 发送 POST 请求
response = requests.post(url, headers=headers, data=json.dumps(payload))

# 打印响应
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
