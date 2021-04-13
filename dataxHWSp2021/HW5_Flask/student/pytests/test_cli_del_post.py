from flaskr.db import get_db
import os

with open(os.path.join(os.path.dirname(__file__),
          'data-test-cli.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


def test_del_post_command_1(runner, app):
    with app.app_context():
        get_db().executescript(_data_sql)
        runner.invoke(args=['del-post', '1'], input='y')
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None
        reply = db.execute('SELECT * FROM reply WHERE post_id = 1').fetchone()
        assert reply is None
        post = db.execute('SELECT * FROM post WHERE id = 2').fetchall()
        assert post is not None
        reply = db.execute('SELECT * FROM reply WHERE post_id = 2').fetchall()
        assert len(reply) == 2


def test_del_post_command_2(runner, app):
    with app.app_context():
        get_db().executescript(_data_sql)
        runner.invoke(args=['del-post', '2'], input='y')
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 2').fetchone()
        assert post is None
        reply = db.execute('SELECT * FROM reply WHERE post_id = 2').fetchone()
        assert reply is None
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchall()
        assert post is not None
        reply = db.execute('SELECT * FROM reply WHERE post_id = 1').fetchall()
        assert len(reply) == 2
