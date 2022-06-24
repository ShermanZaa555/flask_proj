from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap

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
    from logic_flow.func_class import drug_class
    from ml_service.drug.run_drug import input_data
    
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

@app.route('/car_price', methods=['GET', 'POST'])
def car_price():
    from logic_flow.func_class import car_class
    from ml_service.car_price.run_car import input_data

    form = car_class()
    if form.validate_on_submit():
        session['name'] = form.name.data

        session['curbweight'] = form.curbweight.data
        session['highwaympg'] = form.highwaympg.data
        session['citympg'] = form.citympg.data
        session['carwidth'] = form.carwidth.data
        session['horsepower'] = form.horsepower.data
        session['enginesize'] = form.enginesize.data
        session['carlength'] = form.carlength.data
        session['peakrpm'] = form.peakrpm.data
        session['wheelbase'] = form.wheelbase.data
        session['boreratio'] = form.boreratio.data

        session['result'] = input_data(session['curbweight'], session['highwaympg'], session['citympg'], session['carwidth'], session['horsepower'],
                                       session['enginesize'], session['carlength'], session['peakrpm'], session['wheelbase'], session['boreratio'])
        
        form.curbweight.data = ''
        form.highwaympg.data = ''
        form.citympg.data = ''
        form.carwidth.data = ''
        form.horsepower.data = ''
        form.enginesize.data = ''
        form.carlength.data = ''
        form.peakrpm.data = ''
        form.wheelbase.data = ''
        form.boreratio.data = ''
    return render_template("car_price.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)