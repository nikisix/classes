#Here are a few commands for reference for downloading and uploading data

#[[ BOILERPLATE ]]
#Put these at the beginning of ALL your scripts
set -o errexit # stop the script if a command fails
set -o nounset # fail on unset variables
set -o pipefail

#[[ DOWNLOAD ]]
#downloading files with aria
aria2c --dir=sf1b --max-connection-per-server=5 --parameterized-uri=true --force-sequential=true \
    "http://www2.census.gov/census_1990/STF1B_ASCII/STF1B-AK.zip" \
    "http://www2.census.gov/census_1990/STF1B_ASCII/STF1B-AKh.zip" \
    "http://www2.census.gov/census_1990/STF1B_ASCII/STF1B-AL.zip"

#download an entire web-directory and all of its children
wget --directory-prefix=sf3a --accept dbf --mirror --adjust-extension --convert-links\
    --backup-converted --no-parent -e robots=off --level=1 --random-wait\
    "http://www2.census.gov/census_1990/CD90_3A_1/"

#[[ DATATYPING ]]
#upload a file to a database with a non-standard encoding
cat $f | psql -dpropdata -Upostgres -c"copy myschema.mytable from stdin with csv encoding 'latin1';";

#load data into a temp table
COPY myschema.mytable FROM '/mnt/tmp/acs2014_5yr/tab4/sumfile/prod/2010thru2014/group1/e20145ak0001000.txt' WITH CSV;

#copy the data into a temp table
INSERT INTO myschem.mytable
SELECT s.fileid, s.filetype, upper(s.stusab), s.chariter, s.seq, s.logrecno::int, g.geoid,
NULLIF(NULLIF(s.B00001001_moe, ''), '.')::double precision,
NULLIF(NULLIF(s.B00002001_moe, ''), '.')::double precision
FROM acs2014_5yr.tmp_seq0001_moe s
JOIN acs2014_5yr.geoheader g ON (lower(s.stusab)=lower(g.stusab) AND s.logrecno=g.logrecno);


#[[ TRANSFORMS ]]
#delete the first and last lines
#replace spaces with zeros
#load into the db
cat $file |\
sed -n -e '$d' -e '2,$'p |\
sed -e 's/ /0/g' |\
psql -hlocalhost -dpropdata -Upostgres -c "COPY myschema.mytable FROM STDIN"
