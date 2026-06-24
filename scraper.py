import requests
import base64

# لیست منابع معتبر و فعال (آپدیت شده)
SOURCES = [
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/main/v2ray.txt",
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub.txt"
]

def get_configs():
    final_data = ""
    for url in SOURCES:
        try:
            # ایجاد یک درخواست با محدودیت زمانی برای جلوگیری از کندی ربات
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                # اضافه کردن محتوا به لیست نهایی
                final_data += response.text + "\n"
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            continue
    return final_data

if __name__ == "__main__":
    configs = get_configs()
    
    # حذف خطوط خالی برای تمیزتر شدن فایل خروجی
    clean_configs = "\n".join([line for line in configs.splitlines() if line.strip()])
    
    # کدگذاری به Base64 (این فرمت استاندارد سابسکریپشن است)
    encoded_result = base64.b64encode(clean_configs.encode('utf-8')).decode('utf-8')
    
    with open("subscription.txt", "w", encoding="utf-8") as f:
        f.write(encoded_result)
