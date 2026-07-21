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

def fetch_and_split_configs():
    all_lines = []
    
    # دریافت داده‌ها از تمام منابع
    for url in SOURCES:
        try:
            print(f"Fetching: {url}")
            res = requests.get(url, timeout=15)
            if res.status_code == 200:
                lines = res.text.splitlines()
                for line in lines:
                    if line.strip():
                        all_lines.append(line.strip())
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    if not all_lines:
        print("No configs fetched!")
        return

    # ذخیره کل کانفیگ‌ها در all_configs.txt
    with open("all_configs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(all_lines))

    # تقسیم لیست کانفیگ‌ها به ۳ قسمت مساوی برای sub1, sub2, sub3
    chunk_size = len(all_lines) // 3
    remainder = len(all_lines) % 3

    sub1_end = chunk_size + (1 if remainder > 0 else 0)
    sub2_end = sub1_end + chunk_size + (1 if remainder > 1 else 0)

    part1 = all_lines[:sub1_end]
    part2 = all_lines[sub1_end:sub2_end]
    part3 = all_lines[sub2_end:]

    with open("sub1.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(part1))
    
    with open("sub2.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(part2))

    with open("sub3.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(part3))

    print("Configs successfully fetched and split.")

def send_to_bale(file_path, caption):
    if not BALE_TOKEN or not BALE_CHAT_ID:
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
            print(f"Bale ({file_path}): {res.status_code}")
    except Exception as e:
        print(f"Bale error: {e}")

def send_to_telegram(file_path, caption):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
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
            print(f"Telegram ({file_path}): {res.status_code}")
    except Exception as e:
        print(f"Telegram error: {e}")

def main():
    fetch_and_split_configs()
    
    caption_base = "🚀 Latest V2Ray Configs\n📌 Update: Automated Crow-V2Ray"
    
    # لیست فایل‌هایی که باید ارسال شوند
    files_to_send = [
        ("all_configs.txt", f"{caption_base}\n📁 All Configs"),
        ("sub1.txt", f"{caption_base}\n📁 Subscription Part 1"),
        ("sub2.txt", f"{caption_base}\n📁 Subscription Part 2"),
        ("sub3.txt", f"{caption_base}\n📁 Subscription Part 3")
    ]
    
    # ارسال فایل‌ها به بله و تلگرام
    for file_path, caption in files_to_send:
        if os.path.exists(file_path):
            print(f"Sending {file_path} to platforms...")
            send_to_bale(file_path, caption)
            send_to_telegram(file_path, caption)

if __name__ == "__main__":
    main()
