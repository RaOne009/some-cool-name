from server.db import get_db

def roll_number_taken(roll_number):
	db = get_db()
	return db.execute("SELECT id FROM students WHERE roll_number = ?", (roll_number, )).fetchone() is not None
	
	
def email_id_taken(email_id):
	db = get_db()
	return db.execute("SELECT id FROM admins WHERE email_id = ?", (email_id, )).fetchone() is not None
	
	
def add_student(name, roll_number, phone_number, password):
	db = get_db()
	db.execute("INSERT INTO students(name, roll_number, phone_number, password) VALUES(?, ?, ?, ?)", (name, roll_number, phone_number, password))
	db.commit()
	
	
def add_admin(name, email_id, password):
	db = get_db()
	db.execute("INSERT INTO admins(name, email_id, password) VALUES(?, ?, ?)", (name, email_id, password))
	db.commit()


def get_student(roll_number):
	db = get_db()
	user = db.execute("SELECT * FROM students WHERE roll_number = ?", (roll_number, )).fetchone()
	return user
	
	
def get_admin(email_id):
	db = get_db()
	user = db.execute("SELECT * FROM admins WHERE email_id = ?", (email_id, )).fetchone()
	return user


def add_test(name, start_time, duration):
	db = get_db()
	db.execute("INSERT INTO tests(name, start_time, duration) VALUES(?, ?, ?)", (name, start_time, duration))
	db.commit()
	
	
def get_all_tests():
	db = get_db()
	all_tests = db.execute("SELECT * FROM tests")
	return all_tests


def get_test(test_id):
	db = get_db()
	test = db.execute("SELECT * FROM tests WHERE id = ?", (test_id, )).fetchone()
	return test


def update_test(test_id, name, start_time, duration):
	db = get_db()
	db.execute("UPDATE tests SET name = ?, start_time = ?, duration = ? WHERE id = ?", (name, start_time, duration, test_id))
	db.commit()


def get_question(test_id, question_id):
	db = get_db()
	question = db.execute("SELECT * FROM questions WHERE test_id = ? AND question_id = ?", (test_id, question_id)).fetchone()
	return question
