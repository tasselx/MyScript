import hashlib
import shutil
import sys
from pathlib import Path
import os

def generate_copies(img_path: str, num_copies: int):
    img_path = Path(img_path)
    suffix = img_path.suffix
    copy_dir = Path('copy')
    copy_dir.mkdir(exist_ok=True)
    
    for i in range(num_copies):
        # 构造副本文件名
        new_path = copy_dir / f'{i}{suffix}'
        
        # 复制图片到副本目录
        shutil.copy(img_path, new_path)
        # 修改复制后文件的md5值
        # 读取文件内容
        with new_path.open('rb') as f:
            content = f.read()
            # 修改文件内容，添加一些随机数据
            new_content = content + os.urandom(4) 
            # 计算修改后的内容的MD5哈希值
            new_md5 = hashlib.md5(new_content).hexdigest()
            print(f'修改后{new_path}的MD5哈希值为{new_md5}')
            # 将修改后的内容写回文件
            new_path.write_bytes(new_content)
    print('Done!')

if __name__ == '__main__':
    img_path = sys.argv[1]
    num_copies = 10
    generate_copies(img_path, num_copies)