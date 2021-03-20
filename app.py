from flask import Flask, render_template, request , redirect
from flask_sqlalchemy import SQLAlchemy 
from calculate_date import *
from sqlalchemy import desc

 #initialising the app
app = Flask(__name__)

#initialising the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///batches.db'
db = SQLAlchemy(app)

#database model
class Batch_Details(db.Model):
	batch_no = db.Column(db.Integer , primary_key = True)
	course = db.Column(db.String(20) , nullable = False)
	level = db.Column(db.Integer , nullable = False)
	sessions = db.Column(db.Integer , nullable = False)
	trainer = db.Column(db.String(30) , nullable = False)
	days = db.Column(db.String(50) , nullable = False)
	start_time = db.Column(db.String(20) , nullable = False)
	end_time = db.Column(db.String(20) , nullable = False)
	students = db.Column(db.String(50) , nullable = False)
	start_date = db.Column(db.String(20) , nullable = False)
	stop_date = db.Column(db.String(20) , nullable = False)
	next_date = db.Column(db.String(20) , nullable = False)


	def __repr__(self):
		return '<Batch No %r>' %self.batch_no



@app.route('/')
def home():
	data = Batch_Details.query.order_by(desc(Batch_Details.batch_no))

	
	return render_template('home.html' , data = data)
 

@app.route('/edit' , methods = ['GET', 'POST'])
def edit():
	data = Batch_Details.query.order_by(desc(Batch_Details.batch_no))
	last_record = data[0].batch_no
		
 
	if request.method == "POST":


		batch_no =  last_record+1
		course = request.form['course']
		level  = request.form['level'] 
		sessions  = request.form['sessions'] 
		days_list = request.form.getlist('days')
		days = ''
		for i in days_list: 
			days += i 
		

		start_time  = request.form['start_time']
		end_time  = request.form['end_time'] 
		trainer = request.form['trainer']
		students = request.form['students']
		start_date = request.form['start_date']  #2021-02-25

		stop_next_dates = get_date(start_date, days ,sessions)
		stop_date = stop_next_dates[0]
		next_date =  stop_next_dates[1]



		new_entry = Batch_Details(batch_no = batch_no,course = course,level = level, sessions=sessions,days = days,start_time=start_time,end_time=end_time, trainer = trainer, students = students,start_date = start_date ,stop_date =stop_date  ,next_date =next_date )	

 

		try:
	  
			db.session.add(new_entry)
			db.session.commit()

			return redirect('/edit')
		except:
			return "Error Ocurred "

		'''
		print(course)
		print(level)
		print(days)
		print(trainer)
		print(students)
		print(start_date)  #
		print((start_date))

		'''


	else:


		return render_template('edit.html', data = data)

@app.route('/update/<int:batch_no>' , methods = ['GET', 'POST'])
def update(batch_no):

	entry_to_update  = Batch_Details.query.get_or_404(batch_no)
    
	if request.method == "POST":

		entry_to_update.course = request.form['course']
		entry_to_update.level = request.form['level']
		entry_to_update.sessions = request.form['sessions']
		entry_to_update.trainer = request.form['trainer']
		days_list = request.form.getlist('days')
		days = ''
		for i in days_list: 
			days += i 
 
		entry_to_update.days = days
		entry_to_update.start_time = request.form['start_time']
		entry_to_update.end_time = request.form['end_time']
		entry_to_update.students = request.form['students']
		entry_to_update.start_date = request.form['start_date']


		stop_next_dates = get_date(request.form['start_date'], days ,request.form['sessions'])
		entry_to_update.stop_date = stop_next_dates[0]
		entry_to_update.next_date =  stop_next_dates[1]


		if request.form['stop_date']:
			entry_to_update.stop_date = request.form['stop_date']

		if request.form['next_date']:
			entry_to_update.next_date = request.form['next_date']



		try:
			db.session.commit()
			return redirect('/edit')
		except: 
			"Error Occurred"
	else:  

		return render_template('update.html',  entry_to_update=entry_to_update)
	
	
  
@app.route('/delete/<int:batch_no>' , methods = ['GET', 'POST'])
def delete(batch_no):
	entry_to_delete = Batch_Details.query.get_or_404(batch_no)
    


	try:
		db.session.delete(entry_to_delete)
		db.session.commit()
		return redirect('/edit')
	except: 
		return "Error Occurred"


if  __name__ == "__main__":
	app.run(debug = True)










