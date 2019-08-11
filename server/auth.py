import functools
from flask import Blueprint, redirect, url_for, render_template, flash, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from server.db import get_db

bp = Blueprint("auth", __name__, url_prefix = "/auth")

@bp.route("/register", methods = ("GET", "POST"))
def register():
	if request.method == "POST":
		name = request.form["name"]
		password = request.form["password"]
		db = get_db()
		error = None
		if not name:
			error = "Name is required"
		elif not password:
			error = "Password is required"
		elif db.execute("""
			SELECT id FROM student WHERE name = ?
		""", (name, )).fetchone() is not None:
			error = "User {} is already registered".format(name, )
		if error is None:
			print("{} registered.".format(request.form["user_name"]))
			return redirect(url_for("index"))
		else:
			flash(error)
			return redirect(url_for("auth/register"))
	else:
		return render_template("auth/register.html")

@bp.route("/login", methods = ("GET", "POST"))
def login():
	if request.method == "POST":
		print("{} logged in.".format(request.form["user_name"]))
		return redirect(url_for("index"))
	else:
		return render_template("auth/login.html")

@bp.route("/logout")
def logout():
	session.clear()
	return redirect(url_for("index"))
