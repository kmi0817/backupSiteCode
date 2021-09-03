from app import app
from flask import render_template, redirect, jsonify, session, request, url_for
from app.models import Test, User, Comment

import sys
faberId = "id"

@app.route("/")
def index() :
    test = Test.query.all()
    
    output = []
    for t in test :
        output.append({"id": t.id, "title": t.title, "release_year": t.release_year, "rating": t.rating})

    return render_template("index.html", datatable=output)

@app.route("/repositories")
def repositories() :
    return render_template("repositories.html")

@app.route("/invitation")
def invitation() :
    if "invitation" in session :
        print("invitation: " + faberId, file=sys.stdout)
        return render_template("invitation.html", invitation=True)
    else :
        return render_template("invitation.html", invitation=False)

@app.route("/credential")
def credential() :
    if "invitation" in session :
        return render_template("credential.html", invitation=True)
    else :
        return render_template("credential.html", invitation=False)
        
@app.route("/processCreateInvitation", methods=["POST"])
def processCreateInvitation() :
    session["invitation"] = True
    faberId = request.form.get("faberId")
    global aliceId
    aliceId = request.form.get("aliceId")

    return redirect(url_for("invitation"))

@app.route("/processDeleteInvitation", methods=["POST"])
def processDeleteInvitation():
    session.pop("invitation", None)
    return redirect(url_for("invitation"))
    
@app.route("/webix-layout")
def webix() :
    return render_template("webix_layout.html")




# 데이터 부분 #
@app.route("/test")
def get_tests() :
    test = Test.query.all()
    
    output = []
    for t in test :
        output.append({"id": t.id, "title": t.title, "release_year": t.release_year, "rating": t.rating})

    return jsonify(output)
    # return {"test" : output}

@app.route("/comment")
def get_comment1() :
    return render_template("comment.html")

@app.route("/comments")
def get_comments() :
    comments = Comment.query.all()

    output = []
    for c in comments :
        created_at = c.created_date.strftime("%Y-%m-%d %H:%M")
        output.append({"id": c.id, "user_id": c.user_id, "date": created_at, "text": c.content})
    return jsonify(output)

@app.route("/users")
def get_users() :
    users = User.query.all()

    output = []
    for u in users :
        if u.image :
            output.append({"id": u.id, "value": u.name, "image": u.image})
        else :
            output.append({"id": u.id, "value": u.name})
    return jsonify(output)

