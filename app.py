import motor
from tornado.web import Application
from core.urls import urlpatterns as core_urlpatterns
from settings import DATABASE_NAME, DATABASE_URI

def create_app():
    db_client = motor.motor_tornado.MotorClient(DATABASE_URI)
    urlpatterns = [
        *core_urlpatterns,
    ]

    app = Application(
        urlpatterns,
        debug=True,
        db_client=db_client,
        db_name=DATABASE_NAME,
    )

    return app
