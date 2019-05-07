# Files:

- QueryResults

SELECT
  Posts.Id,
  Posts.Body,
  Posts.Tags,
  Posts.CreationDate,
  Posts.DeletionDate,
  Posts.Score,
  Posts.OwnerUserId,
  Posts.LastActivityDate,
  Posts.AnswerCount,
  Posts.CommentCount,
  Posts.FavoriteCount,
  Posts.ClosedDate,
  Users.Id,
  Users.Reputation,
  Users.UpVotes,
  Users.DownVotes
FROM
  Posts JOIN Users ON Posts.OwnerUserId = Users.Id
WHERE
  datalength(Tags) > 0
;

- JavaQueryResults

SELECT
  Posts.Id,
  Posts.Body,
  Posts.Tags,
  Posts.CreationDate,
  Posts.DeletionDate,
  Posts.Score,
  Posts.OwnerUserId,
  Posts.LastActivityDate,
  Posts.AnswerCount,
  Posts.CommentCount,
  Posts.FavoriteCount,
  Posts.ClosedDate,
  Users.Id,
  Users.Reputation,
  Users.UpVotes,
  Users.DownVotes
FROM
  Posts JOIN Users ON Posts.OwnerUserId = Users.Id
WHERE
  datalength(Posts.Tags) > 0
  AND Posts.Tags LIKE '%java%'
  AND Posts.Tags NOT LIKE '%javascript%'
;

- Python Query Results

SELECT
  Posts.Id,
  Posts.Body,
  Posts.Tags,
  Posts.CreationDate,
  Posts.DeletionDate,
  Posts.Score,
  Posts.OwnerUserId,
  Posts.LastActivityDate,
  Posts.AnswerCount,
  Posts.CommentCount,
  Posts.FavoriteCount,
  Posts.ClosedDate,
  Users.Id,
  Users.Reputation,
  Users.UpVotes,
  Users.DownVotes
FROM
  Posts JOIN Users ON Posts.OwnerUserId = Users.Id
WHERE
  datalength(Posts.Tags) > 0
  AND Posts.Tags LIKE '%python%'
;
