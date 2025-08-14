# eBay Laptop Scraper

## 📌 Overview
This Python script scrapes laptop listings from eBay that match specific filters (1TB SSD, 32GB RAM) and saves the results to an Excel file (`laptops.xlsx`).  
It collects:
- **Name** of the laptop
- **Price**
- **Shipping cost**
- **Listing link**

## 🚀 Features
- Scrapes **multiple pages** of search results  
- Uses **custom headers** to avoid blocking  
- Saves data in **Excel** format for easy analysis  

## 🛠️ Requirements
Make sure you have Python 3 installed, then install dependencies:
```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## ▶️ How to Run
1. Clone this repository:
```bash
git clone https://github.com/YOUR-USERNAME/ebay-laptop-scraper.git
cd ebay-laptop-scraper
```
2. Run the script:
```bash
python scraper.py
```
3. After running, check `laptops.xlsx` for the results.

## ⚠️ Notes
- You can adjust the **eBay search URL** in the script to target different filters or categories.  
- **Avoid hardcoding cookies** if possible — they may expire quickly.  
- Be mindful of **eBay's Terms of Service** when scraping.  

## 📸 Example Output
![Example Output](example_output.png)

## 📜 License
This project is open-source under the MIT License.
