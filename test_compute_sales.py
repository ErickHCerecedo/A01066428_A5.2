"""
This is a test document files for computeSales.py

Author: Erick de Jesus Hernandez Cerecedo
Student ID: A01066428
Date: February 11, 2014
Document Version: 1
"""
import unittest
from computeSales import ComputeSales

class TestComputeStatistics(unittest.TestCase):
    """
    Test class for computeSales.py
    """
    
    def setUp(self):
        """
        Set up test cases.
        """
        self.test_cases = [
            {"catalogue_file": "TC1/TC1.ProductList.json", "sales_file": "TC1/TC1.Sales.json", "expected_total_cost": 2481.86},
            {"catalogue_file": "TC2/TC1.ProductList.json", "sales_file": "TC2/TC2.Sales.json", "expected_total_cost": 166568.23},
            {"catalogue_file": "TC3/TC1.ProductList.json", "sales_file": "TC3/TC3.Sales.json", "expected_total_cost": 165235.37}
        ]

    def test_TC1(self):
        """
        Test case 1: Verify the total cost calculation for TC1.
        """
        catalogue_data = self.test_cases[0]["catalogue_file"]
        sales_data = self.test_cases[0]["sales_file"]

        sales_processor = ComputeSales(catalogue_data, sales_data)
        sales_processor.process_sales()
        expected_total_cost = self.test_cases[0]["expected_total_cost"]
        self.assertEqual(sales_processor.total_cost, expected_total_cost)

    def test_TC2(self):
        """
        Test case 2: Verify the total cost calculation for TC2.
        """
        catalogue_data = self.test_cases[1]["catalogue_file"]
        sales_data = self.test_cases[1]["sales_file"]

        sales_processor = ComputeSales(catalogue_data, sales_data)
        sales_processor.process_sales()
        expected_total_cost = self.test_cases[1]["expected_total_cost"]
        self.assertEqual(sales_processor.total_cost, expected_total_cost)

    def test_TC3(self):
        """
        Test case 3: Verify the total cost calculation for TC3.
        """
        catalogue_data = self.test_cases[2]["catalogue_file"]
        sales_data = self.test_cases[2]["sales_file"]

        sales_processor = ComputeSales(catalogue_data, sales_data)
        sales_processor.process_sales()
        expected_total_cost = self.test_cases[2]["expected_total_cost"]
        self.assertEqual(sales_processor.total_cost, expected_total_cost)
