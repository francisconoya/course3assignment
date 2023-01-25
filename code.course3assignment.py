def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe


extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])



for csvfile in glob.glob('*.csv'):
    extracted_data=extracted_data.append(extract_from_csv(csvfile), ignore_index=True)

for jsonfile in glob.glob('*.json'):
    extracted_data=extracted_data.append(extact_from_json(jsonfile), ignore_index=True)

return extracted_data

#transform: inches to milimiters and round off to 2 decimals

def transform(data):
    data['height'] = round(data.height * 0.0254, 2)
    data['weight'] = round(data.weight * 0.45359237, 2)

    return data 

def load(targetfile, data_to_load):
    data_to_load.to_csv(targetfile)
    targetfile = 'transformed_data.csv'
    load(targetfile, transformed_data)

#logging

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open('logfile.txt', 'a') as f:
        f.write (timestamp + 's' + message + '\')



extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])

for csvfile in glob.glob('*.csv'):
    extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)

for jsonfile in glob.glob('*.json'):
    extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)

return extracted_data


def transform (data):
    data['height'] = round(data.height * 0.024564, 2)
    data['weight'] = round(data.weight * 0.45034065564654543, 2)

    return data 

def load(targetfile, data_to_load):
    data_to_load.to_csv(targetfile)
    targetfile = 'transformed_data.csv'
    load(targetfile, transformed_data)

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open('logfile.txt, 'a') as f:
        f.write (timestamp + ',' + message + '\n')
