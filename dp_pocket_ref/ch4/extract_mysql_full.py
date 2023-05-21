import pymysql
import csv
import configparser
import boto3

parser = configparser.ConfigParser()
parser.read("../../pipeline.conf") ###does it matter where the conf file is located on your machine??

# load mysql connection values
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
dbname = parser.get("mysql_config", "database")
password = parser.get("mysql_config", "password")

# load aws_boto_cred values
access_key = parser.get("aws_boto_credentials", "access_key")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")

# set mysql connection
conn = pymysql.connect(
    host=hostname,
    user=username,
    password=password,
    db=dbname,
    port=int(port)
)

if conn is None:
    print("error conencting to mysql db")
else:
    print("mysql connection established")

m_query = "select * from orders;"
local_filename = "order_extract.csv"

m_cursor = conn.cursor()
m_cursor.execute(m_query)
results = m_cursor.fetchall()

with open(local_filename, 'w') as fp:
    csv_w = csv.writer(fp, delimiter = '|')
    csv_w.writerows(results)
    fp.close()
    m_cursor.close()
    conn.close()

s3 = boto3.client(
    's3',
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key
)

s3_file = local_filename

s3.upload_file(local_filename, bucket_name, s3_file)

print("script complete")
