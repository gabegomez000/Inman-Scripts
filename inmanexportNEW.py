import requests
import logging
import pandas as pd
import json
import os
from dotenv import dotenv_values
from datetime import datetime

config = dotenv_values(".env")
logger = logging.getLogger(__name__)


# Function to read the last run timestamp from a text file
def read_timestamp_NEW():
    try:
        with open('timestamp_NEW.txt', 'r') as file:
            timestamp = file.read().strip()
            return timestamp
    except FileNotFoundError:
        # Set default timestamp for the first run
        print("\nERROR: timestamp_NEW.txt file not found. Using default timestamp - NONE")
        return ''


# Function to write the current timestamp to the text file
def write_timestamp_NEW():
    current_timestamp = datetime.now().strftime('%Y-%m-%d')
    with open('timestamp_NEW.txt', 'w') as file:
        file.write(current_timestamp)


# Read the last run timestamp
timestamp_NEW = read_timestamp_NEW()

if timestamp_NEW == '':
    print(f'This script has never been run. The query will return ALL members that meet the criteria.\n')
    user_input = input("Type 'yes' to continue and retrieve ALL members OR enter the desired date in the format YYYY-MM-DD: ")

    if user_input == 'yes':
        payload = {
            'Key': config['API_KEY'],
            'Operation': 'GetEntities',
            'Entity': 'cobalt_membership',
            'Filter': f'statuscode<eq>1 AND '
                      'ramco_associationid<eq>D9F2A0F9-F420-E111-B470-00155D000140 AND '
                      'ramco_primarymembership<eq>true AND '
                      '(cobalt_MemberTypeId<eq>d00b84b0-ef20-e111-b470-00155d000140 OR '
                      'cobalt_MemberTypeId<eq>d20b84b0-ef20-e111-b470-00155d000140 OR '
                      'cobalt_MemberTypeId<eq>3DAC84A7-AA47-E611-84A6-00155D24B70C OR '
                      'cobalt_MemberTypeId<eq>D40B84B0-EF20-E111-B470-00155D000140)',
            'Attributes': 'cobalt_contact_cobalt_membership/firstname,cobalt_contact_cobalt_membership/lastname,cobalt_contact_cobalt_membership/emailaddress1',
            'streamToken': None
        }
    else:
        payload = {
            'Key': config['API_KEY'],
            'Operation': 'GetEntities',
            'Entity': 'cobalt_membership',
            'Filter': f'cobalt_joindate<ge>{user_input} AND '
                      'statuscode<eq>1 AND '
                      'ramco_associationid<eq>D9F2A0F9-F420-E111-B470-00155D000140 AND '
                      'ramco_primarymembership<eq>true AND '
                      '(cobalt_MemberTypeId<eq>d00b84b0-ef20-e111-b470-00155d000140 OR '
                      'cobalt_MemberTypeId<eq>d20b84b0-ef20-e111-b470-00155d000140 OR '
                      'cobalt_MemberTypeId<eq>3DAC84A7-AA47-E611-84A6-00155D24B70C OR '
                      'cobalt_MemberTypeId<eq>D40B84B0-EF20-E111-B470-00155D000140)',
            'Attributes': 'cobalt_contact_cobalt_membership/firstname,cobalt_contact_cobalt_membership/lastname,cobalt_contact_cobalt_membership/emailaddress1',
            'streamToken': None
        }

    streamToken = None
else:
    print(f'This script was last run on: {timestamp_NEW}\nThe query will return NEW members since this date.')
    user_input = input("Type 'yes' to continue OR enter a different date in the format YYYY-MM-DD OR type 'reset' to return ALL members that fit the criteria: ")

    if user_input == 'yes':
        payload = {
            'Key': config['API_KEY'],
            'Operation': 'GetEntities',
            'Entity': 'cobalt_membership',
            'Filter': f'cobalt_joindate<ge>{timestamp_NEW} AND '
                      'statuscode<eq>1 AND '
                      'ramco_associationid<eq>D9F2A0F9-F420-E111-B470-00155D000140 AND '
                      'ramco_primarymembership<eq>true AND '
                      '(cobalt_MemberTypeId<eq>d00b84b0-ef20-e111-b470-00155d000140 OR '
                      'cobalt_MemberTypeId<eq>d20b84b0-ef20-e111-b470-00155d000140 OR '
                      'cobalt_MemberTypeId<eq>3DAC84A7-AA47-E611-84A6-00155D24B70C OR '
                      'cobalt_MemberTypeId<eq>D40B84B0-EF20-E111-B470-00155D000140)',
            'Attributes': 'cobalt_contact_cobalt_membership/firstname,cobalt_contact_cobalt_membership/lastname,cobalt_contact_cobalt_membership/emailaddress1',
            'streamToken': None
        }
    elif user_input == 'reset':
        payload = {
            'Key': config['API_KEY'],
            'Operation': 'GetEntities',
            'Entity': 'cobalt_membership',
            'Filter': f'statuscode<eq>1 AND '
                      'ramco_associationid<eq>D9F2A0F9-F420-E111-B470-00155D000140 AND '
                      'ramco_primarymembership<eq>true AND '
                      '(cobalt_MemberTypeId<eq>d00b84b0-ef20-e111-b470-00155d000140 OR '
                      'cobalt_MemberTypeId<eq>d20b84b0-ef20-e111-b470-00155d000140 OR '
                      'cobalt_MemberTypeId<eq>3DAC84A7-AA47-E611-84A6-00155D24B70C OR '
                      'cobalt_MemberTypeId<eq>D40B84B0-EF20-E111-B470-00155D000140)',
            'Attributes': 'cobalt_contact_cobalt_membership/firstname,cobalt_contact_cobalt_membership/lastname,cobalt_contact_cobalt_membership/emailaddress1',
            'streamToken': None
        }
    else:
        payload = {
            'Key': config['API_KEY'],
            'Operation': 'GetEntities',
            'Entity': 'cobalt_membership',
            'Filter': f'cobalt_joindate<ge>{user_input} AND '
                      'statuscode<eq>1 AND '
                      'ramco_associationid<eq>D9F2A0F9-F420-E111-B470-00155D000140 AND '
                      'ramco_primarymembership<eq>true AND '
                      '(cobalt_MemberTypeId<eq>d00b84b0-ef20-e111-b470-00155d000140 OR '
                      'cobalt_MemberTypeId<eq>d20b84b0-ef20-e111-b470-00155d000140 OR '
                      'cobalt_MemberTypeId<eq>3DAC84A7-AA47-E611-84A6-00155D24B70C OR '
                      'cobalt_MemberTypeId<eq>D40B84B0-EF20-E111-B470-00155D000140)',
            'Attributes': 'cobalt_contact_cobalt_membership/firstname,cobalt_contact_cobalt_membership/lastname,cobalt_contact_cobalt_membership/emailaddress1',
            'streamToken': None
        }

    streamToken = None


def extract_fields(json_data, fields, default_value=None):
    """Extracts the given fields from the given JSON data.

    Args:
        json_data: A JSON object or list of JSON objects.
        fields: A list of strings, where each string is a field name.
        default_value: The default value to use for missing fields.

    Returns:
        A list of lists, where each sublist is a list of values for the given fields
        for a single entry in the JSON data.
    """

    extracted_fields_list = []
    for entry in json_data:
        extracted_fields = []

        for field in fields:
            # Check if the field exists in the entry.
            if field in entry['cobalt_contact_cobalt_membership']:
                # If the field exists, extract the value.
                extracted_fields.append(entry['cobalt_contact_cobalt_membership'][field])
            else:
                # If the field does not exist, use the default value.
                extracted_fields.append(default_value)

                # Log a warning message.
                logger.warning('Field "{}" not found in entry: {}'.format(field, entry))

        extracted_fields_list.append(extracted_fields)

    return extracted_fields_list


def export_to_excel(extracted_fields_list, excel_file_path):
    """Exports the given list of fields to an Excel file (.xlsx), appending to existing file if it exists.

    Args:
        extracted_fields_list: A list of lists, where each sublist is a list of values
        for the given fields.
        excel_file_path: The path to the Excel file to export to.
    """

    # Create a DataFrame from the extracted fields list
    new_data_df = pd.DataFrame(extracted_fields_list, columns=['LastName', 'FirstName', 'EMailAddress1'])

    # Check if the file exists
    if os.path.isfile(excel_file_path):
        # Read existing data
        existing_data_df = pd.read_excel(excel_file_path)
        # Append new data using concat
        updated_df = pd.concat([existing_data_df, new_data_df], ignore_index=True)
    else:
        updated_df = new_data_df

    # Export the updated DataFrame to an Excel file
    updated_df.to_excel(excel_file_path, index=False)


current_date = datetime.now().strftime('%Y-%m-%d')

while True:
    # add the streamToken to the request payload
    payload['streamToken'] = streamToken

    print('Requesting Data from RAMCO...')
    # request data from RAMCO API
    r = requests.post(config['API_URL'], data=payload)

    # Parse the data
    data = json.loads(r.text)

    # extract the fields for each entry, using the default value of None for missing fields.
    fields = ['LastName', 'FirstName', 'EMailAddress1']
    extracted_fields_list = extract_fields(data['Data'], fields)

    # Export the extracted fields to an Excel file.
    # Split the current_date into year, month, and day
    year, month, day = current_date.split('-')

    # Create a new variable in the desired format
    formatted_currdate = f'{month}{day[0:2]}{year[2:]}'

    excel_file_path = f'export-inman-new-{formatted_currdate}.xlsx'
    export_to_excel(extracted_fields_list, excel_file_path)

    if data:
        # the query returned a result
        if 'StreamToken' in data:
            # the result set includes a `StreamToken` column
            streamToken = data['StreamToken']
            hasMoreData = True
        else:
            # the result set does not include a `StreamToken` column
            streamToken = None
            hasMoreData = False
    else:
        # the query returned no results
        streamToken = None
        hasMoreData = False

    # break the loop if there is no more data to retrieve
    if not hasMoreData:
        break

write_timestamp_NEW()
print(f'timestamp_NEW.txt updated with todays date: {current_date}')
