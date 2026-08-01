# PRODIGY_SD_05

# Web Scraping using Python

## Description

This project was developed as **Task 5** of the **Prodigy InfoTech Software Development Internship**.

The application scrapes book details from the **Books to Scrape** website using Python. It extracts the book title, price, and rating, converts the prices into Indian Rupees (using a fixed exchange rate for demonstration), displays the data in the console, and saves it into a CSV file.

---

## Features

- Extract Book Name
- Extract Price
- Extract Rating
- Convert GBP to INR
- Display Data in Console
- Save Data to CSV

---

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas

---

## Website Used

https://books.toscrape.com/

---

## Required Libraries

```bash
pip install requests beautifulsoup4 pandas
```

---

## How to Run

```bash
python main.py
```

---

## Project Structure

```
PRODIGY_SD_05
│
├── main.py
├── books.csv
├── README.md
└── screenshot.png
```

---

## Sample Output

```
Book Name                                    Price (INR)    Rating

A Light in the Attic                         Rs.5953.55     Three
Tipping the Velvet                           Rs.6179.10     One
Soumission                                   Rs.5761.50     One
Sharp Objects                                Rs.5499.30     Four
```

---

## Future Improvements

- Scrape multiple pages
- Store data in a database
- Export to Excel
- Use a live currency exchange API
- Allow users to enter any website URL

---
