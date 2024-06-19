import os
import json
import csv
import pandas as pd
import ftfy

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def fix_text(text):
    return ftfy.fix_text(text)

def extract_customer_details(json_data):
    customer_details = []
    if 'messages' in json_data:
        for message in json_data['messages']:
            sender_name = fix_text(message.get('sender_name', ''))
            content = fix_text(message.get('content', ''))
            timestamp = message.get('timestamp_ms', '')
            customer_details.append({
                'sender_name': sender_name,
                'content': content,
                'timestamp': pd.to_datetime(timestamp, unit='ms', errors='coerce')
            })
    return customer_details

def save_to_csv(data, output_path):
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Customer details extracted and saved to {output_path}")

def process_all_json_files(parent_folder):
    all_customer_details = []
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.json'):
                    json_file_path = os.path.join(folder_path, file_name)
                    if os.path.isfile(json_file_path):
                        json_data = read_json_file(json_file_path)
                        customer_details = extract_customer_details(json_data)
                        all_customer_details.extend(customer_details)
    return all_customer_details

# Path to the parent folder containing the JSON folders
parent_folder_path = 'C:/Users/hrido/Downloads/inbox'

# Use Documents directory for the output CSV file to avoid permission issues
output_csv_path = os.path.join(os.path.expanduser('~'), 'Documents', 'customer_details.csv')

all_customer_details = process_all_json_files(parent_folder_path)
save_to_csv(all_customer_details, output_csv_path)
