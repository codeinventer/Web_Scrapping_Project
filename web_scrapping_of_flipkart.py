from bs4 import BeautifulSoup
import requests
import pandas as pd
page=requests.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup = BeautifulSoup(page.content,'html.parser')
model_name=soup.find_all('div',class_="_4rR01T")
#for item in model_name:
 #     print(item.get_text())
#print(model_name[0].get_text())
price = soup.find_all(class_="_30jeq3 _1_WHN1")
rating = soup.select("._1lRcqv ._3LWZlK")
#for i in rating:
 #   print(i.get_text())
#len(rating)
model = [item.get_text() for item in model_name]
price= [item.get_text() for item in price]
rating = [item.get_text() for item in rating]
laptops = pd.DataFrame({"Model":model,"Rating":rating,"Price":price})
print(laptops)
