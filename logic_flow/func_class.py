from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, SubmitField

class DrugForm(FlaskForm):
    name = StringField("ป้อนชื่อของคุณ")
    age = StringField("อายุ")
    gender = RadioField("เพศ", choices=[('M','ชาย'),('F','หญิง')])
    bp = SelectField('ระดับความดันในเลือด', choices=[('HIGH','สูง'),('NORMAL','ปกติ'),('LOW','ต่ำ')])
    cholesterol = SelectField('ระดับคอเลสเตอรอล', choices=[('HIGH','สูง'),('NORMAL','ปกติ')])
    na_to_k = StringField("สัดส่วนระหว่างโซเดียมกับโพแทสเซียม")
    submit = SubmitField("บันทึก")

class CarForm(FlaskForm):
    name = StringField("ป้อนชื่อรถ")
    curbweight = StringField("น้ำหนักของรถ")
    highwaympg = StringField("ระยะทางที่ขับบนทางหลวง (ไมล์)")
    citympg = StringField("ระยะทางที่ขับบนเมือง (ไมล์)")
    carwidth = StringField("ความกว้างของรถ")
    horsepower = StringField("แรงม้า")
    enginesize = StringField("ขนาดของรถ")
    carlength = StringField("ความยาวของรถ")
    peakrpm = StringField("ความเร็วของรถสูงสุด")
    wheelbase = StringField("ขนาดฐานล้อรถ")
    boreratio = StringField("อัตราส่วนของรถ")
    submit = SubmitField("บันทึก")

def drug_class():
    form = DrugForm()
    return form

def car_class():
    form = CarForm()
    return form