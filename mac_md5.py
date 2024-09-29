import hashlib
import psutil
import re
import random

class MacAddressHandler:
    @staticmethod
    def get_mac_md5():
        # 原始的获取 MAC 地址并计算 MD5 的方法
        mac_addresses = []
        for interface, addrs in psutil.net_if_addrs().items():
            if interface.startswith(('en', 'Ethernet', '以太网', 'WLAN')):
                if interface.startswith('en'):
                    match = re.match(r'en(\d+)', interface)
                    if match and int(match.group(1)) > 6:
                        continue
                
                for addr in addrs:
                    if addr.family == psutil.AF_LINK:
                        mac_addresses.append(addr.address)
        
        mac_addresses.sort()
        mac_string = ','.join(mac_addresses)
        return hashlib.md5(mac_string.encode()).hexdigest()

    @staticmethod
    def mock_mac_md5(seed=None):
        # 模拟 MAC 地址 MD5 的方法
        if seed is not None:
            random.seed(seed)
        
        # 生成一个随机的 32 字符的十六进制字符串
        mock_hash = ''.join(random.choices('0123456789abcdef', k=32))
        return mock_hash

    @staticmethod
    def get_or_mock_mac_md5(use_mock=False, mock_seed=None):
        # 根据参数决定使用真实数据还是模拟数据
        if use_mock:
            return MacAddressHandler.mock_mac_md5(mock_seed)
        else:
            return MacAddressHandler.get_mac_md5()

# 使用示例
handler = MacAddressHandler()

# 获取真实的 MAC MD5
print("Real MAC MD5:", handler.get_mac_md5())

# 获取模拟的 MAC MD5
print("Mocked MAC MD5:", handler.mock_mac_md5())

# 使用种子以获得可重复的模拟结果
print("Seeded Mocked MAC MD5:", handler.mock_mac_md5(seed=42))

# 使用组合方法，可以轻松切换between真实和模拟数据
print("Real data:", handler.get_or_mock_mac_md5(use_mock=False))
print("Mocked data:", handler.get_or_mock_mac_md5(use_mock=True))
print("Seeded mocked data:", handler.get_or_mock_mac_md5(use_mock=True, mock_seed=42))