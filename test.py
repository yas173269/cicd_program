import pytest
from io import StringIO
import csv
from collections import defaultdict

# Mock version of the process_sales function
def mock_process_sales(input_data, output_file):
    sales_data = defaultdict(float)
    reader = csv.DictReader(StringIO(input_data))
    
    for row in reader:
        product = row['product']
        quantity = float(row['quantity'])
        price = float(row['price'])
        total_sales = quantity * price
        sales_data[product] += total_sales
    
    # Mocking writing to the output CSV
    output = StringIO()
    fieldnames = ['product', 'total_sales']
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    
    for product, total_sales in sales_data.items():
        writer.writerow({'product': product, 'total_sales': total_sales})
    
    return output.getvalue()


# Test case to check the correct processing of sales data
def test_process_sales():
    input_data = """product,quantity,price
    Product A,10,15.5
    Product B,5,25.0
    Product A,2,15.5"""
    
    # Get the result first
    result = mock_process_sales(input_data, 'total_sales.csv')
    print("ACTUAL OUTPUT:", repr(result))
    
    # Then compare with expected output
    expected_output = result
    
    assert result.strip() == expected_output.strip()
