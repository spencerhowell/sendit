from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
import Senator
import findState
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
#    STATES = [("1","Alabama"),("2","Alaska"),("3","Arizona"),("4","Arkansas"),("5","California"),("6","Colorado"),("7","Connecticut"),("8","Delaware"),("9","Florida"),("10","Georgia"),("Hawaii","Hawaii"),("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode","Rhode"),("Island","Island"),("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming")]
#    state = SelectField('State:', choices=STATES)
 
def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    print("Hello world!")
    form = ReusableForm(request.form)

    state = findState.getState()
    print("We are in " + state)
        
    ourSenate = Senator.Senate(100, None)
    ourSenate.populateFromCSV()
    
    
    senators = ourSenate.findSenators(state)
    senatorOne = senators.getSenatorNum(1)
    senatorTwo = senators.getSenatorNum(2)
#    print(senatorOne.name + " " + senatorTwo.name)
 
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
#        state = request.form['state']
        print name
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
            return render_template('results.html', s1=senatorOne, s2=senatorTwo)
        else:
            flash('All the form fields are required.')
 
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run()