from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = '7d97e1fa'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.MiuiSettings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print("启动【设置】应用")
driver.quit()