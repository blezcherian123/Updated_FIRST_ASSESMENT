
"""
validators.py

This module contains file and data validation functions used in the application.
"""

import os
import pandas as pd

# ---------------------------
# File Validation Functions
# ---------------------------

ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
MAX_FILE_SIZE_MB = 5

def is_allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_valid_file_size(file):
    """
    Check if the uploaded file is within the allowed file size limit.
    """
    file.seek(0, os.SEEK_END)
    size_mb = file.tell() / (1024 * 1024)
    file.seek(0)
    return size_mb <= MAX_FILE_SIZE_MB

# ---------------------------
# Data Validation Functions
# ---------------------------

def required_columns_present(df, required_columns):
    """
    Check for missing required columns in the DataFrame.
    Returns a list of missing columns.
    """
    missing = [col for col in required_columns if col not in df.columns]
    return missing

def validate_date_column(df, date_col):
    """
    Validates that the given date column can be parsed into datetime.
    Returns True if successful, False otherwise.
    """
    try:
        pd.to_datetime(df[date_col])
        return True
    except Exception:
        return False

def high_value_transactions(df, amount_col='amount', threshold=10000):
    """
    Filters transactions in the DataFrame with an amount higher than the given threshold.
    Returns a filtered DataFrame.
    """
    if amount_col in df.columns:
        return df[df[amount_col] > threshold]
    return pd.DataFrame()
