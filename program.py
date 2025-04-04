import csv
from collections import defaultdict

# Function to read, process, and write sales data
def process_sales(input_file, output_file):
    sales_data = defaultdict(float)  # A dictionary to accumulate total sales for each product

    # Reading the input CSV file
    with open(input_file, mode='r') as infile:
        reader = csv.DictReader(infile)  # Use DictReader to read rows as dictionaries
        
        for row in reader:
            product = row['product']
            quantity = float(row['quantity'])
            price = float(row['price'])
            
            # Calculate total sales for each product
            total_sales = quantity * price
            sales_data[product] += total_sales
    
    # Writing the output CSV file
    with open(output_file, mode='w', newline='') as outfile:
        fieldnames = ['product', 'total_sales']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for product, total_sales in sales_data.items():
            writer.writerow({'product': product, 'total_sales': total_sales})

process_sales('sales_data.csv', 'total_sales.csv')
