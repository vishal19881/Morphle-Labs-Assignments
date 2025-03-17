from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "ANGADI MOHAMMAD SADIQ"  
   
    username = os.environ.get('USER', 'Unknown User')  # Fallback to 'Unknown User' if not found
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST") 
    

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error retrieving 'top' output: {str(e)}"
    
    return f"""
    Name: {full_name}<br>
    User: {username}<br>
    Server Time: {server_time}<br>
    TOP output:<br><pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
