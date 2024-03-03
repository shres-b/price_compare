import unittest
from unittest.mock import patch  # For mocking network requests
from price_compare.main import find_url_from_google, track_product_price

class TestMain(unittest.TestCase):
    # @patch('requests.get')  
    # def test_correct_url_format(self, mock_get):
    #     mock_get.return_value.text = '<html>...some simulated HTML...</html>' 
    #     result = find_url_from_google('bestbuy.ca', 'Laptop Model XYZ')
    #     self.assertEqual(result, 'https://some-mocked-url/from-bestbuy') 
    
    @patch('requests.get')
    def test_amazon_price_extraction(self, mock_get):
        amazon_html = """
        <span id="productTitle">Samsung TV Model X</span>
        <span class="a-offscreen">$250.00</span>
        """
        mock_get.return_value.content = amazon_html
        title, price = track_product_price('amazon', 'https://amazon.ca/some-product')
        self.assertEqual(title, 'Samsung TV Model X')
        self.assertEqual(price, '$250.00')
