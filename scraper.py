import requests

SOURCES = [
    "https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/main/mix.txt",
    "https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/main/v2ray.txt",
    "https://raw.githubusercontent.com/0xRadikal/Free-v2ray-Configs/main/all/configs.txt",
    "https://raw.githubusercontent.com/MrRabbitson/RabbitProxyZ-proxy-list/main/proxy-list.txt",
    "https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/main/config.txt",
    "https://raw.githubusercontent.com/iboxz/free-v2ray-collector/main/main/mix.txt",
    "https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/sub/sub.txt",
    "https://raw.githubusercontent.com/MohammadBahemmat/V2ray-Collector/main/sub/sub.txt",
    "https://raw.githubusercontent.com/mohamadfg-dev/telegram-v2ray-configs-collector/main/v2ray.txt",
    "https://raw.githubusercontent.com/R3ZARAHIMI/tg-v2ray-configs-every2h/main/v2ray.txt"
]

def get_all_configs():
    all_lines = []
    for url in SOURCES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                all_lines.extend(response.text.splitlines())
        except: continue
    return list(set([line for line in all_lines if line.strip()]))

if __name__ == "__main__":
    configs = get_all_configs()
    # تولید ۲۰ فایل
    for i in range(20):
        batch = configs[i*200 : (i+1)*200]
        if not batch: break
        with open(f"sub{i+1}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(batch))
