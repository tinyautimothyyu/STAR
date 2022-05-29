
from flask import Flask, render_template, request, redirect, url_for, Response

app = Flask(__name__)

# @app.route('/success/<name>')
# def success(name):
#    return 'Welcome %s' % name

# sign in
@app.route("/", methods=['GET', 'POST'])
def Sign_inPage():
    if request.method == 'POST':
        un = request.form['un']
        pw = request.form['pw']
        print(un, pw)
        return redirect(url_for('Check_inPage'))
        # return render_template('check_in.html', famMembers=famMembers)
    return render_template('sign_in.html')


# # register
# @app.route("/register", methods=['GET', 'POST'])
# def RegisterPage():
#     return render_template('register.html')

# check in
@app.route("/check_in", methods=['GET', 'POST'])
def Check_inPage():
    famMembers = ['Fiona','Nicky','Joe']  # collect the names of the family member of the account from database
    if request.method == 'POST':
        print(list(request.form.values()))  # list of names who checked in
        # Send the list of names to the database and append the check-in date and time to the date array of each member
        return redirect(url_for('Successful'))
        # return render_template('successful.html')
    return render_template('check_in.html', famMembers=famMembers)


@app.route("/register", methods=['GET', 'POST'])
def RegisterPage():

    if request.method == 'POST':
        pFName = request.form['First Name']
        pLName = request.form['Last Name']
        pPhone = request.form['Phone']
        pEmail = request.form['Email Address']
        print(pFName,pLName,pPhone,pEmail)
        # Check if there is any duplicate account
        # Create an account for this User
        if request.form['button'] == 'Submit':
            return redirect(url_for('Sign_inPage'))
        elif request.form['button'] == 'Add Family Member':
            return redirect(url_for('RegisterPage_add'))
        else:
            pass
        
    return render_template('register.html')

@app.route("/register/add", methods=['GET', 'POST'])
def RegisterPage_add():
    if request.method == 'POST':
        FName = request.form['First Name']
        LName = request.form['Last Name']
        print(FName,LName)
        if request.form['button'] == 'submit':
            return redirect(url_for('Sign_inPage'))
        elif request.form['button'] == 'add':
            return render_template('add.html') 
        else:
            pass
              
    return render_template('add.html')

# successful
@app.route("/successful", methods=['GET', 'POST'])
def Successful():
    if request.method == 'POST':
        return redirect(url_for('Sign_inPage'))
        # return render_template('sign_in.html')
    return render_template('successful.html')




if __name__ == '__main__':
        app.run(debug=True)