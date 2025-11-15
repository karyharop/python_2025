from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Integer, String, Boolean, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session

# CONFIGURACIÓN BASE DE DATOS
"""
    Create: POST
    Read: GET
    Update: PUT/ PATCH 
    Delete: DELETE  
"""

# crear motor de conexión a base de datos
engine = create_engine(
    "sqlite:///09_sqlalchemy/cancioncitas.db",
    echo=True,
    connect_args={"check_same_thread": False}
)

# crear fábrica de sesiones de base de datos
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=True,
    expire_on_commit=False
)
# Hasta aquí se hace 1 vez, y lo siguiente para cada modelo, en mi caso "GENERO"

# MODELO BASE DE DATOS (sqlalchemy)
# eSTA ES LA CLASE QUE HEREDARÁN TODOS LOS MODELOS, ES PARA METADATOS, AHÍ SE PUEDEN INCLUIR TODOS LO METADATOS. 
# clase base para modelos sqlalchemy
class Base(DeclarativeBase):
    pass

# modelo de la tabla song (se crea sólo un modelo, que será una tabla en nuestra base de datos)
class Song(Base): # Aquí se puede colocar el ORM, no influye.
    __tablename__ = "songs" # nombre de la tabla en bd
    
    # clave primaria, se genera automáticamente
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # requerido, máximo 200 caracteres
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    # requerido, máximo 200 caracteres
    artist: Mapped[str] = mapped_column(String(200), nullable=False)
    # opcional, en este caso es un poco redundante colocar el nullable, pero no molesta.
    duration_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)
    # optional
    explicit: Mapped[bool | None] = mapped_column(Boolean, nullable=True)


# MODELOS PYDANTIC (schemas)
# modelos que validan los datos que llegan y salen de la api
# Normalmente se crean 4 modelos: song_response para una respuesta, song_create (esquema para crear una cancion, aquí no se mete id, porque se crea automaticamente), luego song_put esquema para actualizacion completa. Patch es para actualizaciones parciales( ejemplo cambiar sólo título, por lo tanto será sólo opcional).
# Create y put, son lo mismo o bien son muy similares.
# schema para TODAS las respuestas de la API
# lo usamos en GET, POST, PUT, PATCH

class SongResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True) # esto es lo anterior escrito, porque en response, describes como quieres que se respondan las caracteristicas de tu aplicacion. 
    
    id: int
    title: str
    artist: str
    duration_seconds: int | None
    explicit: bool | None

# schema para CREAR una canción (POST)
# no incluimos id porque se genera automáticamente, va a servir para los post, aquí se pone solo el id.
class SongCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str
    artist: str
    duration_seconds: int | None = None
    explicit: bool | None = None

# schema para ACTUALIZACIÓN COMPLETA (PUT)
# todos los campos se tienen que enviar, porque todo será reemplazado, recuerda que update es un PUT. se unsa para un reemplazo.
class SongUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str
    artist: str
    duration_seconds: int | None
    explicit: bool | None

# schema para ACTUALIZACIÓN PARCIAL (PATCH)
# sólo se envían los campos que quieras actualizar
class SongPatch(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str | None = None
    artist: str | None = None
    duration_seconds: int | None = None
    explicit: bool | None = None


# INICIALIZACIÓN BASE DE DATOS

# crear todas las tablas
Base.metadata.create_all(engine)

# método inicializar con canciones por defecto
def init_db():
    """
    Inializa la base de datos con canciones por defecto si está vacía.
    Sólo crea las canciones si no existen ya en la base de datos.
    """
    db = SessionLocal()
    try:
        existing_songs = db.execute(select(Song)).scalars().all()
        
        if existing_songs:
            return
        
        default_songs = [# ESTA ES LA LISTA
            Song(title="Mamma Mia", artist="ABBA", duration_seconds=300, explicit=False),
            Song(title="Sin ti no soy nada", artist="Amaral", duration_seconds=250, explicit=False),
            Song(title="Sonata para piano nº 14", artist="Ludwing van Beethoven", duration_seconds=800, explicit=False),
            Song(title="Mediterráneo", artist="Joan Manuel Serrat", duration_seconds=400, explicit=False),
            Song(title="Never to Return", artist="Darren Korb", duration_seconds=300, explicit=False),
            Song(title="Billie Jean", artist="Michael Jackson", duration_seconds=294, explicit=False),
            Song(title="Smells Like Teen Spirit", artist="Nirvana", duration_seconds=301, explicit=True)
        ]
        
        # agregar las canciones
        db.add_all(default_songs)
        db.commit()# CONFIRMA LOS CAMBIOS Y LOS GUARDA, IMPRESCINDIBLE ES GUARDAR LAS COSAS
    finally:
        db.close()

# inicializa la base de datos con canciones por defecto
init_db()


# DEPENDENCIA DE FASTAPI
# Para evitar hacer varias veces el try/finally, se hace esto.

def get_db():
    db = SessionLocal()
    try:
        yield db # entrega la sesión al endpoint
    finally:
        db.close()



# APLICACIÓN FASTAPI

# crea la instancia de la aplicación FastAPI
app = FastAPI(title="Cancioncitas", version="1.0.0")

# endpoint raíz. 
# esto no es obligatorio, es como para mostrar un link, que muestra lo que hace la página.
@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la app Cancioncitas"}


# ENDPOINTS CRUD

# GET - obtener TODAS las canciones
@app.get("/api/songs", response_model=list[SongResponse])
def find_all(db: Session = Depends(get_db)):# me permite hacer operacones en la base de datos.
    # db.execute(): ejecuta la consulta
    # select(Song): crea consulta SELECT * FROM song
    # .scarlars(): extrae los objetos Song
    # .all(): obtiene los resultados como lista
    return db.execute(select(Song)).scalars().all()# Aquí está devolviendo los objetos que en este caso tiene un id, artista

# GET - obtener UNA canción por id
@app.get("api/songs/{id}", response_model=SongResponse)# esto es si sólo quiero una cancion, o bien he hecho esto y este es el resultado de lo realizado. es como decir, quiero que me devuelvas una cancion, como voy a saber la cancion... con el id.
def find_by_id(id: int, db: Session = Depends(get_db)):
    # busca a canción con el id de la ruta
    # .scalar_one_or_none(): devuelve el objeto o None si no existe
    song = db.execute( # aquí es busca esta cancion...
        select(Song).where(Song.id == id)
    ).scalar_one_or_none()
    
    if not song: # si no hay nada, lanza la excepcion, lanza este codigo 404. 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado la canción con id {id}"
        )
    return song
# La lista donde están los errores habituales status codes- FastAPI / https://http.cat/

# POST - crear una nueva cancion 
# if es una validación
@app.post("api/songs", response_model=SongResponse, status_code=status. HTTP_201_CREATED)
def create(song_dto: SongCreate, db:Session = Depends(get_db)): # va a pasar el titulo, artista y los opcionales los puede pasar o no.
    if not song_dto.title.strip(): # strip se usa para quitar los espacios que molestan (principio y final).
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El título no puede estar vacío"
        )
    if not song_dto.artist.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El artista de la canción no puede estar vacío"
        )
    
    if song_dto.duration_seconds is not None and song_dto.duration_seconds < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La duración debe ser un número positivo"
        )
    
    # crea objeto Song con datos validados
    song = Song(
        title=song_dto.title.strip(),
        artist=song_dto.artist.strip(),
        duration_seconds=song_dto.duration_seconds,
        explicit=song_dto.explicit
    )
    
    db.add(song) # agrega el objeto a la sesión, no a la bd
    db.commit() # confirma la creación en base de datos(guarda en bd)
    db.refresh(song) # refresca el objeto para obtener el id generado
    return song # retorna la canción creada (devuelve)

# PUT - actualizar COMPLETAMENTE una canción
@app.put("/api/songs/{id}", response_model=SongResponse)
def update_full(id: int, song_dto: SongUpdate, db: Session = Depends(get_db)):
    # busca canción por id
    song = db.execute(
        select(Song).where(Song.id == id)
    ).scalar_one_or_none()
    
    # si no existe, devuelve 404
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado la canción con id {id}"
        )
    
    # validaciones (igual que en POST)(no son obligatorias pero es ecomendable ponerlas)
    if not song_dto.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El artista de la canción no puede estar vacío"
        )
    
    if not song_dto.artist.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El artista de la canción no puede estar vacío"
        )
    
    if song_dto.duration_seconds is not None and song_dto.duration_seconds < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La duración debe ser un número positivo"
        )
    #debemos actualizar todos los campos, ya no hay que crear una variable, se ha creado (song=db.execute) antes
    song.title = song_dto.title.strip()
    song.artist = song_dto.artist.strip()
    song.duration_seconds = song_dto.duration_seconds
    song.explicit = song_dto.explicit
    
    db.commit() # confirma los cambios (guarda)
    db.refresh(song) # refresca el objeto de la base de datos
    return song # retorna la canción actualizada (devuelve)

# PATCH - actualizar PARCIALMENTE una canción
@app.patch("/api/songs/{id}", response_model=SongResponse)
def update_partial(id: int, song_dto: SongPatch, db: Session = Depends(get_db)):
    # busca canción por id
    song = db.execute(
        select(Song).where(Song.id == id)
    ).scalar_one_or_none()
    
    # si no existe, devuelve 404
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado la canción con id {id}"
        )
    
    # actualiza SÓLO los campos que se han enviado (no son None), hay que hacer la misma comprobación de antes. 
    if song_dto.title is not None:
        if not song_dto.title.strip():
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El título de la canción no puede estar vacío"
        )
        song.title = song_dto.title.strip()
    
    if song_dto.artist is not None:
        if not song_dto.artist.strip():
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El artista de la canción no puede estar vacío"
        )
        song.artist = song_dto.artist.strip()
    
    if song_dto.duration_seconds is not None:
        if song_dto.duration_seconds < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La duración debe ser un número positivo"
            )
        song.duration_seconds = song_dto.duration_seconds
    
    if song_dto.explicit is not None:
        song.explicit = song_dto.explicit
    
    db.commit() # confirma los cambios en base datos
    db.refresh(song) # refresca el objeto
    return song

# DELETE

@app.delete("/api/song/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id:int, db: Session = Depends(get_db)):
    #busca la canción por id
    song = db.execute(
        select(song).where(Song.id == id)        
    ).scalar_one_or_none()
    
    # Si no existe, colocar 404
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            detail=f"No se ha encontrado la canción con el id {id}"
        ) 
    # Para elimina la cancion de bd
    db.delete(song)# marca el objeto para eliminacion
    db.commit() # Confirma eliminacion en bd
    return None
        
   
        
        
        
        