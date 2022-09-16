# here we are trying to get the students stored details and vote.....
import random
import requests
from bs4 import BeautifulSoup
import mechanicalsoup
import base64
import csv
import pandas as pd
#import openpyxl



def encode(str):
    HERE = base64.b64encode(bytes(str, 'utf-8'))
    out = HERE.decode('ascii')
    return out

def get_phone(url, company_name, id):
    #print(url[:url.index('.ng/') + 4], company_name, id)
    path = url[:url.index('.ng/') + 4] + "ws/getp?p=company&a=get_ph_json&idx=" + encode(id+'--'+company_name)
    #print(path)
    r = requests.get(url=path)
    _o = BeautifulSoup(r.json()['0'], 'html.parser')
    _o.find_all("phone trigger-call")
    precise = ""
    for i in _o:
        precise = precise + i.text
    return precise
    
def get_details(link):
    r = requests.get(url=link)
    soup = BeautifulSoup(r.text, 'html.parser')
    address = soup.find("div", {"class": "address_com address.address mid-wrapper"}).text[7:]
    more_details = soup.find("span", {"class": "description"}).text
    return [address, more_details]


def the_chief(url):
    result = []
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, 'html.parser')
    companies = soup.find_all('li', {'class': "company card eventa", "data-id": "company_list_ver_ficha_body"})
    #soup.get_attribute_list
    category = url.split('/')
    category = category[len(category) -1]
    print('Saving In file...')
    for i in companies:
        #get the link for more details on the company
        comp_links = i.find('a').get('href')
        splt_comp = comp_links.split('/')
        company_name = splt_comp[len(splt_comp)-2]
        #company_rm = company_name.replace('-', ' ')
        idx = splt_comp[len(splt_comp)-1]
        #idx = comp_links[ comp_links.rindex('/') ]
        company_rm = i.find('span', {"class": "title-com"})            
        #get company phone number
        phone = get_phone(url, company_name, idx)
        streetAddress = i.find('span', {"class": "streetAddress"})
        addressLocality = i.find('span', {"class": "addressLocality"})
        addressState = i.find('span', {"class": "addressState"})
        #the address and more
        #address, more_d = get_details(comp_links)
        print( company_rm.text, idx, phone, addressLocality.text, category)
        result.append([company_rm.text, streetAddress.text, addressLocality.text, addressState.text, phone, idx ])

    df = pd.DataFrame(result, columns=['company','streetAddress', 'addressLocality','addressState', 'phone','idx'])
    df.to_excel(url[8:12]+str(random.randint(1, 15))+category+'.xlsx', sheet_name='new_sheet_name', index=False)
    print("Done Saving")
    
    """ with open(url[8:12]+str(random.randint(1, 15)) + ".csv","w",encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['company','address', 'phone','idx'])

        for i in companies:
            #get the link for more details on the company
            comp_links = i.find('a').get('href')
            splt_comp = comp_links.split('/')
            company_name = splt_comp[len(splt_comp)-2]
            #company_rm = company_name.replace('-', ' ')
            idx = splt_comp[len(splt_comp)-1]
            #idx = comp_links[ comp_links.rindex('/') ]
            company_rm = i.find('span', {"class": "title-com"})            
            #get company phone number
            phone = get_phone(url, company_name, idx)
            address = i.find('p', {"class": "address"})
            #the address and more
            #address, more_d = get_details(comp_links)
            #print( company_rm, idx, phone, address, more_d)
            writer.writerow([company_rm.text, address.text, phone, idx ]) 
        print("Done Saving") """



browser = mechanicalsoup.StatefulBrowser()
urls = ['https://port-harcourt.infoisinfo.ng/search/consultancy', 'https://port-harcourt.infoisinfo.ng/search/car-repair', 'https://kaduna.infoisinfo.ng/search/computer', 'https://kaduna.infoisinfo.ng/search/electric-appliances', 'https://kaduna.infoisinfo.ng/search/construction', 'https://kaduna.infoisinfo.ng/search/hotel']

for i in urls:
    the_chief(i)
    
    #url = 'https://port-harcourt.infoisinfo.ng/search/consultancy'
#print(url[url.rindex('/') + 1:])
