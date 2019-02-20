import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import threading

def get_screenShots(urls1, urls2, names1, names2, source1, source2, username, password) :

    try :
        driver1 = webdriver.Chrome(executable_path='webdriver/chromedriver.exe')
        driver2 = webdriver.Chrome(executable_path='webdriver/chromedriver.exe')

        authenciation(driver1, username, password)
        time.sleep(2)
        authenciation(driver2, username, password)

        print('Authentication Completed')
        time.sleep(2)

        t1 = threading.Thread(target=screenshots_powerBI, args=(driver1, urls1, names1, source1))
        t2 = threading.Thread(target=screenshots_powerBI, args=(driver2, urls2, names2, source2))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        driver1.quit()
        driver2.quit()
    except Exception as e :
        print(e)

def authenciation(driver, username, password) :
    try :
        user = username
        pwd = password
        url = "https://login.microsoftonline.com/common/oauth2/authorize?client_id=871c010f-5e61-4fb1-83ac-98610a7e9110&response_mode=form_post&response_type=code+id_token&scope=openid+profile&state=OpenIdConnect.AuthenticationProperties%3dxlHpggDIjUiED4boIr__piS15gKEVIPwkw3wqkZ9D86JirORoRviN_4ZzaaYKIGIRrUNAfL7-EqxuZU5hGLKNESpSjgh8-GOl6L2ccRogHwd8NkQLCCbjuTgz8SutXGlyvH9-2CmTm-P2VCR2LuwkA&nonce=636856457135966067.NzUzMGExNmYtZWNmYS00YWJkLWJhZDktMzIzNmQzNDUxNTMxMTJlZTM5MDUtOTYyYy00OWI4LTg0YzUtYzU0NTY2YmUyYmI5&site_id=500453&redirect_uri=https%3a%2f%2fapp.powerbi.com%2f%3fnoSignUpCheck%3d1&post_logout_redirect_uri=https%3a%2f%2fapp.powerbi.com%2f%3fnoSignUpCheck%3d1&resource=https%3a%2f%2fanalysis.windows.net%2fpowerbi%2fapi&nux=1&msafed=0"

        driver.get(url)

        elem = driver.find_element_by_id("i0116")
        elem.send_keys(user)
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
        time.sleep(10)

        driver.find_element_by_xpath('//*[@id="loginMessage"]/a/p').click()
        time.sleep(2)

        elem = driver.find_element_by_id("passwordInput")
        elem.send_keys(pwd)
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="submitButton"]').click()
        time.sleep(5)

        driver.find_element_by_xpath('//*[@id="WindowsAzureMultiFactorAuthentication"]').click()
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
        time.sleep(2)
    except Exception as e :
        print("Automating Authentication :", e)

def screenshots_powerBI(driver, urls, names, source) :

    try :
        for i in range(0, len(urls)):
            print('Fetching URL :', names[i])

            driver.switch_to.window(driver.window_handles[-1])
            driver.get(urls[i])

            element_present = EC.presence_of_element_located((By.XPATH, "//span[@class='collapsedFiltersTitle largeFontSize']"))
            WebDriverWait(driver, 15).until(element_present)

            time.sleep(30)
            element = driver.find_element_by_class_name('visualContainerHost')
            element.screenshot(source + '/img_' + str(i + 1) + '.png')
    except Exception as e :
        print(e)
    print('Screenshots Captured')