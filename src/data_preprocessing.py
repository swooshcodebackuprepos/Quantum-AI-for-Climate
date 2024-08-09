import os
import requests
import xarray as xr
import pandas as pd

# Function to download and save data
def download_data(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = url.split('/')[-1]
    filepath = os.path.join(folder, filename)
    response = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {filename}")

# Function to load NetCDF datasets
def load_datasets(folder, ext='.nc'):
    data_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(ext)]
    datasets = [xr.open_dataset(file) for file in data_files]
    combined_ds = xr.concat(datasets, dim='time')
    return combined_ds

# Function to preprocess data
def preprocess_data():
    # URLs for datasets
    ersst_urls = [
        "https://www.ncei.noaa.gov/pub/data/cmb/ersst/v4/netcdf/ersst.v4.202001.nc",
        "https://www.ncei.noaa.gov/pub/data/cmb/ersst/v4/netcdf/ersst.v4.202002.nc",
    ]
    
    # Download datasets
    for url in ersst_urls:
        download_data(url, 'data/ersst_v4_data')

    # Load datasets
    ersst_data = load_datasets('data/ersst_v4_data')
    return ersst_data

if __name__ == "__main__":
    ersst_data = preprocess_data()
