from application3 import application
from flask import render_template, request, Response, json

courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]


@application.route("/")
@application.route("/index")
@application.route("/home")
@application.route("/joseph")
def index():
    return render_template("index.html", index=True)

@application.route("/denglu")
def login():
    return render_template("login.html", login=True)

@application.route("/kecheng/")
@application.route("/kecheng/<term>")
def courses(term="Spring 2019"):
    print(courseData[0]["title"])
    return render_template("courses.html", courses=True, courseData=courseData, term=term)

@application.route("/zhuce")
def register():
    return render_template("register.html", register=True)
    
@application.route("/enrollment", methods=["GET","POST"])
def enrollment():
    id = request.form.get('courseID')
    print(id)
    
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html", data={ "id": id, "title": title, "term": term })

@application.route("/api/")
@application.route("/api/<idx>")
def api(idx=None):
    if idx == None:
        jData = courseData
    else:
        jData = courseData[int(idx)]
        
    return Response(json.dump(jData), mimetype="application/json")