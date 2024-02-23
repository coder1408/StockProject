#!/bin/bash

# Navigate to the directory where your Python script is located
cd C:\Users\ishan\Desktop\Ishan\Coding\Projects\BabaStocks\bulk.ipynb

# Download the CSV file from the NSE website
wget -O data.csv "https://www.nseindia.com/path/to/your/csv/file"

# Run your Python script with the downloaded CSV file
python your_script.py data.csv
