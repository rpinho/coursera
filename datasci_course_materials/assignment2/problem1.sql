--SELECT term,count FROM frequency WHERE docid='10080_txt_crude' OR docid='17035_txt_earn';

--SELECT count(*) FROM frequency WHERE term=='parliament';
--SELECT count(*) FROM frequency WHERE docid=='10398_txt_earn';

--SELECT count(docid) FROM frequency WHERE term=='transactions' and term=='world';

--.separator ", "
SELECT MAX(a) FROM (
SELECT SUM(count) AS a
FROM frequency
WHERE term='washington' OR term='taxes' OR term='treasury'
GROUP BY docid
);--HAVING SUM(count) > 300;


/*SELECT *
FROM (
SELECT term FROM frequency WHERE docid=='10080_txt_crude' --AND count==1)
INTERSECT --UNION
SELECT term FROM frequency WHERE docid=='17035_txt_earn' --AND count==1)
);*/

--SELECT count(count) FROM frequency WHERE docid=='10398_txt_earn' AND count==1 OR docid=='925_txt_trade' AND count==1;