import json
import yfinance as yf
import datetime
import boto3
import sys

def lambda_handler(event, context):
    
    # Initialize boto3 client
    kinesis = boto3.client("kinesis", "us-east-2")
    
    # Define required variables and arrays for compamny stocks we will analyze
    sdate = '2020-12-01'
    edate = '2020-12-02'
    granuality = '5m'
    tickers = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
    
    # Fetch stock values for each company
    for ticker in range(len(tickers)):
        records = yf.download(tickers[ticker], start = sdate, end = edate, interval = granuality)
        data = []
        
        # Cleaning the data and store them as a dict
        for i in range(len(records)):
            output = {"high":records['High'][i],"low":records['Low'][i],"ts":records.index[i].strftime('%m/%d/%Y %X'),"name":tickers[ticker]}
            
            # Convert the data into JSON
            as_jsonstr = json.dumps(output)+"\n"
            kinesis.put_record(
                StreamName="sta9760stream2",
                Data=as_jsonstr,
                PartitionKey="partitionkey")
            data.append(output)

    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {as_jsonstr}')
    }

