
乐岸教育ORM教学示例<http://www.leanntech.com>

# 创建

创建数据库

	In [1]: from app import db
	In [2]: db.create_all()   # db.drop_all() 删除数据库
	In [3]: from app import Student
	In [4]: bob = Student('bob', 20, 'beijing')
	In [5]: lily = Student('lily', 19, 'shanghai')
	In [6]: db.session.add(bob)
	In [7]: db.session.add(lily)
	In [8]: db.session.commit()


# 插入

数据插入示例

	mysql> select * from student;
	+-----+-------+------+----------+
	| sno | sname | sage | saddress |
	+-----+-------+------+----------+
	|   1 | bob   |   20 | beijing  |
	|   2 | lily  |   19 | shanghai |
	+-----+-------+------+----------+
	2 rows in set (0.00 sec)

# 查询

all:

	In [9]: Student.query.all()
	Out[9]:
	[Student({'sno': 1L,'sage': 20L, 'saddress': u'beijing', 'sname': u'bob'}),
	 Student({'sno': 2L, 'sage': 19L, 'saddress': u'shanghai', 'sname': u'lily'})]

order by:

	In [11]: Student.query.order_by(Student.sage.desc()).all()
	Out[11]:
	[Student({'sno': 1L, 'sage': 20L, 'saddress': u'beijing', 'sname': u'bob'}),
	 Student({'sno': 2L, 'sage': 19L, 'saddress': u'shanghai', 'sname': u'lily'})]

	In [12]: Student.query.order_by(Student.sage).all()
	Out[12]:
	[Student({'sno': 2L, 'sage': 19L, 'saddress': u'shanghai', 'sname': u'lily'}),
	 Student({'sno': 1L, 'sage': 20L, 'saddress': u'beijing', 'sname': u'bob'})]

limit:

	In [13]: Student.query.order_by(Student.sage).first()
	Out[13]: Student({'sno': 2L, 'sage': 19L, 'saddress': u'shanghai', 'sname': u'lily'})

where:

	In [19]: Student.query.filter_by(sno=1).all()
	Out[19]: [Student({'sno': 1L, 'sage': 20L, 'saddress': u'beijing', 'sname': u'bob'})]

删除：

	In [14]: student = Student.query.filter_by(sno=1).first()
	In [15]: student
	Out[15]: Student({'sno': 1L, 'sage': 20L, 'saddress': u'beijing', 'sname': u'bob'})
	In [16]: db.session.delete(student)
	In [17]: db.session.commit()

# Flask代码

在Flask中使用ORM示例:

	@app.route('/user/<username>')
	def show_user(username):
	    user = User.query.filter_by(username=username).first_or_404()
	    return render_template('show_user.html', user=user)
