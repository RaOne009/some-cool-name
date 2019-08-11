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
