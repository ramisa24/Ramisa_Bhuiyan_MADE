import os
import sqlite3


crime_data_path = "data/crime_data.db"
arrest_data_path = "data/arrest_data.db"

def test_pipeline_output_files():
    
    assert os.path.exists(crime_data_path), f"Missing output file: {crime_data_path}"
    assert os.path.exists(arrest_data_path), f"Missing output file: {arrest_data_path}"

def test_crime_data_table():
   
    conn = sqlite3.connect(crime_data_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='crime_data';")
    result = cursor.fetchone()
    conn.close()
    assert result is not None, "Table 'crime_data' does not exist in the database."

def test_arrest_data_table():
    
    conn = sqlite3.connect(arrest_data_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='arrest_data';")
    result = cursor.fetchone()
    conn.close()
    assert result is not None, "Table 'arrest_data' does not exist in the database."

if __name__ == "__main__":
    # Run tests
    test_pipeline_output_files()
    test_crime_data_table()
    test_arrest_data_table()
    print("All tests passed!")
