from flaskr.db import get_db
import os

with open(os.path.join(os.path.dirname(__file__),
          'data-test-cli.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


def test_del_user_command_1(runner, app):
    with app.app_context():
        get_db().executescript(_data_sql)
        runner.invoke(args=['del-user', '1'], input='y')
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None
        reply = db.execute('SELECT * FROM reply WHERE post_id = 1').fetchone()
        assert reply is None
        post = db.execute('SELECT * FROM post WHERE id = 2').fetchone()
        assert post is not None
        reply = db.execute('SELECT * FROM reply WHERE post_id = 2').fetchall()
        assert len(reply) == 1
        assert reply[0]['author_id'] == 2
        user = db.execute('SELECT * FROM user').fetchall()
        assert len(user) == 1
        assert user[0]['id'] == 2


def test_del_user_command_2(runner, app):
    with app.app_context():
        get_db().executescript(_data_sql)
        runner.invoke(args=['del-user', '2'], input='y')
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 2').fetchone()
        assert post is None
        reply = db.execute('SELECT * FROM reply WHERE post_id = 2').fetchone()
        assert reply is None
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is not None
        reply = db.execute('SELECT * FROM reply WHERE post_id = 1').fetchall()
        assert len(reply) == 1
        assert reply[0]['author_id'] == 1
        user = db.execute('SELECT * FROM user').fetchall()
        assert len(user) == 1
        assert user[0]['id'] == 1
