
import unittest
import pandas as pd
from validators import data_validators

class TestDataValidators(unittest.TestCase):
    def setUp(self):
        self.df_valid = pd.DataFrame({
            'date': ['2023-01-01', '2023-02-01'],
            'amount': [5000, 15000],
            'name': ['Alice', 'Bob']
        })
        self.df_invalid_date = pd.DataFrame({
            'date': ['invalid-date', 'another-bad-date'],
            'amount': [100, 200]
        })
        self.required_columns = ['date', 'amount', 'name']

    def test_required_columns_present(self):
        missing = data_validators.required_columns_present(self.df_valid, self.required_columns)
        self.assertEqual(missing, [])

        missing = data_validators.required_columns_present(self.df_valid, self.required_columns + ['extra'])
        self.assertIn('extra', missing)

    def test_validate_date_column(self):
        self.assertTrue(data_validators.validate_date_column(self.df_valid, 'date'))
        self.assertFalse(data_validators.validate_date_column(self.df_invalid_date, 'date'))

    def test_high_value_transactions(self):
        high_value_df = data_validators.high_value_transactions(self.df_valid)
        self.assertEqual(len(high_value_df), 1)
        self.assertEqual(high_value_df.iloc[0]['amount'], 15000)

if __name__ == '__main__':
    unittest.main()
