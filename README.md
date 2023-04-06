# Instructions for starting webapp
All of the commands below must be ran from the workingdir folder. This project was done on the Ubuntu Linux
distribution, but steps to run this project on Windows are also included.

Setting up environment
1. Create a virtual environment using: python3.8 -m venv venv (python -m venv venv if on Windows)
2. Activate the environment using:  source venv/bin/activate (venv/Scripts/activate if on Windows)
3. Install the required libraries/modules using: pip install -r requirements.txt
4. If on Windows, sqlite3 will need to be installed. https://www.tutorialspoint.com/sqlite/sqlite_installation.htm

Uploading data to SQLite serverless database
1. Run the database_upload.py file using: python database.upload.py

Running the web app
1. Use: flask --app test_app run 
2. CRTL + left click on the url given to be taken to the index page

Accessing the data
1. Once you're taken to the initial page, add to the end of the base url /data 
2. Click on the "Select Data" button to choose the data for the Y axis
3. Click on "Select Data" again to collapse the dropdown
4. Choose a beginning and/or end date to filter the data according to date and hit the filter button

# Next Steps

1. create a proper base page to extend to additional pages (and create a home page). Try to get creative with what to add
2. work with some frameworks. Look into Angular, React, Vue.Js
3. improve performance, work with JavaScript a bit more
4. look into optimising the web app for better performance & security
5. find some additional fun data to work with to make the project more realistic