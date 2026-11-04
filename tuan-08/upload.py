import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Khởi tạo WebDriver (Chrome)
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # 2. Truy cập vào trang File Upload của The Internet
    driver.get("https://the-internet.herokuapp.com/upload")
    print("Đã mở trang File Upload thành công.")

    # 3. Tạo một file tạm thời để test upload 
    test_file_path = os.path.abspath("test_upload.txt")
    with open(test_file_path, "w", encoding="utf-8") as f:
        f.write("Đây là nội dung kiểm thử tính năng upload file trong Selenium.")

    # 4. Tìm thẻ input type="file" bằng Explicit Wait
    file_input = wait.until(
        EC.presence_of_element_located((By.ID, "file-upload"))
    )

    # 5. Gửi đường dẫn tuyệt đối của file vào phần tử input thông qua send_keys()
    file_input.send_keys(test_file_path)
    print(f"Đã chọn file để upload: {test_file_path}")

    # 6. Nhấn nút Submit (nút 'Upload')
    upload_button = wait.until(
        EC.element_to_be_clickable((By.ID, "file-submit"))
    )
    upload_button.click()
    print("Đã nhấn nút Upload.")

    # 7. Chờ và xác thực kết quả tải lên thành công (Trang hiển thị dòng chữ 'File Uploaded!')
    success_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.example h3"))
    )
    
    uploaded_file_name = wait.until(
        EC.visibility_of_element_located((By.ID, "uploaded-files"))
    )

    print(f"Kết quả kiểm thử: {success_message.text}")
    print(f"Tên file đã tải lên: {uploaded_file_name.text}")

finally:
    driver.quit()