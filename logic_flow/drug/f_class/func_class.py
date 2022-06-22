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

def drug_class():
    form = DrugForm()
    return form