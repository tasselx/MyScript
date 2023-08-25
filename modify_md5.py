import hashlib
import os
import sys

#定义个过滤器数组，过滤指定的后缀名
filter = ['mp3','png','jpg','mp4']
    

def get_md5(file_path):
    """获取文件md5值"""
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
    return hash

def modify_md5(file_path):
    # 过滤指定filter后缀名的文件
    if file_path.split('.')[-1] not in filter:
        return
    """修改文件md5值"""
    original_md5 = get_md5(file_path)
    print(f'原文件{file_path}的md5值为{original_md5}')
    
    # 打开文件读取内容
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # 改变文件内容,添加一些无意义的数据
    new_content = content + os.urandom(4)  
    
    # 计算新内容的md5值
    new_md5 = hashlib.md5(new_content).hexdigest()
    print(f'修改后{file_path}的md5值为{new_md5}')
    
    # 打开文件以二进制写入模式,写入新内容
    with open(file_path, 'wb') as f:
        f.write(new_content)

def modify_all_md5(dir_path):
    """遍历目录修改所有文件md5值"""
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            modify_md5(file_path)
            
if __name__ == '__main__':
    arguments = sys.argv
    path = arguments[1]
    if os.path.isfile(path):
        modify_md5(path)
    else:
        modify_all_md5(path)
