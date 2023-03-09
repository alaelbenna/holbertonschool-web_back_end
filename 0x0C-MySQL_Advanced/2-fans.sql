-- script that ranks county's origins of bands
-- best band !
SELECT origin AS origin, SUM(fans) AS nb_fans
FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
