# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, session
import config
from models import User, Question, Comment
from exts import db
from decorators import login_restrict

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
	context = {
		'questions': Question.query.order_by(Question.create_time.desc()).all()
	}
	return render_template('index.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		print '111111'
		return render_template('login.html', tip='')
	else:
		print '222222'
		tel = request.form.get('telephone')
		pwd = request.form.get('password')
		user = User.query.filter(User.tel == tel, User.password == pwd).first()
		if user:
			session['user_id'] = user.id
			session.permanent = True
			return redirect(url_for('index'))
		else:
			print '333333'
			tmp_str = u"手机号码或者密码错误，请确认后在登陆～"
			return render_template('login.html', tip=tmp_str)


@app.route('/detail/<question_id>')
def detail(question_id):
	detail_question = Question.query.filter(Question.id == question_id).first()

	return render_template('detail.html', question=detail_question)


@app.route('/register/', methods=['POST', 'GET'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	else:
		tel = request.form.get('tel')
		username = request.form.get('username')
		pwd1 = request.form.get('pwd1')
		#pwd2 = request.form.get('pwd2')
		#手机号码验证
		user = User.query.filter(User.tel == tel).first()
		if user:
			return render_template('user_exists.html')
		else:
			user = User(tel=tel, username=username, password=pwd1)
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('login'))


@app.route('/logout/')
def logout():
	session.clear()
	# del session['user_id']
	# session.pop('user_id')
	return redirect(url_for('login'))


@app.route('/question/', methods=['POST', 'GET'])
@login_restrict
def question():
	if request.method == 'GET':
		return render_template('question.html')
	else:
		title = request.form.get('title')
		content = request.form.get('content')
		question1 = Question(title=title, content=content)
		user_id = session.get('user_id')
		user = User.query.filter(User.id == user_id).first()
		question1.author = user
		db.session.add(question1)
		db.session.commit()
		return redirect(url_for('index'))


@app.route('/add_comment/', methods=['POST'])
@login_restrict
def add_comment():
	content = request.form.get('comment')
	#print content
	question_id = request.form.get('question_id')

	comment = Comment(content=content)
	user_id = session['user_id']
	user = User.query.filter(User.id == user_id).first()
	comment.author = user

	question_comment = Question.query.filter(Question.id == question_id).first()
	comment.question = question_comment
	db.session.add(comment)
	db.session.commit()

	return redirect(url_for('detail', question_id=question_id))
	#return redirect(url_for('login'))


@app.context_processor
def my_context_processor():
	user_id = session.get('user_id')
	if user_id:
		# print 'user_id=====', user_id
		user = User.query.filter(User.id == user_id).first()
		if user:
			return {'User': user}
	# print 'User_id not exists'
	return {}


@app.route('/search_question/', methods=['POST'])
@login_restrict
def search_question():
	key_words = request.form.get('search')
	#print (key_words)
	if key_words == '':
		#print 'AAAA11111'
		return redirect(url_for('index'))

	context = {
		'questions': Question.query.filter(Question.content.like('%'+key_words+'%')).order_by(Question.create_time.desc(
		)).all()
	}

	length = len(context['questions'])
	if length == 0:
		return redirect(url_for('index'))
	else:
		return render_template('index.html', **context)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.errorhandler(505)
def page_not_found(e):
	return render_template('505.html'), 505


if __name__ == '__main__':
	app.run()
