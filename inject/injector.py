
from config.log_config import create_log
from service.handler.util_handler import Utils
from service.rest_api_service import ServiceHandler

logger = create_log()

util = Utils(logger=logger)
service_inject = ServiceHandler(util=util, logger=logger)
