from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import csv
@app.route('/')
def starter():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)

# @app.route('/about.html')
# def about():
#     return render_template('about.html')
def write_to_file(data):
    with open('database.txt', mode= 'a') as database:
        email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]
        file = database.write(f'\n {email}, {subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode= 'a') as databasecsv:
        email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]
        csv_writer = csv.writer(databasecsv, delimiter = ',',   quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        write_to_file(data)
        return redirect ('/thanks.html')
    else:
        return 'Something went wrong. Try again'

if __name__=="__main__":
    app.run(debug=True)