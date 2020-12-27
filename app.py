
from  flask import Flask , render_template , request , redirect

import gspread  

gc = gspread.service_account(filename="cred.json")

sh = gc.open_by_key('1NJdDbyOGT0aZJcmueUGjGqiu3P6rqhPy37-NMOE73Yg')

worksheet = sh.sheet1

app = Flask(__name__)


@app.route('/',methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        #print(name , email , subject , message)
        full_data = []
        full_data.extend([name , email , subject,message])
        worksheet.insert_row(full_data)
        full_data.clear()
        #print(full_data)
    return render_template('index.html')




if __name__ == "__main__":
    app.run()
    
