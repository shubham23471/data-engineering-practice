import boto3
import os
import time 
import botocore


BUCKET_NAME="commoncrawl"
OBJECT_NAME="commoncrawl/CC-MAIN-2022-05/robotstxt.paths.gz"
FILE_NAME="robotstxt.paths.gz"


def make_download_dir():
    cwd = os.getcwd()
    download_folder = cwd + '/' + 'downloads'

    if os.path.exists(download_folder):
        print('Folder Exists')
    else:
        os.makedirs(download_folder, exist_ok=True)
        print('Folder created')
    return download_folder

def download_file():
    s3 = boto3.client('s3', config=botocore.client.Config(signature_version=botocore.UNSIGNED))    
    s3.download_file(BUCKET_NAME, OBJECT_NAME,  FILE_NAME)

# def download_all_files():
#     print("here")
#     #initiate s3 resource
#     s3 = boto3.resource('s3', botocore.client.Config(signature_version=botocore.UNSIGNED))
#     # select bucket
#     my_bucket = s3.Bucket(BUCKET_NAME)
#     # print(my_bucket.objects)

#     # download file into current directory
#     for s3_object in my_bucket.objects.all():
#         filename = s3_object.key
#         print(filename)
#         # my_bucket.download_file(s3_object.key, filename)



def main():
    download_folder =  make_download_dir()
    # download_file()
    download_all_files()  


if __name__ == '__main__':
    print("**************** STARTING SCRIPT ****************")
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()

    total_time = end_time - start_time
    print("TOTAL TIME :: {}".format(round(total_time / 60 , 2)))
    print("**************** END ****************")
