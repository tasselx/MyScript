#!/bin/bash
#脚本放在项目外面 cd的目录是要扫描的目录
cd /Users/tassel/Documents/Project/meyo
filter () {
	#排除的目录
	grep -r $1 . --color=auto --exclude-dir={.git,.dart_tool,./build,.sciprt,web,./ios/.symlinks,./ios/Pods}  --binary-files=without-match
}
#有需要新加的扫码字段,在后面扩展
# config=(bet lottery income jackpot price free dice game videoPrice voicePrice)
config=(meyo)
for i in ${config[@]}
do
	filter $i
done

