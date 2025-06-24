from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

url = "https://btc240.netlify.app/"

while True:
    try:
        driver.set_page_load_timeout(60)
        driver.get(url)
        print("✅ زيارة ناجحة:", url)
        time.sleep(30)
    except Exception as e:
        print("❌ خطأ أثناء تحميل الصفحة:", e)
        time.sleep(10)
    time.sleep(60)