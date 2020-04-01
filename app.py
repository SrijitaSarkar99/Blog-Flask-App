from flask import Flask, render_template, request, redirect
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def homepage():
	con = sql.connect("blogdata.db")
	con.row_factory = sql.Row
	cur = con.cursor()
   	cur.execute("SELECT * FROM myblogs")
   	rows = cur.fetchall();
   	return render_template('home.html', items=rows)

@app.route('/newpost', methods = ['POST', 'GET'])
def addpostpage():
	if request.method == 'POST':
			title = request.form['title']
			blog = request.form['blog']

			with sql.connect("blogdata.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO myblogs (title,blog) VALUES (?,?)",(title,blog))
				con.commit()
				
				return redirect('/newpost')
	else:
		return render_template('newpost.html')
		con.close()

@app.route('/delete/<string:title>')
def deletepost(title):
		con = sql.connect("blogdata.db")
		cur = con.cursor()
		cur.execute('DELETE FROM myblogs WHERE title=(?)', (title,))
		con.commit()
		return redirect('/')



if __name__ == "__main__":
    app.run(debug = True)	