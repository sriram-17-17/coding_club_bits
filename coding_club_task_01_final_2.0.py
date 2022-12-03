import csv
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

  
def web_scrape():
    library = []
    for p in range(1, 5):
        url = 'https://www.myntra.com/shoes?p=' + str(p)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')



        page = []
        products = soup.find_all('li', {'class': 'product-base'})
        for product in products:
            Name = product.find('div', {'class': 'product-productMetaInfo'}).h3.text
            Category = product.find('div', {'class': 'product-productMetaInfo'}).h4.text

            try:    
                rating = product.find('div', {'class': 'product-ratingsContainer'}).text
            except AttributeError:
                rating = ''

            
            tup = (Name, Category, rating)
            page.append(tup)
            
    

        library.append(page)

        
    return library


def write_csv():
    with open('cc_task_01_try.csv', 'w') as fh:
        writer = csv.writer(fh)
        library = web_scrape()
        writer.writerow(['Name', 'Category', 'Rating'])
        for page in library:
            for record in page:
                if 'sneaker' in record[1].lower():
                    writer.writerow(record)

    return None


write_csv()
        



