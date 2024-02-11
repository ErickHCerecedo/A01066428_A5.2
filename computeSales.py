"""
This program computes the total cost of sales based
on a price catalogue and sales records.

Author: Erick de Jesus Hernandez Cerecedo
Student ID: A01066428
Date: February 11, 2014
Document Version: 1
"""
# pylint: disable=invalid-name
import json
import sys
import time


class ComputeSales:
    """
    Class to compute the total cost of sales.
    """

    def __init__(self, price_catalogue_file, sales_record_file):
        self.price_catalogue_file = price_catalogue_file
        self.sales_record_file = sales_record_file
        self.total_cost = 0
        self.elapsed_time = 0

    def load_json_file(self, filename):
        """
        Loads a JSON file.

        Args:
            filename (str): Name of the JSON file to load.

        Returns:
            dict: Data loaded from the JSON file, or None if there is an error.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file '{filename}'.")
            return None

    def compute_total_cost(self, price_catalogue, sales_record):
        """
        Computes the total cost of sales using the price catalogue.

        Args:
            price_catalogue (list): List of products with their prices.
            sales_record (list): List of sales records.

        Returns:
            float: Total cost of all sales.
        """
        price_catalogue_dict = {
            item['title']: item['price']
            for item in price_catalogue
        }
        total_cost = 0
        for sale in sales_record:
            product_name = sale['Product']
            quantity = sale['Quantity']
            if product_name in price_catalogue_dict:
                total_cost += price_catalogue_dict[product_name] * quantity
            else:
                print(f"Error: Product '{product_name}' "
                      f"not found in the price catalogue.")
        return total_cost

    def print_results(self, total_cost, elapsed_time):
        """
        Prints the results of the sales processing.

        Args:
            total_cost (float): Total cost of all sales.
            elapsed_time (float): Time elapsed during sales processing.
        """
        self.total_cost = round(total_cost, 2) 
        self.elapsed_time = round(elapsed_time, 10)
        print("------ Sales Results ------")
        print(f"Total sales cost: ${self.total_cost}")
        print(f"Time elapsed: {self.elapsed_time} seconds")
        print("---------------------------\n\n")
        with open("SalesResults.txt", "a", encoding='utf-8') as results_file:
            results_file.write("------ Sales Results ------\n")
            results_file.write(f"Total sales cost: ${self.total_cost}\n")
            results_file.write(f"Time elapsed: {self.elapsed_time} seconds\n")
            results_file.write("---------------------------\n\n")

    def process_sales(self):
        """
        Processes the sales by loading JSON files,
        computing total cost, and printing results.
        """
        start_time = time.time()

        price_catalogue = self.load_json_file(self.price_catalogue_file)
        if price_catalogue is None:
            return

        sales_record = self.load_json_file(self.sales_record_file)
        if sales_record is None:
            return

        total_cost = self.compute_total_cost(price_catalogue, sales_record)
        elapsed_time = time.time() - start_time

        self.print_results(total_cost, elapsed_time)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: "
              "python computeSales.py priceCatalogue.json salesRecord.json")
    else:
        sales_processor = ComputeSales(sys.argv[1], sys.argv[2])
        sales_processor.process_sales()
