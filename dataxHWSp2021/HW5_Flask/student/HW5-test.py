import pytest

print(pytest.main(["-qqs", "pytests/test_factory.py"]))
print(pytest.main(["-qqs", "pytests/test_db.py"]))
print(pytest.main(["-qqs", "pytests/test_auth.py"]))
print(pytest.main(["-qqs", "pytests/test_blog.py"]))

print(pytest.main(["-qqs", "pytests/test_reply.py"]))
print(pytest.main(["-qqs", "pytests/test_reply_del.py"]))
print(pytest.main(["-qqs", "pytests/test_anonym.py"]))
print(pytest.main(["-qqs", "pytests/test_cli_del_post.py"]))
print(pytest.main(["-qqs", "pytests/test_cli_del_user.py"]))
