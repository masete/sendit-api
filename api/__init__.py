from flask import Flask


def create_app():

    app = Flask(__name__)
    from api.views.controllers import parcel_blueprint as parcel_blueprint
    from api.views.controllers import user_blueprint as user_blueprint

    app.register_blueprint(parcel_blueprint)
    app.register_blueprint(user_blueprint)

    return app
