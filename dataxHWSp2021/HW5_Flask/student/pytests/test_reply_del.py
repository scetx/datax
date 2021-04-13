import pytest
from flaskr.db import get_db
import os

with open(os.path.join(os.path.dirname(__file__), 'data-reply.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


def test_index(app, client, auth):
    with app.app_context():
        get_db().executescript(_data_sql)
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test' in response.data
    assert b'on 01/01/2021' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data
    assert b'href="/1/reply"' in response.data

    assert b'on 01/02/2021' in response.data
    assert b'test reply1' in response.data
    assert b'href="/R1/delete"' not in response.data
    assert b'on 01/03/2021' in response.data
    assert b'test reply2' in response.data
    assert b'"/R2/delete"' in response.data


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/reply',
    '/1/delete',
    '/R1/delete',
    '/R2/delete',
))
def test_login_required(client, path, app):
    with app.app_context():
        get_db().executescript(_data_sql)
    response = client.post(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'


def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/1/update"' not in client.get('/').data

    with app.app_context():
        get_db().executescript(_data_sql)
    assert client.post('/R1/delete').status_code == 403


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/reply',
    '/2/delete',
    '/R1/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404


def test_delete_reply(client, auth, app):
    with app.app_context():
        get_db().executescript(_data_sql)
    auth.login()
    response = client.post('/R2/delete')
    assert response.headers['Location'] == 'http://localhost/'

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is not None
        reply1 = db.execute('SELECT * FROM reply WHERE id = 1').fetchone()
        assert reply1 is not None
        reply2 = db.execute('SELECT * FROM reply WHERE id = 2').fetchone()
        assert reply2 is None


def test_delete(client, auth, app):
    with app.app_context():
        get_db().executescript(_data_sql)
    auth.login()
    response = client.post('/1/delete')
    assert response.headers['Location'] == 'http://localhost/'

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None
        reply = db.execute('SELECT * FROM reply').fetchone()
        assert reply is None
