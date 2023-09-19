#!/bin/bash
# 脚本放在项目外面，扫描的目录是从终端传入的参数

# 检查是否传入路径参数
if [ -z "$1" ]; then
  echo "请传入要扫描的目录路径"
  exit 1
fi

# 设置扫描的目录路径
scan_dir=$1

filter () {
  # 排除的目录
  grep -r $1 $scan_dir --color=auto --exclude-dir={.git,.dart_tool,./build,.script,web,./ios/.symlinks,./ios/Pods}  --binary-files=without-match
}

# 有需要新加的扫描字段，在后面扩展
config=(bet lottery income jackpot price free dice game videoPrice voicePrice)

for i in ${config[@]}
do
  filter $i
done
