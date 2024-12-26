from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# دالة لطباع النصوص بشكل منسق
def cetak(text):
    print(text)

# إعداد المتصفح وتثبيت driver الخاص بـ Chromium
def install_browser():
    """إعداد المتصفح باستخدام Selenium (Chromium)."""
    global driver
    options = Options()
    options.add_argument('--headless')  # تشغيل المتصفح في وضع بدون واجهة رسومية (اختياري)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # تعيين المسار إلى chromedriver (تأكد من المسار الصحيح في جهازك)
    chromedriver_path = "/data/data/com.termux/files/home/storage/downloads/chromedriver_linux64/chromedriver"  # تأكد من المسار الصحيح

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

# دالة تسجيل الدخول إلى Facebook
def login():
    """وظيفة تسجيل الدخول باستخدام Selenium."""
    try:
        email = input("أدخل البريد الإلكتروني: ")
        password = input("أدخل كلمة المرور: ")

        cetak("[*] جارٍ فتح المتصفح وتسجيل الدخول...")
        driver.get("https://m.facebook.com")
        
        # الانتظار حتى يتم تحميل الصفحة
        time.sleep(2)

        # العثور على عناصر البريد الإلكتروني وكلمة المرور
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'pass')
        
        # إدخال البيانات
        email_field.send_keys(email)
        password_field.send_keys(password)
        
        # إرسال النموذج
        password_field.send_keys(Keys.RETURN)

        # الانتظار قليلاً حتى يتم تحميل الصفحة بعد إرسال النموذج
        time.sleep(3)

        # التحقق من حالة تسجيل الدخول
        if 'save-device' in driver.current_url or 'home.php' in driver.current_url:
            cetak("[*] تم تسجيل الدخول بنجاح!")
        elif 'checkpoint' in driver.current_url:
            cetak("[!] الحساب مغلق (Checkpoint). حاول تسجيل الدخول يدويًا.")
        else:
            cetak("[!] فشل تسجيل الدخول. تحقق من البيانات.")
    except Exception as e:
        cetak(f"[!] حدث خطأ أثناء تسجيل الدخول: {e}")

# الدالة الرئيسية
def main():
    """الدالة الرئيسية."""
    install_browser()
    login()

if __name__ == "__main__":
    main()
