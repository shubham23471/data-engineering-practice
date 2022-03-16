from urllib import response
from zipfile import ZipFile
import zipfile
import requests
import os 
import time
from datetime import date, datetime

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]


def make_dirs():
    cwd = os.getcwd()
    download_folder = cwd + '/' + 'downloads'
    os.makedirs(download_folder, exist_ok=True)
    print('Folder created')
    return download_folder


def download_zip_files(uris, download_folder):
    """ 
    1) check the `downloads` dir exist if not then create if  
    2) Download zip file
    """
    for uri in uris:
        print("VALIDATING... : {}".format(uri))
        response = requests.get(uri, stream=True)
        if response.status_code == 200:
            print('--> URI VALID.')
            file_nm = uri.split('/')[-1]
            print('--> STARTED DOWNLOADING..')
            with open(download_folder + '/' + file_nm, 'wb') as zip_file:
                for chunk in response.iter_content(chunk_size=1024*1024):
                    zip_file.write(chunk)
            print('--> {} DOWNLOADED'.format(file_nm))
        else:
            print('URI INVALID :: {}'.format(uri))

def unzip_delete_files(download_folder):
    """ Unzip and delete zip file"""
    zip_files = [zip_file for zip_file in os.listdir(download_folder) if zip_file.endswith('.zip')]
    print('UNZIPPING FILES...')
    for file in zip_files:
        file_name = download_folder + '/' + file
        with ZipFile(file_name, 'r') as zipobj:
            zipobj.extractall(download_folder)
        os.remove(file_name)
        print('DONE')
    return 


def main():
    print("**************** STARTING SCRIPT ****************")
    download_folder = make_dirs()
    download_zip_files(download_uris , download_folder)
    unzip_delete_files(download_folder)
    

if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()

    # total time to complete
    total_time = end_time - start_time
    print("TOTAL TIME: ", round(total_time / 60, 2))
    print("**************** END ****************")



# TODO
# 1. Add async functionality
# 2. Unit testing