from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configparser as cfg

config_db = cfg.ConfigParser()
config_db.read("hh_config.ini")
f = config_db["PostgreSQL"]["path"]
engine = create_engine(config_db["PostgreSQL"]["path"])
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = Session()
Base = declarative_base()
Base.metadata.create_all(bind=engine)

