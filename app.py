from flask import FLASK , request,render_template

from certificates.certificate import cerf

app=FLASK(__name__)

@app.route("/")
def index():
  return render_template('certificate_form.html')

@app.route("/certificate_form.html",methods='POST')
def generate():
  name = request.form.get('name')
  course = request.form.get('course')
  all_classes = request.form.get('all_classes')
  all_assignments = request.form.get('all_assignment')
  certificate= cerf(name,course,all_classes,all_assignments)
  dicts=certificate.generate_certificate()
  name=dicts['name']
  course=dicts['course']
  if all_classes=='yes' and all_assignments=='yes':
    return render_template('generate.html',name=name,course=course)
  
  else:
    return render_template('not_complited.html')
  




