from flask import Blueprint, render_template, request, redirect, url_for
from server.db_interact import *

bp = Blueprint("test", __name__)

@bp.route("/create_test", methods = ("GET", "POST"))
def create_test():
	if request.method == "POST":
		name = request.form["name"]
		start_time = request.form["start_time"]
		duration = request.form["duration"]
		add_test(name, start_time, duration)
		print("Test {} added.".format(name))
		return redirect(url_for("test.tests"))
	else:
		return render_template("test/create_test.html")
		

@bp.route("/tests/")
def tests():
	all_tests = get_all_tests()
	return render_template("test/tests.html", all_tests = all_tests)
	
	
@bp.route("/edit_test/<int:test_id>/", methods = ("GET", "POST"))
def edit_test(test_id):
	test = get_test(test_id)
	if request.method == "POST":
		name = request.form["name"]
		start_time = request.form["start_time"]
		duration = request.form["duration"]
		update_test(test_id, name, start_time, duration)
		print("Test {} updated.".format(name))
		return redirect(url_for("test.tests"))
	else:
		return render_template("test/edit_test.html", test = test)
		

@bp.route("/test/<int:test_id>/question/<int:question_id>", methods = ("GET", "POST"))
def test(test_id, question_id):
	question = get_question(test_id, question_id)
	test = get_test(test_id)
	is_new_question = (question_id == test["questions_count"] + 1)
	print(is_new_question)
	if request.method == "POST":
		statement = request.form["statement"]
		option_a = request.form["option_a"]
		option_b = request.form["option_b"]
		option_c = request.form["option_c"]
		option_d = request.form["option_d"]
		correct_option = request.form["correct_option"]
		if is_new_question:
			add_question(test_id, question_id, statement, option_a, option_b, option_c, option_d, correct_option)
			update_questions_count(test_id, test["questions_count"])
			print("Added question {} to test {}".format(question_id, test_id))
		else:
			update_question(test_id, question_id, statement, option_a, option_b, option_c, option_d, correct_option)
			print("Updated question {} of test {}".format(question_id, test_id))
		return redirect(url_for("test.test", test_id = test_id, question_id = question_id))
	else:
		return render_template("test/test.html", test = test, question = question, question_id = question_id)
