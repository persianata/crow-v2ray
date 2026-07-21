import os
import requests

# خواندن اطلاعات از متغیرهای محیطی (Secrets) گیت‌هاب
BALE_TOKEN = os.getenv("BALE_TOKEN")
BALE_CHAT_ID = os.getenv("CHAT_ID")  # یا BALE_CHAT_ID اگر تغییر دادید

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


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
    # فرض بر این است که فایل‌های کانفیگ شما اینجا استخراج/ساخته می‌شوند
    # و مسیر آن‌ها مشخص است. مثلاً فرض می‌کنیم فایلی به نام configs.txt دارید:
    file_path = "configs.txt" 
    caption = "🚀 Latest V2Ray Configs\n📌 Update: Automated Crow-V2Ray"

    # ساخت یا بررسی وجود فایل نمونه برای تست (اگر در پروژه شما تولید می‌شود)
    if os.path.exists(file_path):
        print("Sending configurations to platforms...")
        
        # ارسال به بله
        send_to_bale(file_path, caption)
        
        # ارسال به تلگرام
        send_to_telegram(file_path, caption)
    else:
        print(f"File {file_path} not found!")


if __name__ == "__main__":
    main()
