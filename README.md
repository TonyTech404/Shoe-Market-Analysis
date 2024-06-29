
---

# Shoe Market Analysis

This project involves scraping data on shoe prices from various online retailers and visualizing the data using Tableau. The goal is to provide insights into the shoe market by analyzing average prices, discounts, price distribution, and price ranges for different shoe brands.

## Project Structure

The project is divided into several scripts and files:

- `urlscrape.py`: This script contains the code for scraping data from various online retailers. It collects information such as brand name, product name, price, sales price, and discount.
- `transform.py`: This script is used to transform the scraped data into a format suitable for analysis and visualization in Tableau.
- `Dashboard 2.png`: An image of the Tableau dashboard created using the scraped and transformed data.

## Visualizations

The Tableau dashboard includes the following visualizations:

1. **Average Price Per Brand**: This bar chart shows the average price of shoes for each brand.
2. **Brand Average Discount**: This bar chart displays the average discount offered by each brand.
3. **Price Distribution**: A scatter plot comparing the average price and average sales price of shoes for each brand.
4. **Brand Price Range**: A box plot showing the price range of shoes for each brand, including the average sales price.

![Dashboard](Dashboard%202.png)

## Installation and Usage

To run this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/shoe-market-analysis.git
   cd shoe-market-analysis
   ```

2. **Install dependencies**:
   Ensure you have the necessary Python packages installed. You can use `pip` to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper**:
   Execute the `urlscrape.py` script to scrape data from the online retailers:
   ```bash
   python urlscrape.py
   ```

4. **Transform the data**:
   Use the `transform.py` script to process the scraped data:
   ```bash
   python transform.py
   ```

5. **Visualize the data**:
   Open Tableau and load the processed data to create the visualizations as shown in `Dashboard 2.png`.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
