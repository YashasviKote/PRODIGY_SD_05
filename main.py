import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Fixed Exchange Rate (Example)
exchange_rate = 115  # 1 GBP = ₹115

try:
    # Send HTTP Request
    response = requests.get(url)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")

    # List to store data
    data = []

    print("=" * 110)
    print("{:<50} {:<15} {:<10}".format("Book Name", "Price (INR)", "Rating"))
    print("=" * 110)

    for book in books:

        # Book Name
        title = book.h3.a["title"]

        # Price in GBP
        price_text = book.find("p", class_="price_color").text

        # Remove £ symbol and convert to float
        price_gbp = float(price_text.replace("£", "").replace("Â", ""))

        # Convert to INR
        price_inr = round(price_gbp * exchange_rate, 2)

        # Rating
        rating = book.find("p")["class"][1]

        # Display
        print("{:<50} ₹{:<13} {:<10}".format(title, price_inr, rating))

        # Save Data
        data.append([title, f"₹{price_inr}", rating])

    # Create DataFrame
    df = pd.DataFrame(data, columns=["Book Name", "Price (INR)", "Rating"])

    # Save CSV File
    df.to_csv("books.csv", index=False)

    print("\n==============================================")
    print("Data successfully saved to books.csv")
    print("==============================================")

except Exception as e:
    print("Error:", e)