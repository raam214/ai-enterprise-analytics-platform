from sqlalchemy import create_engine

# Database connection details
DB_USER = "postgres"
DB_PASSWORD = "rAMA&1505"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "enterprise_decision_intelligence"

# Create SQLAlchemy engine
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def get_engine():
    return engine


if __name__ == "__main__":
    try:
        engine.connect()
        print("Database connection successful")
    except Exception as e:
        print("Database connection failed:", e)
