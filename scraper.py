import requests
import base64

# لیست ۱۰ منبع معتبر و فعال
SOURCES = [
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/main/v2ray.txt",
    "https://raw.githubusercontent.com/freefq/free/master/v2",
    "https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub",
    "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub.txt",
    "https://raw.githubusercontent.com/2Interceptor/V2Ray-Nodes/main/nodes.txt",
    "https://raw.githubusercontent.com/tbbt-service/v2ray-subscribe/main/v2ray",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vless",
    "https://raw.githubusercontent.com/yebekhe/V2RayCollector/main/sub/sub.txt",
    "https://raw.githubusercontent.com/pekaone/v2ray-subscriber/master/v2ray.txt",
    "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub1.txt"
]

def get_configs():
    all_raw_data = []
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                # هر خط را به عنوان یک کانفیگ جداگانه در نظر می‌گیریم
                all_raw_data.extend(response.text.splitlines())
        except: continue
    return all_raw_data

if __name__ == "__main__":
    all_lines = get_configs()
    # حذف موارد تکراری و خالی
    unique_lines = list(set([line for line in all_lines if line.strip()]))
    
    # تقسیم به دو دسته ۱۰۰۰ تایی
    batch1 = unique_lines[:1000]
    batch2 = unique_lines[1000:2000]
    
    # ذخیره فایل‌ها به صورت Base64
    def save_file(filename, data):
        encoded = base64.b64encode("\n".join(data).encode('utf-8')).decode('utf-8')
        with open(filename, "w") as f:
            f.write(encoded)

    save_file("sub1.txt", batch1)
    save_file("sub2.txt", batch2)
