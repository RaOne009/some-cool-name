from flask import Blueprint, redirect, url_for, render_template, flash, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from server.db_interact import *

bp = Blueprint("auth", __name__)

@bp.route("/register", methods = ("GET", "POST"))
def register():
	if request.method == "POST":
		if request.form["choice"] == "Student":
			return redirect(url_for("auth.register_student"))
		else:
			return redirect(url_for("auth.register_admin"))
	else:
		return render_template("auth/register.html")


@bp.route("/register_student", methods = ("GET", "POST"))
def register_student():
	if request.method == "POST":
		name = request.form["name"]
		roll_number = request.form["password"]
		phone_number = request.form["phone_number"]
		password = generate_password_hash(request.form["password"])
		if roll_number_taken(roll_number):
			print("Roll number: {} already registered.".format(roll_number))
			return redirect(url_for("auth.register_student"))
		else:
			add_student(name, roll_number, phone_number, password)
			print("Student: {} registered.".format(name))
			return redirect(url_for("index"))
	else:
		return render_template("auth/register_student.html")

		
@bp.route("/register_admin", methods = ("GET", "POST"))
def register_admin():
	if request.method == "POST":
		name = request.form["name"]
		email_id = request.form["email_id"]
		password = generate_password_hash(request.form["password"])
		if email_id_taken(email_id):
			print("Email-id: {} already registered.".format(email_id))
			return redirect(url_for("auth.register_admin"))
		else:
			add_admin(name, email_id, password)
			print("Admin: {} registered.".format(name))
			return redirect(url_for("index"))
	else:
		return render_template("auth/register_admin.html")


@bp.route("/login", methods = ("GET", "POST"))
def login():
	if request.method == "POST":
		if request.form["choice"] == "Student":
			return redirect(url_for("auth.login_student"))
		else:
			return redirect(url_for("auth.login_admin"))
	else:
		return render_template("auth/login.html")


@bp.route("/login_student", methods = ("GET", "POST"))
def login_student():
	if request.method == "POST":
		roll_number = request.form["roll_number"]
		password = request.form["password"]
		user = get_student(roll_number)
		if not check_password_hash(user["password"], password):
			print("Wrong password entered.")
			return redirect(url_for("auth.login_student"))
		else:
			session.clear()
			session["type"] = "student"
			session["name"] = user['name']
			session["roll_number"] = user["roll_number"]
			session["phone_number"] = user["phone_number"]
			print("Student: {} logged in.".format(user["name"]))
			return redirect(url_for("index"))
	else:
		return render_template("auth/login_student.html")


@bp.route("/login_admin", methods = ("GET", "POST"))
def login_admin():
	if request.method == "POST":
		email_id = request.form["email_id"]
		password = request.form["password"]
		user = get_admin(email_id)
		if not check_password_hash(user["password"], password):
			print("Wrong password entered")
			return redirect(url_for("auth.login_admin"))
		else:
			session["type"] = "admin"
			session["name"] = user['name']
			session["email_id"] = user["email_id"]
			print("Admin: {} logged in.".format(user["name"]))
			return redirect(url_for("index"))
	else:
		return render_template("auth/login_admin.html")


@bp.route("/logout")
def logout():
	session.clear()
	return redirect(url_for("index"))
