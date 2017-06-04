# Data insert to MongoDB


This script execute slack log data insert to MongoDB.

# Hot to use

	1. get slack log zip file => example : https://my.slack.com/services/export
	2. unzip downloaded file 
	3. Run this script. 

	python mongo_import_slack_log.py your_slack_log_data
	
	---The directory structure at the time of execution should be as follows---
	mongo_import_slack_log.py
	your_slack_log_data(unzip directory)/logdata...
					    /logdata...

# Result after execution

All log data is inserted into MongoDB while keeping the json level.
