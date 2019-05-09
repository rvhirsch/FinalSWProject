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

- Fig 1: boxplots of data for all repos

- Fig 2: word clouds for each repo

- Fig 3: bar charts of data for all repos (using same data as Fig 1)