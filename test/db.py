import sqlalchemy as db
from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData
import datetime

#conn = create_engine('sqlite:///db.sqlite', echo=True)
conn = create_engine('postgresql://grin:qwer1234t5@localhost/helper', echo=True)
metadata = MetaData()

clients = db.Table(
    "clients",
    metadata,
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, unique=True ),
    db.Column("name", db.String),
    db.Column("company", db.String),
    db.Column("email", db.String,  unique=True ),
    db.Column("phone", db.String ),
    db.Column("password", db.String),
    db.Column("balance",  db.String),
)

agents = db.Table(
    "agents",
    metadata,
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, unique=True ),
    db.Column("client_id",  db.Integer, db.ForeignKey('clients.id')),
    db.Column("updated_at", db.DateTime, default=datetime.datetime.utcnow ),
    db.Column("created_at", db.DateTime, default=datetime.datetime.utcnow ),
    db.Column("uuid", db.String,  unique=True ),
    db.Column("ip_address", db.String, unique=True ),
)


agent_subscribions = db.Table(
    "agent_subscriptions",
    metadata,
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, unique=True ),
    db.Column("created_at", db.DateTime, default=datetime.datetime.utcnow ),
    db.Column("charged_amount", db.String),
    db.Column("expiried_at", db.DateTime, default=datetime.datetime.utcnow ),
    db.Column("renew_automatically", db.String),
    db.Column("agent_id", db.Integer, db.ForeignKey('agents.id')),
    db.Column("subscription_id", db.Integer, db.ForeignKey('subscriptions.id')),
)


subscribions = db.Table(
    "subscriptions",
    metadata,
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, unique=True ),
    db.Column("type", db.String),
    db.Column("key",  db.String),
    db.Column("name", db.String),
    db.Column("created_at", db.DateTime, default=datetime.datetime.utcnow ),
    db.Column("updated_at", db.DateTime, default=datetime.datetime.utcnow ),
    db.Column("changing_period", db.String),
    db.Column("charged_amount", db.String),
)    


metadata.create_all(bind=conn)








