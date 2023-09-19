import hashlib
import os
import sys

# 定义一个集合，用于过滤指定的文件后缀名
exclude_extensions = ['mp3', 'png', 'jpg', 'mp4','flac']

def get_md5(file_path):
    """获取文件的MD5哈希值"""
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash_value = md5obj.hexdigest()
    return hash_value

def modify_md5(file_path):
    """修改文件的MD5哈希值"""
    # 排除指定的文件扩展名
    
    ext_name = file_path.split('.')[-1]

    if ext_name not in exclude_extensions:
        print('不是指定的文件类型:'+ext_name)
        return
    
    original_md5 = get_md5(file_path)
    print(f'原文件{file_path}的MD5哈希值为{original_md5}')
    
    # 读取文件内容
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # 修改文件内容，添加一些随机数据
    new_content = content + os.urandom(4)  
    
    # 计算修改后的内容的MD5哈希值
    new_md5 = hashlib.md5(new_content).hexdigest()
    print(f'修改后{file_path}的MD5哈希值为{new_md5}')
    
    # 将修改后的内容写回文件
    with open(file_path, 'wb') as f:
        f.write(new_content)

def modify_all_md5(dir_path):
    """修改目录下所有文件的MD5哈希值"""
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            modify_md5(file_path)
            
if __name__ == '__main__':
    # 从命令行获取路径参数
    path = sys.argv[1]
    
    # 检查路径是文件还是目录，并调用相应的函数
    if os.path.isfile(path):
        modify_md5(path)
    else:
        modify_all_md5(path)