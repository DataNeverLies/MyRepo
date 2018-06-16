SELECT
  s1.Score                    AS Score,
  (SELECT count(DISTINCT s2.score) + 1
   FROM Scores s2
   WHERE s2.score > s1.score) AS Rank
FROM Scores s1
ORDER BY Rank ASC;
