import requests
import os

SOURCES = [
    "https://raw.githubusercontent.com/3nerg0n/vless-parser/refs/heads/main/sub_vless_3nerg0n_92sh81",
    "https://raw.githubusercontent.com/iboxz/free-v2ray-collector/main/main/mix.txt",
    "https://raw.githubusercontent.com/zxcursedzxc0721/vless-subscriptions/refs/heads/main/all/vless.txt",
    "https://raw.githubusercontent.com/MohammadBahemmat/V2ray-Collector/refs/heads/main/all_servers.txt",
    "https://raw.githubusercontent.com/Surfboardv2ray/Proxy-sorter/refs/heads/main/output/converted.txt",
    "https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/main/mix.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/main/v2ray.txt",
    "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/all/configs.txt",
    "https://raw.githubusercontent.com/MrRabbitson/RabbitProxyz-proxy-list/main/proxy-list.txt",
    "https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/main/config.txt",
    "https://raw.githubusercontent.com/iboxz/free-v2ray-collector/main/main/mix.txt",
    "https://raw.githubusercontent.com/MohammadBahemmat/V2Ray-Collector/main/sub/sub.txt",
    "https://raw.githubusercontent.com/mohamadfg-dev/telegram-v2ray-configs-collector/main/v2ray.txt",
    "https://raw.githubusercontent.com/R3ZARAHIMI/tg-v2ray-configs-every2h/main/v2ray.txt",
    "https://raw.githubusercontent.com/yebekhe/V2RayConfig/main/v2ray.txt",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/E5%2Fsub.txt",
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/aliilapro/v2rayNG-Config/main/server.txt",
    "https://raw.githubusercontent.com/Anankke/Sub-Store/master/config/node.txt",
    "https://raw.githubusercontent.com/tbbatbb/V2Ray/master/v2ray.txt"
]

def get_all_configs():
    all_lines = []
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                all_lines.extend(response.text.splitlines())
        except:
            continue
    return list(set([line for line in all_lines if line.strip()]))

if __name__ == "__main__":
    configs = get_all_configs()
    
    # حذف فایل‌های قدیمی برای تازه‌سازی کامل
    if os.path.exists("all_servers.txt"):
        os.remove("all_servers.txt")
    for i in range(20):
        if os.path.exists(f"sub{i+1}.txt"):
            os.remove(f"sub{i+1}.txt")
    
    # نوشتن فایل‌های جدید
    with open("all_servers.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
        
    for i in range(20):
        batch = configs[i*500 : (i+1)*500]
        if not batch: break
        with open(f"sub{i+1}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(batch))
