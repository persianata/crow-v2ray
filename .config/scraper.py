import os
import requests

# خواندن اطلاعات از متغیرهای محیطی گیت‌هاب
BALE_TOKEN = os.getenv("BALE_TOKEN")
BALE_CHAT_ID = os.getenv("CHAT_ID")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# لیست کامل منابع و مخزن‌ها
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

def fetch_and_save(output_file="all_configs.txt"):
    all_configs = []
    for url in SOURCES:
        try:
            print(f"Fetching: {url}")
            res = requests.get(url, timeout=15)
            if res.status_code == 200:
                all_configs.append(res.text)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    if all_configs:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(all_configs))

def send_to_bale(file_path, caption):
    if not BALE_TOKEN or not BALE_CHAT_ID:
        print("Bale credentials missing.")
        return
    url = f"https://tapi.bale.ai/bot{BALE_TOKEN}/sendDocument"
    try:
        with open(file_path, "rb") as f:
            res = requests.post(
                url,
                data={"chat_id": BALE_CHAT_ID, "caption": caption},
                files={"document": f},
                timeout=60,
            )
            print(f"Bale: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"Bale error: {e}")

def send_to_telegram(file_path, caption):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials missing.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
    try:
        with open(file_path, "rb") as f:
            res = requests.post(
                url,
                data={"chat_id": TELEGRAM_CHAT_ID, "caption": caption},
                files={"document": f},
                timeout=60,
            )
            print(f"Telegram: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"Telegram error: {e}")

def main():
    file_path = "all_configs.txt"
    fetch_and_save(file_path)
    
    caption = "🚀 Latest V2Ray Configs\n📌 Update: Automated Crow-V2Ray"

    if os.path.exists(file_path):
        print(f"File {file_path} ready. Sending...")
        send_to_bale(file_path, caption)
        send_to_telegram(file_path, caption)
    else:
        print("Config file not found!")

if __name__ == "__main__":
    main()
