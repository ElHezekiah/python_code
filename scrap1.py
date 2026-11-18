import requests
from bs4 import BeautifulSoup
import csv

url = 'https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def scrape_books():
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            products = soup.find_all('article', class_='product_pod')
            
            print(f"Status: Berhasil terhubung. Ditemukan {len(products)} produk.\n")

            with open('Laporan_Scraping_Mikael.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['Nama Produk', 'Harga', 'Status Stok', 'Rating'])
                
                for item in products:
                    title = item.h3.a['title']

                    price = item.find('p', class_='price_color').text.strip()
                    
                    availability = item.find('p', class_='instock availability').text.strip()

                    rating_class = item.find('p', class_='star-rating')['class'][1]

                    print(f"Judul   : {title}")
                    print(f"Harga   : {price}")
                    print(f"Stok    : {availability}")
                    print(f"Rating  : {rating_class}")
                    print("-" * 40)

                    writer.writerow([title, price, availability, rating_class])
                    
            print("\nData berhasil diekspor ke file 'Laporan_Scraping_Mikael.csv'")
        else:
            print(f"Gagal mengakses halaman. Kode Status: {response.status_code}")
            
    except Exception as e:
        print(f"Terjadi kesalahan teknis: {e}")

if __name__ == "__main__":
    scrape_books()