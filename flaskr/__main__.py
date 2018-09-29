from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        print name
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')
 
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run()
We then create the template hello.html in the /templates/ directory:

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
    <head>
        <title>Reusable Form Demo</title>
    </head>
    <body>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message[1] }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
        <form action="" method="post">
            {{ form.csrf }}
 
            <div class="input text">
                {{ form.name.label }} {{ form.name }}
            </div>
 
            <div class="input submit">
                <input type="submit" value="Submit" />
            </div>
        </form>
    </body>
</html>