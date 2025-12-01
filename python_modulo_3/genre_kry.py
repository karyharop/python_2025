from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker, Session
from sqlalchemy import String, Integer, create_engine, ForeignKey, select


app = FastAPI()


DATABASE_URL = "sqlite:///./genre.db"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=True,
    expire_on_commit=False
)

class Genre(BaseModel):
    name_genre: str
     
# MODELO...

class Base(DeclarativeBase):
    pass

class GenreORM(Base):
    __tablename__= "genero"
    
    genero_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name_genre: Mapped[str] = mapped_column(String(200), nullable=False)
    

class GenreResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True) 
    id: int
    name_genre: str
     

class GenreCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name_genre: str
      

class GenrePatch(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    name_genre: str | None = None
    
      
Base.metadata.create_all(engine)

def init_db():
    
    db = SessionLocal()
    try:
        existing_genres = db.execute(select(GenreORM)).scalars().all()
        if existing_genres:
            return  
        default_genres = [
            GenreORM(genero_id=1, name_genre="Acción"),
            GenreORM(genero_id=2,name_genre="Comedia"),
            GenreORM(genero_id=3,name_genre="Drama"),
            GenreORM(genero_id=4,name_genre="Terror"),
            GenreORM(genero_id=5, name_genre="Anime"),
            GenreORM(genero_id=6, name_genre="Animación"),
            GenreORM(genero_id=7, name_genre="Comedia Negra")
            
        ]
        db.add_all(default_genres)
        db.commit() 
    finally:
        db.close()
# esto del genero debo revisarlo, porque creo que con el id, ya está definido el nombre... sería como repetir.
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()



# APLICACIÓN FASTAPI

# crea la instancia de la aplicación FastAPI
app = FastAPI(title="películas", version="1.0.0")

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la app Películas"}

# Revisar el mensaje...

# ENDPOINTS CRUD

# GET - obtener TODAS las canciones
@app.get("/api/genero", response_model=list[GenreResponse])
def find_all(db: Session = Depends(get_db)):# me permite hacer operacones en la base de datos.
   
    return db.execute(select(Genre)).scalars().all()

# GET - obtener UNA canción por id
@app.get("api/generos/{id}", response_model=GenreResponse)
def find_all(db: Session = Depends(get_db)):
    return db.execute(select(Genre)).scalars().all()

# get para obtener un genero

@app.get("/api/genres", response_model=GenreResponse)
def find_by_id(id:int, db: Session = Depends(get_db)):
    genre = db.execute(
        select(Genre). where(Genre.id == id)
    ).scalar_one_or_none()

    
    if not Genre: # si no hay nada, lanza la excepcion, lanza este codigo 404. 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado la canción con id {id}"
        )
    return Genre







# POST - crear una nueva cancion 

@app.post("api/generos", response_model=GenreResponse, status_code=status. HTTP_201_CREATED)
def create(genre_dto: GenreCreate, db:Session = Depends(get_db)): 
    if not genre_dto.name_genre.strip(): 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este campo no puede estar vacío"
        )
    
    
    # crea objeto Song con datos validados
    genre = Genre(
        name_genre=genre_dto.name_genre.strip(),
    )
          
    db.add(genre) 
    db.commit() 
    db.refresh(genre) 
    return genre 



# PATCH - actualizar PARCIALMENTE una canción
@app.patch("/api/genre/{id}", response_model=GenreResponse)
def update_partial(id: int, genre_dto: GenrePatch, db: Session = Depends(get_db)):
    genre = db.execute(
        select(Genre).where(Genre.id == id)
    ).scalar_one_or_none()
    
    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado el genero con id {id}"
        )
    

    if genre_dto.name_genre is not None:
        if not genre_dto.name_genre.strip():
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El género de la película no puede estar vacío"
        )
        genre.name_genre = genre_dto.name_genre.strip()
     
    db.commit() 
    db.refresh(genre) 
    return genre

# DELETE

@app.delete("/api/genre/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id:int, db: Session = Depends(get_db)):
    #busca la canción por id
    genre = db.execute(
        select(genre).where(Genre.id == id)        
    ).scalar_one_or_none()
    
    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se ha encontrado el género con el id {id}"
        ) 
   
    db.delete(genre)
    db.commit() 
    return None
        
   
        
        
        
        



   
