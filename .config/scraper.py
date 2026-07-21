import os
import requests

# خواندن اطلاعات از متغیرهای محیطی (Secrets) گیت‌هاب
BALE_TOKEN = os.getenv("BALE_TOKEN")
BALE_CHAT_ID = os.getenv("CHAT_ID")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# لیست لینک‌ها، مخزن‌ها یا سورس‌های خام کانفیگ (می‌توانید لینک فایل‌های sub.txt دلخواه خود را اینجا اضافه کنید)
SOURCES = [
    # "https://raw.githubusercontent.com/username/repository/main/sub.txt",
]


def fetch_configs(output_file="sub"):
    """جمع‌آوری کانفیگ‌ها از لیست مخزن‌ها و منابع مختلف و ذخیره در فایل خروجی"""
    all_configs = []
    
    for url in SOURCES:
        try:
            print(f"Fetching from source: {url}")
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                all_configs.append(response.text)
        except Exception as e:
            print(f"Error fetching from {url}: {e}")

    # اگر سورس‌ها کانفیگی برگرداندند، آن‌ها را در فایل ذخیره می‌کنیم
    # (اگر اسکریپت شما خودش در بخش دیگری فایل sub را تولید می‌کند، این بخش به فایل موجود اضافه یا بازنویسی می‌کند)
    if all_configs:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(all_configs))
            
    return output_file


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
            response.requests_post = requests.post
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
    # نام فایل خروجی کانفیگ‌ها (می‌توانید به sub یا sub.txt تغییر دهید)
    file_path = "sub"
    
    # اول سورس‌ها و مخزن‌ها را بررسی/فچ می‌کنیم (یا اگر فایل از قبل توسط بخش دیگری ساخته شده باشد بررسی می‌شود)
    fetch_configs(file_path)
    
    # اگر فایل نام دیگری مثل sub.txt داشت و فایل اصلی پیدا نشد، بررسی ثانویه
    if not os.path.exists(file_path) and os.path.exists("sub.txt"):
        file_path = "sub.txt"

    caption = "🚀 Latest V2Ray Configs\n📌 Update: Automated Crow-V2Ray"

    if os.path.exists(file_path):
        print(f"Sending configurations from '{file_path}' to platforms...")
        
        # ارسال به بله
        send_to_bale(file_path, caption)
        
        # ارسال به تلگرام
        send_to_telegram(file_path, caption)
    else:
        print(f"File {file_path} not found!")


if __name__ == "__main__":
    main()
