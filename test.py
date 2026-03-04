from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import pandas as pd
import time
import pyperclip
run_index = 0

# ---------- Read CSV ----------
data = pd.read_csv("ready_for_whatsapp_send.csv", names=["name", "website", "phone"], header=0, encoding='latin1')

# ---------- Firefox Setup ----------
options = Options()
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)

# Automatic set path from python
# driver = webdriver.Firefox(
#     service=Service(GeckoDriverManager().install()),
#     options=options
# )


# MAnually specify GeckoDriver path
driver = webdriver.Firefox(
    service=Service(r"C:\Users\geckodriver.exe"),
    options=options
)


time.sleep(4)

# ---------- Open WhatsApp Web ----------
driver.get("https://web.whatsapp.com/")

print("🔑 Scan QR code (first time only)...")
input("👉 Press Enter after WhatsApp Web is ready...")




# ========================= MAIN LOOP ===========================
for _, row in data.iterrows():

    try:
        name = str(row["name"]).strip()
        raw_phone = str(row["phone"]).strip()
        website = str(row["website"]).strip()




        # Remove non-numeric characters
        digits = "".join(filter(str.isdigit, raw_phone))

        if (
            (digits.startswith(("2", "3", "4", "5", "6", "7", "8", "9")) and len(digits) == 10) 
            # (digits.startswith(("9")) and len(digits) == 12) or (digits.startswith(("91", "92")) and len(digits) == 12)  or (digits.startswith(("965")) and len(digits) == 10)
        ):
            phone = f"+1{digits}"
        else:
            print(f"❌ Invalid USA  number  number: {raw_phone}")
            continue

        # ---------- Open Chat ----------
        wait1 = random.randint(5,10)
        time.sleep(wait1)

        driver.get(f"https://web.whatsapp.com/send?phone={phone}")
        
        wait = random.randint(25, 30)
        print(f"⏳ Loading chat... waiting {wait} seconds")
        time.sleep(wait)

        # ---------- Message Input Box ----------
        try:
            msg_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@contenteditable='true' and @data-tab='10']")
                )
            )
            time.sleep(10)
        except:
            try:
                msg_box = WebDriverWait(driver, 20).until(
                    (EC.presence_of_element_located(
                        (By.XPATH, "//div[@contenteditable='true' and @data-tab='6']")
                    ))
                )
            except:
                time.sleep(10)

                print(f"❌ Message box not found — number may not be on WhatsApp: {phone}")
                continue


        # ---------- Send Message Line-by-Line ----------
        test = [
            [
            f"👋 Hi {name},",
            f"🌐 Website: {website}", 
            f"📱 Phone: {phone}",
            "",
            "My name is Parvez Ahmed, and I am an AI Developer.",
            "",
            "I can build a website and an AI voice receptionist for your business.",
            "",
            "It will save your time and also help increase your business revenue.",
            "",
            "Note: And if you want to Show Demo, or increase your business?",
            "reply Yes, otherwise reply No.",
            ],
            [
            f"👋 Hello {name},",
            f"📱 Mobile No: {phone}",
            f"🌐 Website: {website}",
            "",
            "My name is Parvez Ahmed, and I am an AI Developer.",
            "",
            "I can create a  website and an AI voice receptionist for your business.",
            "",
            "This will save you time and help grow your business revenue.",
            "Note: If you want to increase your business?",
            " reply Yes or No.",
            ],
            [
            f"👋 Hi {name},",
            f"🌐 Website: {website}",
            f"📱 Contact: {phone}",
            "",
            "I am AI Developer And My Name is Parvez Ahmed.",
            "",
            "I can develop a website and an AI voice receptionist tailored to your business needs.",
            "",
            "It will automate your work, save your time, and increase your revenue.",
            "",
            "Note: Would you like to increase your business?",
            " Reply Yes or No ",
            ]
        ]


        selected_sms = test[run_index % len(test)]
        run_index += 1
        
        for line in selected_sms:
            pyperclip.copy(line)
            msg_box.send_keys(Keys.CONTROL, 'v')
            msg_box.send_keys(Keys.SHIFT , Keys.ENTER)
            time.sleep(2)
            # print("one by one second")
        time.sleep(4)
        msg_box.send_keys(Keys.ENTER)
        # print("sms successfully done")
        # print("now after  2 second press escap")
        time.sleep(2)
        body = driver.find_element("tag name", "body")
        body.send_keys(Keys.ESCAPE)
        # print("escap buttom pressed so now w8 for next number , ie 2 sec w8")
        time.sleep(2)

        print(f"✅ Message sent to {phone}")
        # driver.get("https://web.whatsapp.com/")
        # ---------- Delay for Anti-Block ----------
        delay = random.randint(250, 300)
        print(f"⏳ Waiting {delay} seconds before next number loaded...")
        time.sleep(delay)

    except Exception as e:
        print(f"⚠️ Error sending to {phone}: {str(e)}")
        time.sleep(25)

print("\n🎉 All messages sent successfully!")
driver.quit()
