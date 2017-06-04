# Create analysis data to MongoDB

This script execute analysis data insert to MongoDB.

# Hot to use

	1. Execute the following command with MongoDB running.
	    python create_analysis_collection.py
	    
This script assumes that MongoDB is running on the local host.<br>
If your environment does not match this, you need to rewrite the script to match your MongoDB environment.

# Result after execution

This script creates two collections **"analysis"** and **"analysis_user _count"** in MongoDB.<br>
It serves as a dedicated collection to use for data analysis.
