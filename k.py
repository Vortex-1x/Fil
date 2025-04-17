import requests
import time

# تحميل البروكسيات من الملف
with open("proxy.txt", "r") as f:
    proxies_list = [line.strip() for line in f if line.strip()]

# User-Agent حقيقي لتفادي الحظر
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

# تجربة البروكسي
def test_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        response = requests.get("https://www.facebook.com", headers=headers, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(f"شغال: {proxy}")
            print("Cookies:", response.cookies.get_dict())
            return True
    except Exception as e:
        print(f"فشل: {proxy} - {e}")
    return False

# تجربة البروكسيات
for proxy in proxies_list:
    if test_proxy(proxy):
        break  # توقف عند أول واحد شغال
    time.sleep(1)  # مهلة قصيرة لتفادي الحظر المؤقت
