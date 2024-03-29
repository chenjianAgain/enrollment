from application4 import application
from flask import render_template, request, Response, json
from application4.models import User

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
        
    return Response(json.dumps(jData), mimetype="application/json")

@application.route("/user")
def user():
    #  User(user_id=3, first_name="Christian", last_name="Hur", email="christian@uta.com", password="abc1234").save()
    #  User(user_id=4, first_name="Mary", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
     users = User.objects.all()
     print('users: ', json.dumps(users))
    #  return Response(json.dumps(users), mimetype="application/json")
     return render_template("user.html", users=users)