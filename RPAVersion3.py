from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from bs4 import BeautifulSoup
import time
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
import os
import shutil
import urllib.parse
import math

# Setting WebDriver to chrome
driver = webdriver.Chrome()

# Function for calculate when user choose day
def get_day_position(day, start_day_of_week):

    # Calculate Position
    day_index = day + start_day_of_week - 2  # index start 0
    tr = day_index // 7 + 1     # row
    td = day_index % 7 + 1      # column

    return tr, td

# Function for calculate page for using max_pages
def get_max_pages():

    # Pull XPATH ALL ROWS
    rows_ALL = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/div')
    rows_text = rows_ALL.text.strip()  

    index_of_of = rows_text.find('of')
    rows_count = float(rows_text[index_of_of + 2:].strip())

    # Split Text back 'of'
    rows_count = float(rows_text.split('of')[-1].strip())  

    pages_pp = math.ceil(rows_count / 10)  
    
    print(pages_pp)

    return pages_pp

try:
    # Open Website
    driver.get("https://pm-rsm.cpretailink.co.th/login")
    # output_dir = "download_images"
    time.sleep(2)

    # Put Username & Password then Enter Login
    username_user = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div/div/div[2]/form/div[1]/input')
    password_user = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div/div/div[2]/form/div[2]/div/input')

    #   Edit username & password here !!
    username_put = 'benjaponsuns'
    password_put = 'Benjapon@0125'

    username_user.send_keys(username_put)
    password_user.send_keys(password_put)

    password_user.send_keys(Keys.RETURN)
    time.sleep(2)

    # Select Part of year you want to check
    selecting_part = driver.find_element(By.XPATH, '/html/body/app-root/app-plan-search/div/div/div[2]/app-search-pm-box/div/form/div[1]/div[2]/mat-form-field/div[1]/div[2]/div[1]/input')
    selecting_part.click()
    time.sleep(2)

    # Selecting Year
    # Just 2023 - 2024 - 2025
    #   Edit year here !!
    year_put = 2024

    if year_put == 2023:
        year_select = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-multi-year-view/table/tbody/tr[6]/td[2]/button/div[1]')
        year_select.click()
        time.sleep(2)
    elif year_put == 2024:
        year_select = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-multi-year-view/table/tbody/tr[6]/td[3]/button/div[1]')
        year_select.click()
        time.sleep(2)
    elif year_put == 2025:
        year_select = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-multi-year-view/table/tbody/tr[6]/td[4]/button/div[1]')
        year_select.click()
        time.sleep(2)

    # Selecting month
    #   Edit month here !!
    month_put = 1

    month_table = {1: [2,1], 2: [2,2], 3: [2,3], 4: [2,4], 5: [3,1], 6: [3,2], 7: [3,3], 8: [3,4], 9: [4,1], 10: [4,2], 11: [4,3], 12: [4,4]}

    month_select = driver.find_element(By.XPATH, f'/html/body/div/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-year-view/table/tbody/tr[{month_table[month_put][0]}]/td[{month_table[month_put][1]}]/button')
    month_select.click()
    time.sleep(2)

    # STATIC PART # START

    # Select ALL from search from
    search_select = driver.find_element(By.XPATH, '/html/body/app-root/app-plan-search/div/div/div[2]/app-search-pm-box/div/form/div[2]/div[2]/mat-button-toggle-group/mat-button-toggle[4]/button/span')
    search_select.click()
    time.sleep(2)

    # Select Company part
    cpn_select = driver.find_element(By.XPATH, '/html/body/app-root/app-plan-search/div/div/div[2]/app-search-pm-box/div/form/div[3]/div[2]/app-multi-search-box/div/input')
    cpn_select.click()
    time.sleep(2)

    cpn_select = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[2]/angular2-multiselect/div/div[1]/div')
    cpn_select.click()
    time.sleep(2)

    seven_select = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[2]/angular2-multiselect/div/div[2]/div[3]/div[2]/ul/li[1]/label')
    seven_select.click()
    time.sleep(2)

    finish_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[1]/button')
    finish_button.click()
    time.sleep(2)

    # Select Contract type
    contract_select = driver.find_element(By.XPATH, '/html/body/app-root/app-plan-search/div/div/div[2]/app-search-pm-box/div/form/div[4]/div[2]/app-multi-search-box/div/input')
    contract_select.click()
    time.sleep(2)

    contract_select = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[2]/angular2-multiselect/div/div[1]/div')
    contract_select.click()
    time.sleep(2)

    PP_contract = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[2]/angular2-multiselect/div/div[2]/div[3]/div[2]/ul/li[7]/label')
    PP_contract.click()
    time.sleep(2)

    finish_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/div/div/app-dialog-multiselect/div/div[1]/button')
    finish_button.click()
    time.sleep(2)

    # Select search
    search_button = driver.find_element(By.XPATH, '/html/body/app-root/app-plan-search/div/div/div[2]/app-search-pm-box/div/form/div[7]/button')
    search_button.click()
    time.sleep(3)

    # STATIC PART # STOP

    # Get position on day in month
    #   Problem(?) User must check calendar everytime when use it ***
    #   or Programming when user choosed to click on calendar and then send value on this

    #   Edit day here !!
    day = 1
    #   Edit start day here !!
    start_day_of_week = 2

    # Calculate position of day
    tr, td = get_day_position(day, start_day_of_week)

    day_xpath = f'/html/body/app-root/app-e-service-plan/div/full-calendar/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[{tr}]/td[{td}]/div/div[2]/div[1]/a'
    driver.find_element(By.XPATH, day_xpath).click()
    time.sleep(2)

    # Var downloaded_urls
    downloaded_urls = set() 

    # Var current page
    current_page = 1

    # Var next count & i for count click
    next_count = 1
    i = 1

    # max pages should fill by Total of pages that calculated
    max_pages = get_max_pages()

    # Not finish Page
    if current_page <= max_pages:
        try:
            total_rows = len(driver.find_elements(By.XPATH, '//app-table-contract/div/table/tbody/tr'))
            print(f"พบหัวข้อทั้งหมด {total_rows} รายการในหน้า {current_page}")

            if current_page == 1:
                try:
                    # Topic 1 - end
                    for row_index in range(1, total_rows + 1):
                        try:
                            topic_xpath = f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[5]'
                            topic_link = driver.find_element(By.XPATH, topic_xpath)
                                    
                            if 5 <= row_index < total_rows:
                                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                time.sleep(3)

                                # Check 'รหัสร้าน' before Click
                                number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                number_store_text = number_store.text.strip() 

                                # Click 'ดูรูปภาพ'
                                driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                topic_link.click()
                                print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                time.sleep(3)

                                div_elements = driver.find_elements(By.XPATH, '/html/body/app-root/app-images/div/div')
                                image_idx = 1

                                # Create Folder of store before Downloading image
                                # os.makedirs({number_store_text})
                                os.makedirs(f"download_images/{str(number_store_text)}", exist_ok=True)
                                output_dir = f"download_images/{number_store_text}"

                                # Download Picture for keep in folder
                                for div_element in div_elements:
                                    image_elements = div_element.find_elements(By.TAG_NAME, 'img')

                                    for img in image_elements:
                                        image_url = img.get_attribute("src")
                                        if image_url.endswith(".svg"):
                                            print(f"ข้ามไฟล์ SVG: {image_url}")
                                            continue
                                        if image_url in downloaded_urls:
                                            print(f"ข้ามรูปที่เคยดาวน์โหลด: {image_url}")
                                            continue

                                        response = requests.get(image_url, stream=True)
                                        if response.status_code == 200:
                                            filename = os.path.join(output_dir, f"downloaded_image_page{current_page}_{row_index}_{image_idx}.jpg")
                                            with open(filename, 'wb') as file:
                                                for chunk in response.iter_content(1024):
                                                    file.write(chunk)
                                                print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                downloaded_urls.add(image_url)
                                                image_idx += 1
                                        else:
                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")


                                driver.back()
                                time.sleep(3)

                            elif row_index < 5:
                                # Check 'รหัสร้าน' before Click
                                number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                number_store_text = number_store.text.strip()

                                driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                topic_link.click()
                                print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                time.sleep(3)

                                div_elements = driver.find_elements(By.XPATH, '/html/body/app-root/app-images/div/div')
                                image_idx = 1

                                # Create Folder of store before Downloading image
                                # os.makedirs({number_store_text})
                                os.makedirs(f"download_images/{str(number_store_text)}", exist_ok=True)
                                output_dir = f"download_images/{number_store_text}"

                                # Download Picture for keep in folder
                                for div_element in div_elements:
                                    image_elements = div_element.find_elements(By.TAG_NAME, 'img')

                                    for img in image_elements:
                                        image_url = img.get_attribute("src")
                                        if image_url.endswith(".svg"):
                                            print(f"ข้ามไฟล์ SVG: {image_url}")
                                            continue
                                        if image_url in downloaded_urls:
                                            print(f"ข้ามรูปที่เคยดาวน์โหลด: {image_url}")
                                            continue

                                        response = requests.get(image_url, stream=True)
                                        if response.status_code == 200:
                                            filename = os.path.join(output_dir, f"downloaded_image_page{current_page}_{row_index}_{image_idx}.jpg")
                                            with open(filename, 'wb') as file:
                                                for chunk in response.iter_content(1024):
                                                    file.write(chunk)
                                                print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                downloaded_urls.add(image_url)
                                                image_idx += 1
                                        else:
                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")


                                driver.back()
                                time.sleep(3)
                            
                            elif row_index == total_rows:
                                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                time.sleep(3)

                                # Check 'รหัสร้าน' before Click
                                number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                number_store_text = number_store.text.strip()

                                driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                topic_link.click()
                                print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                time.sleep(3)

                                div_elements = driver.find_elements(By.XPATH, '/html/body/app-root/app-images/div/div')
                                image_idx = 1

                                # Create Folder of store before Downloading image
                                # os.makedirs({number_store_text})
                                os.makedirs(f"download_images/{str(number_store_text)}", exist_ok=True)
                                output_dir = f"download_images/{number_store_text}"

                                # Download Picture for keep in folder
                                for div_element in div_elements:
                                    image_elements = div_element.find_elements(By.TAG_NAME, 'img')

                                    for img in image_elements:
                                        image_url = img.get_attribute("src")
                                        if image_url.endswith(".svg"):
                                            print(f"ข้ามไฟล์ SVG: {image_url}")
                                            continue
                                        if image_url in downloaded_urls:
                                            print(f"ข้ามรูปที่เคยดาวน์โหลด: {image_url}")
                                            continue

                                        response = requests.get(image_url, stream=True)
                                        if response.status_code == 200:
                                            filename = os.path.join(output_dir, f"downloaded_image_page{current_page}_{row_index}_{image_idx}.jpg")
                                            with open(filename, 'wb') as file:
                                                for chunk in response.iter_content(1024):
                                                    file.write(chunk)
                                                print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                downloaded_urls.add(image_url)
                                                image_idx += 1
                                        else:
                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")


                                driver.back()
                                time.sleep(3)

                                current_page += 1

                                next_button = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/button[3]/span[4]')
                                
                                next_button.click()
                                time.sleep(3)
                                
                                driver.execute_script("window.scrollTo(0, 0);")
                                time.sleep(2)

                        except Exception as e:
                            print(f"เกิดข้อผิดพลาดในหัวข้อที่ {row_index}: {e}")
                            break

                except Exception as e:
                    print(f"เกิดข้อผิดพลาด: {e}")

            if current_page >= 2:
                try:
                    # Topic 1 - end
                    for row_index in range(1, total_rows + 1):
                        try:
                            topic_xpath = f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[5]'
                            topic_link = driver.find_element(By.XPATH, topic_xpath)
                                    
                            if 5 <= row_index < total_rows:

                                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                time.sleep(3)

                                # Check 'รหัสร้าน' before Click
                                number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                number_store_text = number_store.text.strip()

                                driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                topic_link.click()
                                print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                time.sleep(3)

                                div_elements = driver.find_elements(By.XPATH, '/html/body/app-root/app-images/div/div')
                                image_idx = 1

                                # Create Folder of store before Downloading image
                                # os.makedirs({number_store_text})
                                os.makedirs(f"download_images/{str(number_store_text)}", exist_ok=True)
                                output_dir = f"download_images/{number_store_text}"

                                # Download Picture for keep in folder
                                for div_element in div_elements:
                                    image_elements = div_element.find_elements(By.TAG_NAME, 'img')

                                    for img in image_elements:
                                        image_url = img.get_attribute("src")
                                        if image_url.endswith(".svg"):
                                            print(f"ข้ามไฟล์ SVG: {image_url}")
                                            continue
                                        if image_url in downloaded_urls:
                                            print(f"ข้ามรูปที่เคยดาวน์โหลด: {image_url}")
                                            continue

                                        response = requests.get(image_url, stream=True)
                                        if response.status_code == 200:
                                            filename = os.path.join(output_dir, f"downloaded_image_page{current_page}_{row_index}_{image_idx}.jpg")
                                            with open(filename, 'wb') as file:
                                                for chunk in response.iter_content(1024):
                                                    file.write(chunk)
                                                print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                downloaded_urls.add(image_url)
                                                image_idx += 1
                                        else:
                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")


                                driver.back()
                                time.sleep(3)

                                for next_count in range(i):
                                    try:
                                        next_button = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/button[3]/span[4]')
                                        next_button.click()
                                        time.sleep(3)

                                    except Exception as e:
                                        print(f"เกิดข้อผิดพลาด: {e}")
                                        break

                            elif row_index < 5:

                                driver.execute_script("window.scrollTo(0, 0);")
                                time.sleep(2)

                                # Check 'รหัสร้าน' before Click
                                number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                number_store_text = number_store.text.strip()

                                driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                topic_link.click()
                                print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                time.sleep(3)

                                div_elements = driver.find_elements(By.XPATH, '/html/body/app-root/app-images/div/div')
                                image_idx = 1

                                # Create Folder of store before Downloading image
                                # os.makedirs({number_store_text})
                                os.makedirs(f"download_images/{str(number_store_text)}", exist_ok=True)
                                output_dir = f"download_images/{number_store_text}"

                                # Download Picture for keep in folder
                                for div_element in div_elements:
                                    image_elements = div_element.find_elements(By.TAG_NAME, 'img')

                                    for img in image_elements:
                                        image_url = img.get_attribute("src")
                                        if image_url.endswith(".svg"):
                                            print(f"ข้ามไฟล์ SVG: {image_url}")
                                            continue
                                        if image_url in downloaded_urls:
                                            print(f"ข้ามรูปที่เคยดาวน์โหลด: {image_url}")
                                            continue

                                        response = requests.get(image_url, stream=True)
                                        if response.status_code == 200:
                                            filename = os.path.join(output_dir, f"downloaded_image_page{current_page}_{row_index}_{image_idx}.jpg")
                                            with open(filename, 'wb') as file:
                                                for chunk in response.iter_content(1024):
                                                    file.write(chunk)
                                                print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                downloaded_urls.add(image_url)
                                                image_idx += 1
                                        else:
                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")


                                driver.back()
                                time.sleep(3)

                                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                time.sleep(3)

                                for next_count in range(i):
                                    try:
                                        next_button = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/button[3]/span[4]')
                                        next_button.click()
                                        time.sleep(3)

                                    except Exception as e:
                                        print(f"เกิดข้อผิดพลาด: {e}")
                                        break

                                driver.execute_script("window.scrollTo(0, 0);")
                                time.sleep(2)
                            
                            elif row_index == total_rows:
                                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                time.sleep(3)

                                # Check 'รหัสร้าน' before Click
                                number_store = driver.find_element(By.XPATH, f'/html/body/app-root/app-e-service-table/div/app-table-contract/div/table/tbody/tr[{row_index}]/td[6]')
                                number_store_text = number_store.text.strip()

                                driver.execute_script("arguments[0].scrollIntoView(true);", topic_link)
                                topic_link.click()
                                print(f"กำลังคลิกหัวข้อที่ {row_index} ในหน้า {current_page}")
                                time.sleep(3)

                                div_elements = driver.find_elements(By.XPATH, '/html/body/app-root/app-images/div/div')
                                image_idx = 1

                                # Create Folder of store before Downloading image
                                # os.makedirs({number_store_text})
                                os.makedirs(f"download_images/{str(number_store_text)}", exist_ok=True)
                                output_dir = f"download_images/{number_store_text}"

                                # Download Picture for keep in folder
                                for div_element in div_elements:
                                    image_elements = div_element.find_elements(By.TAG_NAME, 'img')

                                    for img in image_elements:
                                        image_url = img.get_attribute("src")
                                        if image_url.endswith(".svg"):
                                            print(f"ข้ามไฟล์ SVG: {image_url}")
                                            continue
                                        if image_url in downloaded_urls:
                                            print(f"ข้ามรูปที่เคยดาวน์โหลด: {image_url}")
                                            continue

                                        response = requests.get(image_url, stream=True)
                                        if response.status_code == 200:
                                            filename = os.path.join(output_dir, f"downloaded_image_page{current_page}_{row_index}_{image_idx}.jpg")
                                            with open(filename, 'wb') as file:
                                                for chunk in response.iter_content(1024):
                                                    file.write(chunk)
                                                print(f"ดาวน์โหลดรูปภาพสำเร็จ: {filename}")
                                                downloaded_urls.add(image_url)
                                                image_idx += 1
                                        else:
                                            print(f"ไม่สามารถดาวน์โหลดรูปภาพจาก {image_url} ได้ (HTTP {response.status_code})")


                                driver.back()
                                time.sleep(3)

                                current_page += 1

                                for next_count in range(i):
                                    try:
                                        next_button = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/button[3]/span[4]')
                                        next_button.click()
                                        time.sleep(3)
                                        
                                    except Exception as e:
                                        print(f"เกิดข้อผิดพลาด: {e}")
                                        break

                                i += 1

                                next_button = driver.find_element(By.XPATH, '/html/body/app-root/app-e-service-table/div/mat-paginator/div/div/div[2]/button[3]/span[4]')
                                next_button.click()
                                time.sleep(3)

                        except Exception as e:
                            print(f"เกิดข้อผิดพลาด: {e}")
                            break
                
                except Exception as e:
                    print(f"เกิดข้อผิดพลาด: {e}")

        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}")

finally:
    driver.quit()

