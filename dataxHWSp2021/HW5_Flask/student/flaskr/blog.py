from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username, anonym'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    replies = []
    for post in posts:
        replies.append(get_replies(post["id"]))
    return render_template('blog/index.html',
                           posts_replies=zip(posts, replies))


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        anonym = False
        # TODO: Q3
        # Extract anonym from request.form

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id, anonym)'
                ' VALUES (?, ?, ?, ?)',
                (title, body, g.user['id'], anonym)
            )
            db.commit()
            # TODO: Q1.b
            # Redirect to the index page.
            # Modify the return statement below
            return

    return render_template('blog/create.html')


def get_post(id, check_exist=True, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username, anonym'
        ' FROM post p JOIN user u'
        '  ON p.author_id = u.id'
        '  AND p.id = ?'
        ' ORDER BY created',
        (id,)
    ).fetchone()

    if check_exist and post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


def get_replies(postid):
    replies = []
    # TODO: Q2.a
    # Return a list of rows in the reply table 
    #    which were replied to the post with postid.
    # Also include username in row.

    return replies 


@bp.route('/<int:id>/reply', methods=('GET', 'POST'))
@login_required
def reply(id):
    post = get_post(id, True, False)
    replies = get_replies(id)
    if request.method == 'POST':
        body = None
        # TODO: Q2.a
        # Get reply text from the request and store in body.

        error = None

        if not body:
            error = 'reply body is required.'
        if error is not None:
            flash(error)
        else:
            # TODO: Q2.a 
            # Commit new reply to database.

            # TODO: Q2.a
            # Redirect to the index page.
            # Modify the return statement below
            return

    return render_template('blog/reply.html', post=post, replies=replies)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            # TODO: Q1.b 
            # Update the title and body of the post in the table.

            # TODO: Q1.b
            # Redirect to the index page.
            # Modify the return statement below
            return

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))

    # TODO: Q2.b 
    # Also delete replies to the post.

    db.commit()

    # TODO: Q1.b
    # Redirect to the index page.
    # Modify the return statement below
    return


@bp.route('/R<int:id>/delete', methods=('POST',))
@login_required
def delete_reply(id):
    # TODO: Q2.b
    # Delete the reply according to the reply id.
    # Return 404 if reply not found with id or 403 if wrong author.

    # TODO: Q2.b
    # Redirect to the index page.
    # Modify the return statement below
    return
