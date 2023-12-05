import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
sesuaikan semua element sesuai dengan elemen pada html target
elemen dibawah ini hanyalah contoh kasus
'''
def check_in():
    driver.find_element(By.ID, "userId").send_keys(username)
    driver.find_element(By.ID, "userPassword").send_keys(password)
    driver.find_element(By.ID, "kt_login_signin_submit").click()
    time.sleep(2)

    # Mengubah ukuran halaman menjadi ukuran perangkat seluler
    set_device_metrics = {
        "width": 375,
        "height": 667,
        "deviceScaleFactor": 2,
        "mobile": True
    }
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", set_device_metrics)

    actions = ActionChains(driver)
    actions.click(driver.find_element(By.ID, "kt_login_signin_submit")).perform()
    time.sleep(1)
    # Menjalankan JavaScript untuk mereload halaman dengan user agent perangkat seluler
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent})
    
    driver.find_element(By.ID, "kt_aside_mobile_toggle").click()
    time.sleep(1)

    driver.find_element(By.ID, "kt_quick_fab_toggle").click()
    time.sleep(1)

    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "#custReason > option:nth-child(2)").click()
    time.sleep(10)
    
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(5) 

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "aside-overlay"))
    )

    script = "document.querySelector('.aside-overlay').click();"
    driver.execute_script(script)
    
    driver.find_element(By.ID, "fab-1-In").click()
    time.sleep(9)
    
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(5)

def check_out():
    
    actions = ActionChains()
    set_device_metrics = {
        "width": 375,
        "height": 667,
        "deviceScaleFactor": 2,
        "mobile": True
    }
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", set_device_metrics)

    # Menjalankan JavaScript untuk mereload halaman dengan user agent perangkat seluler
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent})
    
    driver.find_element(By.ID, "kt_aside_mobile_toggle").click()
    time.sleep(1)

    driver.find_element(By.ID, "kt_quick_fab_toggle").click()
    time.sleep(1)

    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "#custReason > option:nth-child(2)").click()
    time.sleep(10)
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "aside-overlay"))
    )

    script = "document.querySelector('.aside-overlay').click();"
    driver.execute_script(script)

    driver.find_element(By.ID, "fab-1-Out").click()
    time.sleep(9)

    actions.send_keys(Keys.ENTER).perform()
    time.sleep(5)
    
schedule.every().day.at('23:29').do(check_in)
schedule.every().day.at('23:30').do(check_out)

username = ""  # Isi usernamemu
password = ""  # isi passwordmu

#untuk lokasi tempat anda login
Map_coordinates = dict({
    "latitude": -0.9560453472593481,
    "longitude": 122.793032100726,
    "accuracy": 100
})

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument(r"--use-file-for-fake-video-capture=C:\Users\Yudha Mansoba\Documents\draft proposal\RAW PROJECT YUDHA\ABSENSI\kode qr.y4m")
#chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_camera": 1
})
driver = webdriver.Chrome(options=chrome_options)

driver.get("")#isi dengan link

while True:
    schedule.run_pending()
    time.sleep(2)
