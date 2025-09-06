from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    favorites_characters: Mapped[list['FavoriteCharacters']] = relationship(back_populates='users')
    favorites_planets: Mapped[list['FavoritePlanets']] = relationship(back_populates='users')
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

class Characters(db.Model):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[int] = mapped_column(Integer, nullable=False)
    favorite_character_by: Mapped[list['FavoriteCharacters']] = relationship(back_populates='character')

class Planets(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    favorite_planet_by: Mapped[list['FavoritePlanets']] = relationship(back_populates='planet')

class FavoriteCharacters(db.Model):
    __tablename__ = 'favorite_characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    users: Mapped['User'] = relationship(back_populates='favorites_characters')
    character_id: Mapped[int] = mapped_column(ForeignKey('character.id'))
    character: Mapped['Characters'] = relationship(back_populates='favorite_character_by')

class FavoritePlanets(db.Model):
    __tablename__ = 'favorite_planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    users: Mapped['User'] = relationship(back_populates='favorites_planets')
    planet_id: Mapped[int] = mapped_column(ForeignKey('planet.id'))
    planet: Mapped['Planets'] = relationship(back_populates='favorite_planet_by')


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }