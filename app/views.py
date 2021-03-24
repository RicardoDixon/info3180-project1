from app import app, db
from flask import render_template, request, url_for, redirect, flash, send_from_directory
from .forms import Form
from werkzeug.utils import secure_filename
from .models import Property
from sqlalchemy import exc

import datetime
import os

@app.route("/")
def home():
    return render_template('home.html')
    
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')   
    
@app.route("/property", methods=["GET", "POST"])
def property():
    PptyForm = Form()
    
    if request.method == "POST":
        
        if  PptyForm.validate_on_submit():
            
                title =  PptyForm.title.data
                description = PptyForm.description.data
                number_of_bedrooms = PptyForm.number_of_bedrooms.data
                number_of_bathrooms = PptyForm.number_of_bathrooms.data
                location = PptyForm.location.data
                price = PptyForm.price.data
                ptype = PptyForm.ptype.data
                photo = PptyForm.photo.data
                photofilename = secure_filename(photo.filename)
                
                pH = Property(title,description,number_of_bedrooms,number_of_bathrooms,price,location,ptype,photofilename)
                
                db.session.add(pH)
                db.session.commit()
                
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'],photofilename))
                
                flash("Profile Added", "success")
                return redirect(url_for("properties"))
            
            
        errors = form_errors(PptyForm)
        flash(''.join(error+" " for error in errors), "danger")
    return render_template("new_property.html", PptyForm = PptyForm)


@app.route("/properties")
def properties():
    properties_h = Property.query.all()
    properties = []
    
    for propertyH  in properties_h:
        properties.append({"title":propertyH.title, "price":propertyH.price, "location":propertyH.location, "photo":propertyH.photo, "id":propertyH.id})
    
    return render_template("view_all_properties.html", properties = properties)

@app.route('/property/<propertyid>')
def i_property(propertyid):
    pH  = Property.query.filter_by(id=propertyid).first()
    
    if pH  is None:
        return redirect(url_for('home'))
    
    return render_template("property.html", pH=pH)

@app.route('/uploads/<filename>')
def get_image(filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FILES_DIR = os.path.abspath(os.path.join(BASE_DIR, app.config['UPLOAD_FOLDER']))
    return send_from_directory(FILES_DIR, filename, as_attachment =True)
    


def read_file(filename):
    data = ""
    
    with open(filename, "r") as stream:
        data = stream.read()
        
    return data

def form_errors(form):
    error_list =[]
    for field, errors in form.errors.items():
        for error in errors:
            error_list.append(field+": "+error)
            
    return error_list
    
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
