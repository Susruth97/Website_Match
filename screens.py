import time
from selenium import webdriver

def get_screenShots(urls1, urls2) :

    driver1 = webdriver.Chrome()
    driver2 = webdriver.Chrome()

    authenciation(driver1)
    time.sleep(3)
    authenciation(driver2)
    time.sleep(3)

    for i in range(0, len(urls1)) :

        driver1.switch_to.window(driver1.window_handles[-1])
        driver2.switch_to.window(driver2.window_handles[-1])

        driver1.get(urls1[i])
        driver2.get(urls2[i])

        if i == 0 :
            time.sleep(40)
        else :
            time.sleep(25)

        class1 = driver1.find_element_by_class_name('visualContainerHost')
        class1.screenshot('src1/img_' + str(i + 1) + '.png')
        class2 = driver2.find_element_by_class_name('visualContainerHost')
        class2.screenshot('src2/img_' + str(i + 1) + '.png')

    driver1.quit()

def authenciation(driver) :
    user = "v-shlakh@microsoft.com"
    pwd = "Oct@1996"
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
    time.sleep(10)

    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(2)



