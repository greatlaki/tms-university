from envparse import Env

env = Env()
env.read_envfile()

SQLALCHEMY_DATABASE_URL = env.str("SQLALCHEMY_DATABASE_URL")
