import requests
import base64

SOURCES = [
    "https://raw.githubusercontent.com/iboxz/free-v2ray-collector/main/main/mix.txt",
    "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/refs/heads/main/all/configs.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs_no1.txt",
    "https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/vmess_configs.txt"
]

def fetch_configs():
    all_lines = []
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                all_lines.extend(response.text.splitlines())
        except Exception:
            continue
    return list(set([line for line in all_lines if line.strip()]))

if __name__ == "__main__":
    configs = fetch_configs()
    
    # تقسیم به دو فایل برای جلوگیری از سنگین شدن
    mid = len(configs) // 2
    sub1 = configs[:mid]
    sub2 = configs[mid:]
    
    def write_sub(filename, data):
        encoded = base64.b64encode("\n".join(data).encode('utf-8')).decode('utf-8')
        with open(filename, "w") as f:
            f.write(encoded)
            
    write_sub("sub1.txt", sub1)
    write_sub("sub2.txt", sub2)
