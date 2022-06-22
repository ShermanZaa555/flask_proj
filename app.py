from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap

from logic_flow.drug.f_class.func_class import drug_class
from ml_service.drug.run_drug import input_data
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/drug', methods=['GET', 'POST'])
def drug():
    
    form = drug_class()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['age'] = form.age.data
        session['gender'] = form.gender.data
        session['bp'] = form.bp.data
        session['cholesterol'] = form.cholesterol.data
        session['na_to_k'] = form.na_to_k.data

        session['result'] = input_data(session['age'], session['gender'], session['bp'], session['cholesterol'], session['na_to_k'])

        form.name.data = ''
        form.age.data = ''
        form.gender.data = ''
        form.bp.data = ''
        form.cholesterol.data = ''
        form.na_to_k.data = ''
    return render_template("drug.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)