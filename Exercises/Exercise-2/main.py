from urllib import response
import requests
import pandas


def get_page_content():
    response = requests.get("https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/")
    print('status', response.status_code)
    print(response.content.find))

def main():
    # your code here
    get_page_content()


if __name__ == '__main__':
    print("**************** STARTING SCRIPT ****************")
    main()
