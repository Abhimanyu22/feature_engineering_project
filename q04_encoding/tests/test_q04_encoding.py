# Default Imports
from unittest import TestCase
import pandas as pd
from ..build import encoding
from inspect import getargspec


class TestEncoding(TestCase):
    def test_encoding(self):
        # Input parameters tests
        args = getargspec(encoding)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types
        ny_housing = pd.read_csv('data/train.csv')
        housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
        encoded_housing_data = encoding(housing_data)

        self.assertIsInstance(encoded_housing_data, pd.core.frame.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(encoded_housing_data)))

        # Return value tests
        self.assertEqual(encoded_housing_data.shape, (1460, 11), "Return value shape does not match expected value")
