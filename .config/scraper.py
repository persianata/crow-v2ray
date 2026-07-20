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
    "https://raw.githubusercontent.com/MohammadBahemmat/V2Ray-Collector/main/sub/sub.txt",
    "https://raw.githubusercontent.com/mohamadfg-dev/telegram-v2ray-configs-collector/main/v2ray.txt",
    "https://raw.githubusercontent.com/R3ZARAHIMI/tg-v2ray-configs-every2h/main/v2ray.txt",
    "https://raw.githubusercontent.com/yebekhe/V2RayConfig/main/v2ray.txt",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/E5%2Fsub.txt",
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/aliilapro/v2rayNG-Config/main/server.txt",
    "https://raw.githubusercontent.com/Anankke/Sub-Store/master/config/node.txt",
    "https://raw.githubusercontent.com/tbbatbb/V2Ray/master/v2ray.txt",
    "https://raw.githubusercontent.com/VP01596/vless-top15/main/vless.txt",
    "https://raw.githubusercontent.com/lm705/vair/main/vair.txt",
    "https://raw.githubusercontent.com/Alirewa/V2ray-Configs/main/v2ray.txt",
    "https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/main/v2ray.txt",
    "https://raw.githubusercontent.com/barry-far/v2ray-config/main/v2ray.txt"
]

def is_valid_config(config):
    # پروتکل‌هایی که در ایران معمولاً پایدارتر هستند
    preferred_protocols = ("vless://", "trojan://", "vmess://")
    
    if not config.startswith(preferred_protocols):
        return False
        
    if len(config) < 20 or len(config) > 1000:
        return False
    return True

def get_all_configs():
    all_lines = set()
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    clean_line = line.strip()
                    if is_valid_config(clean_line):
                        all_lines.add(clean_line)
        except:
            continue
    return list(all_lines)

if __name__ == "__main__":
    configs = get_all_configs()
    
    # محدودیت ۵۰۰۰ کانفیگ برای تعادل بین حجم و تنوع
    configs = configs[:5000] 

    with open("all_servers.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(configs))
        
    BATCH_SIZE = 100
    for i in range(50): 
        batch = configs[i*BATCH_SIZE : (i+1)*BATCH_SIZE]
        if not batch: break
        with open(f"sub{i+1}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(batch))
