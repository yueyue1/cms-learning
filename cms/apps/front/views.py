from flask import Blueprint,render_template
from flask_sqlalchemy import get_debug_queries
import logging
from logging.handlers import RotatingFileHandler
from config import FLASK_DB_QUERY_TIMEOUT

bp = Blueprint('front',__name__)

@bp.route('/')
def index():
    return render_template('front/index.html')

@bp.after_app_request
def after_request(response):
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
    )
    handler = RotatingFileHandler('slow_query.log',maxBytes=10000, backupCount=10)
    handler.setLevel(logging.WARN)
    handler.setFormatter(formatter)
    logger = logging.getLogger("logger")
    logger.addHandler(handler)
    for query in get_debug_queries():
        if query.duration >= FLASK_DB_QUERY_TIMEOUT:
            logger.warning(
                ('\nContext:{}\nSLOW QUERY:{}\nParameters:{}\nSTART_TIME:{}\nDuration:{}\n'
            ).format(query.context,
                     query.statement,
                     query.parameters,
                     query.start_time,
                     query.duration))
    return response

@bp.app_errorhandler
def error_404(error):
    return render_template('front/404.html'), 404