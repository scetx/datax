import click
from flask.cli import with_appcontext
from flaskr.db import get_db
from flaskr.blog import get_post, get_replies


@click.command('list-users')
@with_appcontext
def list_users_command():
    """List all users with their id and username"""
    db = get_db()
    table = db.execute(
        'SELECT id, username FROM user'
    ).fetchall()
    for row in table:
        click.echo(dict(row))


@click.command('list-posts')
@click.argument('n', default=5)
@click.argument('start', default=0)
@with_appcontext
def list_post_command(start, n):
    """List N posts from START in the table"""
    db = get_db()
    posts = db.execute(
        'SELECT id, author_id, created, title, body'
        ' FROM post LIMIT ? OFFSET ?',
        (n, start,)
    ).fetchall()
    for post in posts:
        click.echo("ID:        {id}\n"
                   "Title:     {title}\n"
                   "Body:      {body}\n"
                   "Created:   {created}\n"
                   "author_id: {author_id}\n"
                   "--------------------------"
                   .format(**post))


@click.command('del-post')
@click.argument('id')
@with_appcontext
def del_post_command(id):
    """Delete post and replies according to post id"""
    post = get_post(id, check_exist=False, check_author=False)
    replies = get_replies(id)
    if post is None:
        click.echo("Post not found")
        assert len(replies) == 0
        return
    click.echo("The following post and replies will be deleted:\n")
    click.echo("> Title:   {title}\n"
               "> Body:    {body}\n"
               "> Created: {created}\n"
               "> By:      {username} (id: {author_id})\n"
               "--------------------------"
               .format(**post))
    for reply in replies:
        click.echo(">> Reply id: {id}\n"
                   ">> Body:     {body}\n"
                   ">> Created:  {created}\n"
                   ">> By:       {username} (id: {author_id})\n"
                   "--------------------------"
                   .format(**reply))
    decision = input("Proceed? y/[n] ")
    if decision == 'y':
        # TODO: Q4.a
        # Your code here
        # ...
        click.echo('Done')
    else:
        click.echo('Aborted')


@click.command('del-user')
@click.argument('id')
@with_appcontext
def del_user_command(id):
    """Delete user and corresponding post and replies"""
    decision = input("Proceed? y/[n] ")
    if decision == 'y':
        # TODO: Q4.b
        # Your code here
        # ...
        click.echo('Done')
    else:
        click.echo('Aborted')


def reg_command(app):
    app.cli.add_command(list_post_command)
    app.cli.add_command(list_users_command)
    app.cli.add_command(del_post_command)
    app.cli.add_command(del_user_command)
