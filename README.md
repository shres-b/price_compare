
# Product Comparison Tool

This Python script helps you compare product prices across multiple retailers, with a focus on Canadian e-commerce websites.

**Features**

* **Product Search:** Leverages Google Search to find product pages on specified retailers (currently supports Amazon.ca and Visions.ca).
* **Price Scraping:** Extracts product titles and prices from retailer websites using web scraping.
* **Comparison Report:** Provides both a console output and a CSV file summarizing the price comparisons.

**Dependencies**

* `requests` 
* `beautifulsoup4`
* `lxml`
* `csv`
* `pytest`

**Instructions**

1. **Install Requirements:**
   ```bash
   pip install requests beautifulsoup4 lxml csv
   ```

2. **Modify the Script:**
    * Update the `product` variable with the product you want to track.
    * Add more retailers to the `results` dictionary if necessary.
    * Adjust the `track_product_price` function to match the HTML structure of each retailer's product pages.

3. **Run the Script:**
    ```bash 
    python product_comparison.py
    ```

**Output**

* The script will print the following to the console: 
  ```
  Amazon: Product Title - Product Price
  Visions: Product Title - Product Price
  ...
  ```
* A CSV file named `product_comparison_report.csv` will be generated, containing retailer names, product descriptions, and prices in a structured format.

**Notes**

* Website structures can change, potentially breaking the price scraping logic. You might need to periodically update the selectors in the `track_product_price` function.
* Always respect websites' robots.txt files to avoid overloading them with requests.

**Future Enhancements**

* Expand support to include more Canadian retailers.
* Implement a command-line interface (CLI) for easier user interaction.
* Add email or notification features to alert users when prices change.

**Let me know if you'd like assistance with any of these potential improvements!** 
