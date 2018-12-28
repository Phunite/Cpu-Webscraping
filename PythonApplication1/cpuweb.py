import bs4
from urllib.request import urlopen as URequest
from bs4 import BeautifulSoup as soup

url='https://www.newegg.com/Processors-Desktops/SubCategory/ID-343'
uClient=URequest(url)
page_html=uClient.read()
uClient.close()
page_soup= soup(page_html,"html.parser") #get the entire page using soup

# find all the div with the class name of "item-container" and store it into containers
containers= page_soup.find_all("div",{"class":"item-container"})

file_name="Product.cs"
f= open(file_name,"w")
headers="Price, Product_name, Image \n"

f.write(headers)

for container in containers:
   item_title=container.img["title"]
   price_container=container.find_all("li",{"class":"price-current"})
   item_price='$' + price_container[0].strong.text + '.99'
   item_img=container.img["src"]
   #print('Name: '+ item_title)
   #print('Price: '+'$'+ item_price +'.99')
   #print('Image: '+ item_img)
   f.write(item_price+","+ item_title.replace(".","|") + "," + item_img + "\n")

f.close()
   