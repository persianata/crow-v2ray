import requests
import base64

# لینک مستقیم فایل خروجی این ریپازیتوری که فرستادی
SOURCES = [
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/main/v2ray.txt"
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
    # این منبع خودش کانفیگ‌ها را در قالب بیس۶۴ دارد، 
    # اگر دیدی در برنامه کار نمی‌کند، خط پایین را فقط بنویس: f.write(configs)
    with open("subscription.txt", "w", encoding="utf-8") as f:
        f.write(configs)
