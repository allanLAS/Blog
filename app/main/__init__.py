from flask import Blueprint
from flask_bootstrap import Bootstrap

main = Blueprint('main', __name__)

from . import views, errors
