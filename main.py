import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from pystyle import Colorate, Colors
import os
import time

os.system("cls")
print(Colorate.Horizontal(Colors.blue_to_cyan, """
 _____ _ _   _           _    ______  _____  _____ _____ 
|  __ (_) | | |         | |   | ___ \|  _  ||  _  |_   _|
| |  \/_| |_| |__  _   _| |__ | |_/ /| | | || | | | | |  
| | __| | __| '_ \| | | | '_ \| ___ \| | | || | | | | |  
| |_\ \ | |_| | | | |_| | |_) | |_/ /\ \_/ /\ \_/ / | |  
 \____/_|\__|_| |_|\__,_|_.__/\____/  \___/  \___/  \_/  
========================================================
       https://github.com/EgooDev/   By egodev       
========================================================                                    
"""))
username = input(Colorate.Horizontal(Colors.blue_to_cyan, "Enter your github username: ")).strip()
views = int(input(Colorate.Horizontal(Colors.blue_to_cyan, "Views to generate: ").strip()))

options = uc.ChromeOptions()
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = uc.Chrome(options=options)

url = f"https://github.com/{username}"

driver.get(url)
print((Colorate.Horizontal(Colors.cyan_to_green,f"Succesfuly connected on: https://github.com/{username}")))

for i in range(views):
    driver.refresh()
    print(Colorate.Horizontal(Colors.cyan_to_green,f"Views Added {i+1}/{views}"))
    time.sleep(0.1) 

print(Colorate.Horizontal(Colors.blue_to_cyan, "Successfully added views!"))
time.sleep(2)
