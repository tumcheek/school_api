from sqlalchemy import create_engine
from config import db_config

engine = create_engine(f"postgresql://{db_config['postgresql']['user']}:{db_config['postgresql']['pass']}@"
                       f"{db_config['postgresql']['host']}/test")
engine.connect()
