import requests
import json
import csv  # Import the csv module
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.exceptions import FacebookRequestError  # Import the exception

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

my_app_id = config['app_id']
my_app_secret = config['app_secret']
my_access_token = config['access_token']

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

# Ensure you have the correct Ad Account ID
ad_account_id = 'act_10211150335726754'  # Prefix with 'act_' for Ad Account

# Initialize the Ad Account object
my_account = AdAccount(ad_account_id)

# Ensure campaigns is defined before this line
campaigns = my_account.get_campaigns()  # Example function to fetch campaigns

# Define the fields you want to retrieve
fields = [
    'id',  # Add 'id' to the fields list
    'start_time',
    'end_time',
    'name',
    'updated_time',
    'daily_budget',
    'lifetime_budget',
    'bid_amount',
    'status',
    'effective_status',
    'targeting',
    'created_time',
    'campaign_id'
]

# Open a CSV file to write the data
with open('ad_sets.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()

    # Fetch ad sets for each campaign and write the specified fields to the CSV
    for campaign in campaigns:
        ad_sets = campaign.get_ad_sets(fields=fields)
        for ad_set in ad_sets:
            writer.writerow(ad_set)