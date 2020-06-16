# Canidate Website Scraper

This scrapper retrieves candidate websites given a csv of candidate names and the office they're running for.

## Set up
1. `git clone` repo
2. `cd` into root dir of repo
3. `python3 -m venv venv` to create python virtualenv
4. `source venv/bin/activate` to activate the virtualenv
5. `pip3 install -r requirements.txt` to install all the requirements
6. Add an `input.csv` with the candidate, district, office to the current dirctory
6. `python3 search.py` to run scrapper and output a csv named `outpyt.csv` in the same directory as `search.py`


### Input csv format
- headers: candidate,district,office
- columns:
	- candidate name
	- district
	- office
- district column is ONLY included for easy copy/pasting; it's ignored in the scraper

### Output csv format
- no headers
- columns:
	- candidate name
	- district
	- office
	- website
- district column is ONLY included for easy copy/pasting; it's ignored in the scraper

### Add websites to google docs
1. Go to google sheet document
2. Click `File > Import > Upload`
3. Upload the `output.csv`
4. Select the appropriate import options you want & import the csv!
