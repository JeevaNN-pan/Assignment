from flask import Flask, jsonify, request
import sqlite3
import pandas as pd

app = Flask(__name__)

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('bank_branches.db')
    cursor = conn.cursor()
    
    # Create table for bank branches
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS branches (
        id INTEGER PRIMARY KEY,
        bank_name TEXT,
        branch_name TEXT,
        ifsc TEXT,
        address TEXT,
        city TEXT,
        district TEXT,
        state TEXT
    )
    ''')
    
    # Read data from CSV file
    df = pd.read_csv('bank_branches.csv')
    
    # Insert data into the database
    df.to_sql('branches', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# API endpoint to get all banks or search banks by name
@app.route('/api/banks', methods=['GET'])
def get_banks():
    bank_name = request.args.get('name')
    
    conn = sqlite3.connect('bank_branches.db')
    cursor = conn.cursor()
    
    if bank_name:
        cursor.execute("SELECT DISTINCT bank_name FROM branches WHERE bank_name LIKE ?", (f'%{bank_name}%',))
    else:
        cursor.execute("SELECT DISTINCT bank_name FROM branches")
    
    banks = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    
    if not banks:
        return jsonify({"message": "No banks found matching the criteria"}), 404
    
    return jsonify({"banks": banks})

# API endpoint to get branch details for a specific bank
@app.route('/api/branches', methods=['GET'])
def get_branches():
    bank_name = request.args.get('bank_name')
    
    if not bank_name:
        return jsonify({"error": "Bank name is required"}), 400
    
    conn = sqlite3.connect('bank_branches.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM branches WHERE bank_name=?", (bank_name,))
    branches = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
    
    conn.close()
    
    if not branches:
        return jsonify({"error": "No branches found for the given bank"}), 404
    
    return jsonify({"branches": branches})

if __name__ == '__main__':
    app.run(debug=True)