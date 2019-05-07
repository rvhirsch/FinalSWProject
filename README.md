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
  AND Posts.Tags LIKE '%libraryname%'
;

- getAvgTimes() - returns average dateClosed-dateOpened

- getAvgRep() - returns average user reputation