'''
Entender:
    arquivo requirements
    webdriver
'''

# importing the csv module
import pandas as pd

#Import library from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Call methed
driver = webdriver.Chrome()

#Wait page to be loaded
driver.implicitly_wait(2)

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.get('https://www.nba.com/stats/alltime-leaders')

title = driver.title


select_element = driver.find_elements(By.TAG_NAME, 'select')
# print(select_element[3].text)
select = Select(select_element[3])
select.select_by_visible_text('All')

table_th= driver.find_elements(By.TAG_NAME, "th")
table_td = driver.find_elements(By.TAG_NAME, "td")
number_columns = 23

print(table_th[0].text)
print(table_td[0].text)

columns_count = 0
cabecalho = []
for th in table_th:
    columns_count += 1
    cabecalho.append(th.text)
    if columns_count == number_columns:
        break

columns_count = 0
celulas = []
linhas = []
for td in table_td:
    columns_count += 1
    celulas.append(td.text)
    if columns_count == number_columns:
        linhas.append(celulas)
        celulas = []
        columns_count = 0
    

# print(cabecalho)
# print(linhas)

df = pd.DataFrame(linhas, columns=cabecalho)
df.to_csv('out.csv', index=False)


print('o nome da página:', title)

# driver.quit()