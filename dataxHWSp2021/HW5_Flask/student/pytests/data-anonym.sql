INSERT INTO post (title, body, author_id, created, anonym)
VALUES
  ('test title', 'test' || x'0a' || 'body', 2, '2021-01-02 00:00:00', True);
