from selenium import webdriver
driver = webdriver.Firefox(executable_path=r"geckodriver")
driver.get("https://python.org")
driver.close()

print("Hola Mundo")
