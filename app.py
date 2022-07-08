from flask import Flask,render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "1234"


@app.route("/")
def hello_world():
    name="Pablo"
    session["my name"]= name
    return "<h1>Hello, Python!</h1>"

@app.route("/aboutme/")
def aboutme():
    return render_template("about_me_content.html")

@app.route("/registration/", methods=["GET","POST"])
def registration():
    if request.method == "GET":
        return render_template("registration.html")
    elif request.method == "POST":
        users = {"User1@gmail.com":"password1","User2@gmail.com":"password2"}
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        age=request.form.get("age")
        gender=request.form.get("radio")
        language=request.form.get("language")
        about=request.form.get("about")
        if email in users.keys():
            message="email already exists"
            return render_template("registration.html", result = message)
        elif email not in users.keys():
            message = "Hi "+email+" your registration was successful"
            session["email"]=email
            session["password"]=password
            return render_template("login.html", result=message)

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form.get("login_email")
        password = request.form.get("login_password")
        email_session = session.get("email")
        password_session = session.get("password")
        name=session.get("my name", "abc")
        if email == email_session and password == password_session:
            message = "Hi "+ name +" login was successful"
            session["login"]=True
            return render_template("q1.html", message=message)
        else:
            message = "Either password or email is incorrect"
            return render_template("login.html", message = message)

@app.route("/logout/")
def logout():
    session.clear()
    return render_template("login.html", result="You have successfully logged out")



@app.route("/q1/", methods=["GET", "POST"])
def q1():
    counter_attempted = session.get("counter_attempted", 0)
    count_correct = session.get("count_correct", 0)
    count_incorrect = session.get("count_incorrect", 0)
    if request.method == "GET":
        return render_template("q1.html")
    elif request.method == "POST":
        user_action = request.form.get("q1")
        correct_answer = "2"
        counter_attempted += 1
        session["counter_attempted"]= counter_attempted
        if user_action == correct_answer:
            message="Correct Answer"
            count_correct += 1
            session["count_correct"] = count_correct
        else:
            message="Wrong Answer"
            count_incorrect += 1
            session["count_incorrect"] = count_incorrect
    return render_template("q1.html",message=message)
@app.route("/q2/", methods=["GET","POST"])
def q2():
    counter_attempted = session.get("counter_attempted", 0)
    count_correct = session.get("count_correct", 0)
    count_incorrect = session.get("count_incorrect", 0)
    if request.method == "GET":
        return render_template("q2.html")
    elif request.method == "POST":
        user_action = request.form.get("q2")
        correct_answer= "2"
        counter_attempted += 1
        session["counter_attempted"]=counter_attempted
        if user_action == correct_answer:
            message = "Correct Answer"
            count_correct += 1
            session["count_correct"]= count_correct
        else:
            message="Wrong Anwer"
            count_incorrect += 1
            session["count_incorrect"] = count_incorrect
        return render_template("q3.html", message=message) 

@app.route("/q3/", methods = ["GET", "POST"])
def q3():
    counter_attempted = session.get("counter_attempted", 0)
    count_correct = session.get("count_correct", 0)
    count_incorrect = session.get("count_incorrect", 0)
    if request.method == "GET":
        return render_template("q3.html")
    elif request.method == "POST":
        user_action = request.form.get("q3")
        correct_answer = "3"
        counter_attempted += 1
        session["counter_attempted"]=counter_attempted
        if user_action == correct_answer:
            message = "Correct Answer"
            count_correct += 1
            session["count_correct"]= count_correct
        else:
            message="Wrong Anwer"
            count_incorrect += 1
            session["count_incorrect"] = count_incorrect
        return render_template("q3.html", message=message) 

@app.route("/q4/", methods = ["GET", "POST"])
def q4():
    counter_attempted = session.get("counter_attempted", 0)
    count_correct = session.get("count_correct", 0)
    count_incorrect = session.get("count_incorrect", 0)
    if request.method == "GET":
        return render_template("q4.html")
    elif request.method == "POST":
        user_action = request.form.get("q4")
        correct_answer = "1"
        counter_attempted += 1
        session["counter_attempted"]=counter_attempted
        if user_action == correct_answer:
            message = "Correct Answer"
            count_correct += 1
            session["count_correct"]= count_correct
        else:
            message="Wrong Anwer"
            count_incorrect += 1
            session["count_incorrect"] = count_incorrect
        return render_template("q4.html", message=message) 

@app.route("/q5/", methods = ["GET", "POST"])
def q5():
    counter_attempted = session.get("counter_attempted", 0)
    count_correct = session.get("count_correct", 0)
    count_incorrect = session.get("count_incorrect", 0)
    if request.method == "GET":
        return render_template("q5.html")
    elif request.method == "POST":
        user_action = request.form.get("q5")
        correct_answer = "1"
        counter_attempted += 1
        session["counter_attempted"]=counter_attempted
        if user_action == correct_answer:
            message = "Correct Answer"
            count_correct += 1
            session["count_correct"]= count_correct
        else:
            message="Wrong Anwer"
            count_incorrect += 1
            session["count_incorrect"] = count_incorrect
        return render_template("q5.html", message=message)

@app.route("/q6/", methods = ["GET", "POST"])
def q6():
    counter_attempted = session.get("counter_attempted", 0)
    count_correct = session.get("count_correct", 0)
    count_incorrect = session.get("count_incorrect", 0)
    if request.method == "GET":
        return render_template("q6.html")
    elif request.method == "POST":
        user_action = request.form.get("q6")
        correct_answer = "4"
        counter_attempted += 1
        session["counter_attempted"]=counter_attempted
        if user_action == correct_answer:
            message = "Correct Answer"
            count_correct += 1
            session["count_correct"]= count_correct
        else:
            message="Wrong Anwer"
            count_incorrect += 1
            session["count_incorrect"] = count_incorrect
        return render_template("q6.html", message=message)

@app.route("/q7/", methods = ["GET", "POST"])
def q7():
    counter_attempted = session.get("counter_attempted", 0)
    count_correct = session.get("count_correct", 0)
    count_incorrect = session.get("count_incorrect", 0)
    if request.method == "GET":
        return render_template("q7.html")
    elif request.method == "POST":
        user_action = request.form.get("q7")
        correct_answer = "2"
        counter_attempted += 1
        session["counter_attempted"]=counter_attempted
        if user_action == correct_answer:
            message = "Correct Answer"
            count_correct += 1
            session["count_correct"]= count_correct
        else:
            message="Wrong Anwer"
            count_incorrect += 1
            session["count_incorrect"] = count_incorrect
        return render_template("q7.html", message=message)

@app.route("/q8/", methods = ["GET", "POST"])
def q8():
    counter_attempted = session.get("counter_attempted", 0)
    count_correct = session.get("count_correct", 0)
    count_incorrect = session.get("count_incorrect", 0)
    if request.method == "GET":
        return render_template("q8.html")
    elif request.method == "POST":
        user_action = request.form.get("q8")
        correct_answer = "1"
        counter_attempted += 1
        session["counter_attempted"]=counter_attempted
        if user_action == correct_answer:
            message = "Correct Answer"
            count_correct += 1
            session["count_correct"]= count_correct
        else:
            message="Wrong Anwer"
            count_incorrect += 1
            session["count_incorrect"] = count_incorrect
        return render_template("q8.html", message=message)

@app.route("/q9/", methods = ["GET", "POST"])
def q9():
    counter_attempted = session.get("counter_attempted", 0)
    count_correct = session.get("count_correct", 0)
    count_incorrect = session.get("count_incorrect", 0)
    if request.method == "GET":
        return render_template("q9.html")
    elif request.method == "POST":
        user_action = request.form.get("q9")
        correct_answer = "2"
        counter_attempted += 1
        session["counter_attempted"]=counter_attempted
        if user_action == correct_answer:
            message = "Correct Answer"
            count_correct += 1
            session["count_correct"]= count_correct
        else:
            message="Wrong Anwer"
            count_incorrect += 1
            session["count_incorrect"] = count_incorrect
        return render_template("q9.html", message=message)

@app.route("/q10/", methods = ["GET", "POST"])
def q10():
    counter_attempted = session.get("counter_attempted", 0)
    count_correct = session.get("count_correct", 0)
    count_incorrect = session.get("count_incorrect", 0)
    if request.method == "GET":
        return render_template("q10.html")
    elif request.method == "POST":
        user_action = request.form.get("q10")
        correct_answer = "1"
        counter_attempted += 1
        session["counter_attempted"]=counter_attempted
        if user_action == correct_answer:
            message = "Correct Answer"
            count_correct += 1
            session["count_correct"]= count_correct
        else:
            message="Wrong Anwer"
            count_incorrect += 1
            session["count_incorrect"] = count_incorrect
        return render_template("q10.html", message=message)

@app.route("/qdata/")
def qdata():
    return render_template("qdata.html")

@app.route("/leaderboard/")
def leaderboard():
    return render_template("leaderboard.html")

#------------------ end of project -----------------------


# ---------------- practice programs ---------------------

@app.route("/chr_count/", methods=["GET","POST"])
def chr_count():
    if request.method == "GET":
        return render_template("chr_count.html")
    elif request.method == "POST":
        str1=request.form.get("user_text")
        upper_count=0
        lower_count=0
        for i in str1:
            if ord(i) >= 65 and ord(i) <= 90:
                upper_count += 1
            elif ord(i) >= 97 and ord(i) <= 122:
                lower_count += 1
        final="Number of uppercase letters = " + str(upper_count)
        final2="Number of lowercase letters = " + str(lower_count)
        result= final+" "+" "+final2
        return render_template("chr_count.html", result=result)

@app.route("/even_odd1/")
def even_odd1():
    return render_template("even_odd.html")
@app.route("/even_odd/")
def even_odd():
    string1=int(request.args.get("user_str"))
    if string1 % 2 == 0:
        result = "The number is even"
    elif string1 % 2 == 1:
        result = "The number is odd"
    return render_template("even_odd.html", result=result)

@app.route("/max_num1/")
def max_num1():
    return render_template("max_num.html")

@app.route("/max_num/")
def max_num():
    str1=int(request.args.get("num1"))
    str2=int(request.args.get("num2"))
    str3=int(request.args.get("num3"))
    max_numbers=[]
    max_numbers.append(str1)
    max_numbers.append(str2)
    max_numbers.append(str3)
    result = max(max_numbers)
    return render_template("max_num.html", result=result)

@app.route("/rev_str1/")
def rev_str1():
    return render_template("rev_str.html")

@app.route("/rev_str/")
def rev_str():
    string=request.args.get("string")
    reverse=""
    for i in string:
        reverse=i+reverse
    return render_template("rev_str.html", reverse=reverse)

@app.route("/certificate_input/")
def certificate_input():
    return render_template("certificate_input.html")

@app.route("/certificate/")
def certificate():
    name=request.args.get("name")
    date=request.args.get("date")
    return render_template("certificate.html", name=name, date=date)

@app.route("/marks/")
def marks():
    return render_template("marks.html")

@app.route("/grades/")
def grades():
    subject1=request.args.get("subject1")
    subject2=request.args.get("subject2")
    subject3=request.args.get("subject3")
    subject4=request.args.get("subject4")
    subject5=request.args.get("subject5")
    result = ""
    total=int(subject1)+int(subject2)+int(subject3)+int(subject4)+int(subject5)
    average= total/5
    if average >= 90:
        result = "A"
    elif average >= 80:
        result = "B"
    elif average >= 70:
        result = "C"
    elif average >= 60:
        result = "D"
    elif average >= 0:
        result = "F"
    message="Your grade is a "+result
    return render_template("grades.html", result=message)

@app.route("/month/")
def month():
    return render_template("month.html")

@app.route("/days/")
def days():
    month=request.args.get("month")
    month=month.capitalize()
    days31=["January","March","May","July", "August", "October", "December"]
    days30=["April","June", "September","November"]
    days28=["February"]
    days = ""
    if month in days31:
        days = "31"
    elif month in days30:
        days = "30"
    elif month in days28:
        days = "28"
    message = "There are "+days+" days in "+month
    return render_template("days.html", days=message)

@app.route("/calculator_input/")
def calculator_input():
    return render_template("calculator_input.html")

@app.route("/calculator/")
def calculator():
    value1=int(request.args.get("value_1"))
    value2=int(request.args.get("value_2"))
    operator=request.args.get("operator")
    operation = {"Addition":"+", "Subtraction":"-", "Multiplication":"*", "Division":"/"}
    if operator == "Addition":
        result = value1 + value2
    elif operator == "Subtraction":
        result = value1 - value2
    elif operator == "Multiplication":
        result = value1 * value2
    elif operator == "Division":
        if value2 == 0:
            result = "You cannot divide a number by zero"
            return render_template("calculator.html", equation=result)
        result = value1 / value2
    message = str(value1) + " " + operation[operator] + " " + " " + str(value2) + " " + "=" + " " +str(result)
    return render_template("calculator.html", equation=message)




if __name__=="__main__":
    app.run(debug=True)
