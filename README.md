# Streaming Finance Data with AWS Lambda
For this project, you are tasked with provisioning a Lambda function to generate near real time finance data records for interactive querying. In doing so, you will familiarize yourself with a process that you can leverage in your professional or personal endeavors that require consumption of data that is “always on” and changing very quickly, in sub-hour (and typically) sub-minute intervals.


## Part 1: Data Transformation with Lamda
In mylambda function, using the yfinance module, I will grab pricing information for each of the following stocks:
Facebook (FB). 
Shopify (SHOP). 
Beyond Meat (BYND). 
Netflix (NFLX). 
Pinterest (PINS). 
Square (SQ). 
The Trade Desk (TTD). 
Okta (OKTA). 
Snap (SNAP). 
Datadog (DDOG). 
I am to collect one full day’s worth of stock HIGH and LOW prices for each company listed above on Tuesday, December 1st 2020, at a five minute interval. Note that by “full day” we mean one day of stock trading, which is not 24 hours. I attempt to collect this data “in real time” (of course this would require usage of the Cloudwatch Events trigger on Lambda). 



## Part 2: Data Collector
For this part, I’d like the source code for my lambda function that collects the data from yfinance and puts into the firehose stream.It is proven by screeshots of my kinesis stream and my S3 folder content.




## Part 3: Data Analyzer
I will query S3 with Athena and Glue.Firstly, I will set up Glue to leverage the JSON classifier to generate a table schema for our finance streaming dataset
and point Athena to our Glue catalog as a Connector. Then, I run queries in Athena’s interactive querying shell to assert that we are indeed able to connect to and run queries against our S3 data. After run queries, it will generate a dataset which contains data that correctly identifies hourly “high” stock price per company.


## Part 4: Extra Credit
I will use the results dataset generated after run my query to create three visulizations on jupyter notebook.
