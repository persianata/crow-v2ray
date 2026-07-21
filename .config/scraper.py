import os
import requests

# خواندن اطلاعات از متغیرهای محیطی (Secrets) گیت‌هاب
BALE_TOKEN = os.getenv("BALE_TOKEN")
BALE_CHAT_ID = os.getenv("CHAT_ID")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# لیست کامل مخزن‌ها و منابع کانفیگ
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


def fetch_from_sources(output_file="sub"):
    """جمع‌آوری اطلاعات از مخزن‌ها و منابع مختلف و ذخیره در فایل خروجی"""
    all_configs = []
    
    for url in SOURCES:
        try:
            print(f"Fetching from source: {url}")
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                all_configs.append(response.text)
        except Exception as e:
            print(f"Error fetching from {url}: {e}")

    # اگر از منابع چیزی دریافت شد، در فایل خروجی نوشته شود
    if all_configs:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(all_configs))


def send_to_bale(file_path, caption):
    if not BALE_TOKEN or not BALE_CHAT_ID:
        print("Bale credentials not found. Skipping Bale.")
        return

    url = f"https://tapi.bale.ai/bot{BALE_TOKEN}/sendDocument"
    try:
        with open(file_path, "rb") as f:
            response = requests.post(
                url,
                data={"chat_id": BALE_CHAT_ID, "caption": caption},
                files={"document": f},
                timeout=60,
            )
            print(f"Bale response for {file_path}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Bale error: {e}")


def send_to_telegram(file_path, caption):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials not found. Skipping Telegram.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
    try:
        with open(file_path, "rb") as f:
            response = requests.post(
                url,
                data={"chat_id": TELEGRAM_CHAT_ID, "caption": caption},
                files={"document": f},
                timeout=60,
            )
            print(f"Telegram response for {file_path}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Telegram error: {e}")


def main():
    # نام فایل خروجی
    file_path = "sub" 
    
    # ابتدا کانفیگ‌ها از تمام مخزن‌های لیست بالا فچ و در فایل ذخیره می‌شوند
    fetch_from_sources(file_path)

    # بررسی و هندل کردن خطای پیدا نکردن فایل در صورت داشتن پسوند یا نام دیگر
    if not os.path.exists(file_path) and os.path.exists("configs.txt"):
        file_path = "configs.txt"
    elif not os.path.exists(file_path) and os.path.exists("sub.txt"):
        file_path = "sub.txt"

    caption = "🚀 Latest V2Ray Configs\n📌 Update: Automated Crow-V2Ray"

    if os.path.exists(file_path):
        print(f"File '{file_path}' found. Sending configurations to platforms...")
        
        # ارسال به بله
        send_to_bale(file_path, caption)
        
        # ارسال به تلگرام
        send_to_telegram(file_path, caption)
    else:
        print(f"File {file_path} not found!")


if __name__ == "__main__":
    main()
