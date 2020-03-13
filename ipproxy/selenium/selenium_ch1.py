from selenium import webdriver




driver_path = r'C:\Users\mafuqiang\Envs\pachong1\Scripts\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://account.cnblogs.com')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_css_selector('#LoginName').send_keys('woshimaxiaoqiang@163.com')
driver.find_element_by_css_selector('#Password').send_keys('qiang*010286')
driver.find_element_by_css_selector('#submitBtn').click()