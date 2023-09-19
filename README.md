# MyScript
一些自用脚本

### 修改文件md5,用户洗码

`python3 modify_md5.py $path`
### 生成重复图片,且每个md5都不一样

`python3 generate_image.py $path`

### 解密finalShell中保存的密码

```
Mac端保存路径在 `~/Library/FinalShell/conn` 目录下的json文件中的password字段
可以使用decode_finalshell.java脚本解密,也可以在线运行
```

### 生成app图标
```
python3 app_icon.py $path
```

### 扫描是否包含某些字符


```
sh check.sh $path
```