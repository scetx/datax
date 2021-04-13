INSERT INTO post (title, body, author_id, created, anonym)
VALUES
  ('test title', 'test' || x'0a' || 'body', 2, '2021-01-02 00:00:00', True);

INSERT INTO reply (body, author_id, post_id, created)
VALUES
  ('test reply1', 2, 1, '2021-01-02 00:00:00'),
  ('test reply2', 1, 1, '2021-01-03 00:00:00'),
  ('test reply3', 2, 2, '2021-01-03 00:00:00'),
  ('test reply4', 1, 2, '2021-01-04 00:00:00');
