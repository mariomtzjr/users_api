from flask_marshmallow import Marshmallow

from app.main.models import User

ma = Marshmallow()


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        # Fields to expose
        fields = ("id", "username", "avatar_url", "type", "url")