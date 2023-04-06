from google.cloud.sql.connector import Connector,IPTypes
import sqlalchemy
from cryptography.hazmat.bindings.openssl import binding


connector = Connector()

def getconn():
    conn = connector.connect(
        "website-deployment-demo:asia-south2:gcp-demo",
        "pymysql",
        user="root",
        password="admin123",
        db="info"
    )
    return conn


pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

insert_stmt = sqlalchemy.text(
      "INSERT INTO INFO (name, email, phonenumber,message) VALUES (:name, :email, :phonenumber,:message)",
  		)	
with pool.connect() as db_conn:
    
    db_conn.execute(insert_stmt, parameters={"name": "Meet", "email":"Meet@gmail.com", "phonenumber": "1234567890","message":"Hello"})    
    db_conn.commit()

connector.close()