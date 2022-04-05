from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
from .config import settings

# do not realy need them cause we are connecting with sqlalchemy
import psycopg2
from  psycopg2.extras import RealDictCursor

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:kalakrasa@localhost/testPosts'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

print(settings.database_name)
 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind=engine)

Base = declarative_base() # all the models that we will create will extend this class

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # Σύνδεση με τη βάση δεν χρειάζεται πλεον συνδεόμαστε με sqlalchemy
# while True: # βρόγχος ώστε αν υπάρχει πρόβλημα σύνδεσης άνα δύο δεύτερα να προσπαθεί να συνδεθεί στη βάση, 
#             # ώστε αν δεν γίνει σύνδεση να μην ξεκινά την fastapi....αν γίνει σύνδεση με το break βγαίνει από το βρόγχο

#     try: 
#         conn = psycopg2.connect(host = 'localhost', database = 'testPosts', user = 'postgres', password = 'kalakrasa', cursor_factory=RealDictCursor) 
#         cursor = conn.cursor()
#         print("Database connection was successfull!")
#         break
#     except Exception as error:
#         print("Connection to Database failed")
#         print("Error:", error)
#         time.sleep(2)