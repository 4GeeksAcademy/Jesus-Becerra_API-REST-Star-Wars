import os
from flask_admin import Admin
from models import db, User, Characters, Planets, FavoriteCharacters, FavoritePlanets
from flask_admin.contrib.sqla import ModelView

class FavoriteCharactersModelView(ModelView):
    column_auto_selected_related = True
    column_list = ['id', 'user_id', 'users', 'character_id', 'character']

class FavoritePlanetsModelView(ModelView):
    column_auto_selected_related = True
    column_list = ['id', 'user_id', 'users', 'planet_id', 'planet']

class UserModelView(ModelView):
    column_auto_selected_related = True
    column_list = ['id', 'name', 'last_name', 'email', 'password', 'favorites_characters', 'favorites_planets', 'is_ative']

class CharactersModelView(ModelView):
    column_auto_selected_related = True
    column_list = ['id', 'name', 'height', 'weight', 'favorite_character_by']

class PlanetsMmodelView(ModelView):
    column_auto_selected_related = True
    column_list = ['id', 'name', 'favorite_planet_by']

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(CharactersModelView(Characters, db.session))
    admin.add_view(PlanetsMmodelView(Planets, db.session))
    admin.add_view(FavoriteCharactersModelView(FavoriteCharacters, db.session))
    admin.add_view(FavoritePlanetsModelView(FavoritePlanets, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))