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
    assert b'on 01/03/2021' in response.data
    assert b'test reply2' in response.data


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/reply',
    '/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers['Location'] == 'http://localhost/auth/login'


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/reply',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404


def test_reply(client, auth, app):
    auth.login()
    response = client.get('/1/reply')
    assert response.status_code == 200
    assert b'by test' in response.data
    assert b'on 01/01/2021' in response.data
    assert b'test\nbody' in response.data
    client.post('/1/reply', data={'body': 'test reply'})
    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM reply'
                           ' WHERE post_id=1').fetchone()[0]
        assert count == 1


@pytest.mark.parametrize('path', (
    '/1/reply',
))
def test_reply_validate(client, auth, path, app):
    auth.login()
    response = client.post(path, data={'body': ''})
    assert b'reply body is required.' in response.data
    with app.app_context():
        db = get_db()
        reply = db.execute('SELECT * FROM reply').fetchone()
        assert reply is None
