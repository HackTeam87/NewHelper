#export EE_DATABASE_URL='postgresql://user:passwd@localhost/helper'
#172.16.72.43
from starlette.config import Config
config = Config(".env")
DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
