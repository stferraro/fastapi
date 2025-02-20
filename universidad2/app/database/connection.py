from sqlmodel import create_engine, SQLModel
import os
from dotenv import load_dotenv

# Cargar variables del .env desde la raíz del proyecto
load_dotenv()

class DatabaseConnection:
    def __init__(self):
        # Obtener valores desde el archivo .env
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")
        db_driver = os.getenv("DB_DRIVER", "postgresql+psycopg2")  # Valor por defecto

        # Verificar que no haya valores vacíos
        if not all([db_user, db_password, db_host, db_port, db_name]):
            raise ValueError("Faltan variables en el archivo .env")

        # Construir la URL de conexión
        self.database_url = f"{db_driver}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

        # Crear el engine de SQLAlchemy
        self.engine = create_engine(self.database_url, echo=True)

    def create_tables(self):
        # Asegúrate de importar los modelos correspondientes
        from app.models import Estudiante
        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        return Session()

# Crear la instancia de la conexión
db = DatabaseConnection()



