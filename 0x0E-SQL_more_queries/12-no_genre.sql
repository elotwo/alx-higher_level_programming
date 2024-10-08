-- this script lists all shows contained in hbtn_0d_tvshows without a genre linked
-- This statement select from two tables using the keyword left join
SELECT tv_shows.title, COALESCE(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
