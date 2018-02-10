from flask import Flask, render_template

app=Flask(__name__)
    #if you call this script from another script, __name__ is set to script1

@app.route('/') #this is a python decorator
def home(): #must write a function after the decorator above
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template('about.html')




if __name__=="__main__":
    #since we are calling this script, the internal reference is __main__
    app.run(debug=True)
