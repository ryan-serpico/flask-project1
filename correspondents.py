from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from data import CORRESPONDENTS

app = Flask(__name__)

# This is just something that Bootstrap needs.
Bootstrap(app)

# If you use what follows, you don't have to use a CDN. You can just use the Bootstrap that's installed in the env
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

# This grabs all of the names from data.py and sorts them into a list.
def get_ids_and_names(source):
    ids_and_names = []
    for row in source:
        id = row["ID"]
        name = row["Name"]
        ids_and_names.append([id, name])
    return ids_and_names


# This function finds the row that matches the id passed to it from your function from your detail page down below and uses it to grab the name, title and years.
def get_corr(source, id):
    for row in source:
        # Note to future Ryan: Don't capitalize ID, dummy. It just makes things a little confusing.
        if id == str( row["ID"] ):
            name = row["Name"]
            title = row["Title"]
            years = row["Year(s)"]
            id = str(id)
            return id, name, title, years


# This is for the list of names when you first load up the first page
@app.route('/')
@app.route('/index.html')
def index():
    ids_and_names = get_ids_and_names(CORRESPONDENTS)
    return render_template('index.html', pairs=ids_and_names)

# This is for the detail pages
# In the future, make sure you have an HTML template ready to go before you reach this step, and don't forget that you need to use render_template for anything to happen.
@app.route('/correspondent/<id>')
def correspondent(id):
    id, name, title, years = get_corr(CORRESPONDENTS, id)
    return render_template('correspondent.html', name=name, title=title, years=years)



# Debugging stuff
if __name__ == '__main__':
    app.run(debug=True)
