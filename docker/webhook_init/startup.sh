#!/bin/bash
# @Author: longfengpili
# @Date:   2024-10-18 17:00:41
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-22 14:08:03

# 检查是否传入参数
if [ "$1" == "init" ]; then
  # 传入参数为 "init" 时，执行文件复制操作并退出
  cp -r /webhook_init/config /webhook
  cp -r /webhook_init/scripts /webhook
  cp -r /webhook_init/examples /webhook
  # 退出脚本，不执行 webhook 应用
  exit 0
else
  # 如果未传入 "init" 参数，则判断本地目录是否为空
  if [ -z "$(ls -A /webhook)" ]; then
    # 如果本地目录为空，则从容器复制文件到本地目录
    cp -r /webhook_init/config /webhook
    cp -r /webhook_init/scripts /webhook
    cp -r /webhook_init/examples /webhook
  fi
fi

# 在所有其他情况下，执行 webhook 应用
exec /usr/local/bin/webhook "$@"
