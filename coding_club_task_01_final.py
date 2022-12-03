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
        result_rating = soup.find_all('div', {'class': 'product-ratingsContainer'})
        results = soup.find_all('div', {'class': 'product-productMetaInfo'})

        for i in range(len(result_rating)):
            tup = (results[i].h3.text, results[i].h4.text, result_rating[i].text)
            page.append(tup)
            
        library.append(page)
        
    return library


def write_csv():
    with open('cc_task_01.csv', 'w') as fh:
        writer = csv.writer(fh)
        library = web_scrape()
        writer.writerow(['Name', 'Category', 'Rating'])
        for page in library:
            for record in page:
                if 'sneaker' in record[1].lower():
                    writer.writerow(record)

    return None


write_csv()
        
        
        


