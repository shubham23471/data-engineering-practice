import pandas as pd 
import json
import time
import os 


data_dir = '/'.join([os.getcwd(), 'data'])

def make_download_dir():
    cwd = os.getcwd()
    download_folder = cwd + '/' + 'downloads'

    if os.path.exists(download_folder):
        print('Folder Exists')
    else:
        os.makedirs(download_folder, exist_ok=True)
        print('Folder created')
    return download_folder
    
def json_file_dir(input_dir):
    json_file_abs_dir = []

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.json'):
                json_file = '/'.join([root, file])
                json_file_abs_dir.append(json_file)
    return json_file_abs_dir

def flatten_json(json_file):
    """Read the json file and flatten it
    Returns:
        - flattened json
    """
    flattened_data = dict()
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    for key, value in data.items():
        if not isinstance(value, dict):
            flattened_data[key] = value
        else:
            for k, v in value.items():
                if isinstance(v, list):
                    for num, element in enumerate(v):
                        flattened_data[key + '_' + k + '_' + str(num + 1)] = element
    return flattened_data

def save_to_csv(json_files):
    print("SAVING TO CSV...")
    for json_file in json_files:
        flatten_data = flatten_json(json_file)
        
        csv_file_nm = json_file.split('/')[-1].split('.')[0] + '.csv'
        
        pd.DataFrame([flatten_data]).to_csv(csv_file_nm, index=False)

    print("DONE")

def main():
    # your code here
    json_file_abs_dir = json_file_dir(data_dir)    
    save_to_csv(json_file_abs_dir)
    

if __name__ == '__main__':
    print("**************** STARTING SCRIPT ****************")
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print("TOTAL TIME : {} sec(s)".format(round(total_time, 2)))
    print("**************** END ****************")
