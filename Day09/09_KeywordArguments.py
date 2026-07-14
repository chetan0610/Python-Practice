"""
Program 9: Keyword Arguments
Description: Calls a function using explicit keyword arguments in various orders.
"""

def display_product_info(product_name, category, price):
    """
    Displays information about a product.
    
    Args:
        product_name (str): The name of the product.
        category (str): The product category.
        price (float): The price of the product.
    """
    print(f"Product: {product_name:<15} | Category: {category:<12} | Price: ${price:.2f}")

if __name__ == "__main__":
    # Challenge: Create five different calls using different parameter orders
    print("--- Product Database ---")
    display_product_info(product_name="Laptop", category="Electronics", price=999.99)
    display_product_info(price=45.50, product_name="Running Shoes", category="Footwear")
    display_product_info(category="Home Goods", price=120.00, product_name="Coffee Maker")
    display_product_info(product_name="Python Book", price=29.99, category="Books")
    display_product_info(price=3.99, category="Snacks", product_name="Potato Chips")