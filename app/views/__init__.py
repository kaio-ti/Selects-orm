from flask import Flask



def init_app(app:Flask):
    from app.views.grupos_views import bp_grupos
    app.register_blueprint(bp_grupos)