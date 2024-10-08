-- This script lists all shows contained in the database hbtn_0d_tvshows
-- This statement select from two tables using the keyword left join
SELECT tv_shows.title, COALESCE(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
