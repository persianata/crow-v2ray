import requests
import os
import time
import random

# دریافت اطلاعات بله از Secretها
BALE_TOKEN = os.environ.get("BALE_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# دریافت اطلاعات تلگرام از Secretها
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# لیست کامل سورس‌ها
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

def get_all_configs():
    all_configs = set()
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                lines = [line.strip() for line in response.text.splitlines() if line.strip()]
                all_configs.update(lines)
        except:
            continue
    return list(all_configs)

def send_to_bale(file_path, caption):
    if BALE_TOKEN and CHAT_ID:
        url = f"https://tapi.bale.ai/bot{BALE_TOKEN}/sendDocument"
        try:
            with open(file_path, 'rb') as f:
                requests.post(url, data={"chat_id": CHAT_ID, "caption": caption}, files={"document": f}, timeout=60)
        except:
            pass

def send_to_telegram(file_path, caption):
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
        try:
            with open(file_path, 'rb') as f:
                requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "caption": caption}, files={"document": f}, timeout=60)
        except:
            pass

if __name__ == "__main__":
    all_configs = get_all_configs()
    
    with open("all_configs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(all_configs))
        
    random.shuffle(all_configs)
    
    subs = ["sub1.txt", "sub2.txt", "sub3.txt"]
    for sub in subs:
        subset = all_configs[:100]
        all_configs = all_configs[100:]
        
        if subset:
            with open(sub, "w", encoding="utf-8") as f:
                f.write("\n".join(subset))
            
            caption = f"✅ فایل {sub} با {len(subset)} کانفیگ جدید"
            
            # ارسال هم‌زمان به بله و تلگرام
            send_to_bale(sub, caption)
            send_to_telegram(sub, caption)
            
            time.sleep(5)
        else:
            break
