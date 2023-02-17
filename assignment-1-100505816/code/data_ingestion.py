from cassandra.cluster import Cluster
import uuid
import datetime
import pandas as pd

cluster = Cluster(['localhost'])
session = cluster.connect()
X       
session.execute(
    "CREATE KEYSPACE IF NOT EXISTS yellow_taxi WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '3' };")

# session.execute(
#     """
#     DROP TABLE yellow_taxi.journeys;
#     """)

session.execute(
    """
    CREATE TABLE IF NOT EXISTS yellow_taxi.journeys(
    uuid uuid,
    VendorID int ,
    tpep_pickup_datetime  timestamp ,
    tpep_dropoff_datetime timestamp ,
    passenger_count float ,
    trip_distance float ,
    RatecodeID float ,
    store_and_fwd_flag text ,
    PULocationID int ,
    DOLocationID int,
    payment_type int,
    fare_amount float,
    extra float,
    mta_tax float,
    tip_amount float,
    tolls_amount float,
    improvement_surcharge float,
    total_amount float,
    congestion_surcharge float,
    airport_fee float,
    PRIMARY KEY (PULocationID, DOLocationID , uuid)
);
"""
)

data_path = r"C:\Users\aghazal\Documents\Aalto\Big data\big-data-platfroms-assingments\data\yellow_tripdata_2022-01.parquet"
df = pd.read_parquet(data_path)

data_insetion_statment = """ INSERT INTO yellow_taxi.journeys (uuid,
VendorID  ,
tpep_pickup_datetime   ,
tpep_dropoff_datetime  ,
passenger_count  ,
trip_distance  ,
RatecodeID  ,
store_and_fwd_flag  ,
PULocationID  ,
DOLocationID ,
payment_type ,
fare_amount ,
extra ,
mta_tax ,
tip_amount ,
tolls_amount ,
improvement_surcharge ,
total_amount ,
congestion_surcharge ,
airport_fee ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s ); """

for index, row in df.iterrows():
    # print ( row["tpep_pickup_datetime"].to_pydatetime() )
    try:
        session.execute(data_insetion_statment, (uuid.uuid4(), 
                                                 row["VendorID"],
                                                 row["tpep_pickup_datetime"].to_pydatetime()  ,
                                                 row["tpep_dropoff_datetime"].to_pydatetime()  ,
                                                 row["passenger_count"],
                                                 row["trip_distance"],
                                                 row["RatecodeID"],
                                                 row["store_and_fwd_flag"],
                                                 row["PULocationID"],
                                                 row["DOLocationID"],
                                                 row["payment_type"],
                                                 row["fare_amount"],
                                                 row["extra"],
                                                 row["mta_tax"],
                                                 row["tip_amount"],
                                                 row["tolls_amount"],
                                                 row["improvement_surcharge"],
                                                 row["total_amount"],
                                                 row["congestion_surcharge"],
                                                 row["airport_fee"] ) )  # right
    except Exception as e:
        print(e)