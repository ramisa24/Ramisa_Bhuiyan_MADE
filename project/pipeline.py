import pandas as pd
import sqlite3
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# URLs for the datasets
crime_data_url = "https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD"
arrest_data_url = "https://data.lacity.org/api/views/amvf-fr72/rows.csv?accessType=DOWNLOAD"

# Function to process crime data
def process_crime_data(url):
    
    df = pd.read_csv(url)  # Download CSV data from the URL

    # Select relevant columns for analysis
    df_selected = df[['Crm Cd Desc', 'Date Rptd', 'Vict Sex', 'LOCATION', 'AREA NAME', 'DR_NO']]

    # Clean data (remove rows with missing important values)
    df_selected = df_selected.dropna(subset=['Crm Cd Desc', 'Date Rptd', 'AREA NAME'])

    # Save to SQLite
    conn = sqlite3.connect('data/crime_data.db')
    df_selected.to_sql('crime_data', conn, if_exists='replace', index=False)
    conn.close()

    print("Processed and saved crime data.")

# Function to process arrest data
def process_arrest_data(url):
    
    df = pd.read_csv(url)  # Download CSV data from the URL

    # Select relevant columns for analysis
    df_selected = df[['Charge', 'Arrest Date', 'Arrest Type Code', 'Charge Description', 'Location', 'Area Name', 'Report ID']]

    # Clean data (remove rows with missing important values)
    df_selected = df_selected.dropna(subset=['Charge Description', 'Arrest Date', 'Area Name'])

    # Save to SQLite
    conn = sqlite3.connect('data/arrest_data.db')
    df_selected.to_sql('arrest_data', conn, if_exists='replace', index=False)
    conn.close()

    print("Processed and saved arrest data.")



def main():
    # Process both datasets
    process_crime_data(crime_data_url)
    process_arrest_data(arrest_data_url)


if __name__ == '__main__':
    main()
