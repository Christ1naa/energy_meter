import os

TARIFFS = {"day": 2.5, "night": 1.2}
FAKE_INCREMENT = {"day": 100, "night": 80}

SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL", "sqlite:///./meters.db")

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost/")
QUEUE_NAME = "meter_readings"
