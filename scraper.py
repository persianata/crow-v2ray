import requests
import base64

# لیست منابع معتبر (این‌ها آدرس‌های اصلی هستند)
SOURCES = [
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub"
]

def get_configs():
    final_data = ""
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                final_data += response.text + "\n"
        except:
            continue
    return final_data

if __name__ == "__main__":
    configs = get_configs()
    # تبدیل به Base64 برای اینکه در برنامه کار کند
    encoded = base64.b64encode(configs.encode('utf-8')).decode('utf-8')
    with open("subscription.txt", "w") as f:
        f.write(encoded)
