import logging
from logging.handlers import RotatingFileHandler


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


requests_logger = logging.getLogger("requests")
requests_handler = RotatingFileHandler("requests.log")
requests_logger.addHandler(requests_handler)


validations_logger = logging.getLogger("validations")
# validations_handler = RotatingFileHandler("validations.log", maxBytes=5000000, backupCount=5)
validations_handler = RotatingFileHandler("validations.log")
validations_logger.addHandler(validations_handler)


general_logger = logging.getLogger("general")
general_handler = RotatingFileHandler("general.log")
general_logger.addHandler(general_handler)


def log_program_start():
    general_logger.info("Program started")

def log_program_stop(reason="Normal exit"):
    general_logger.info(f"Program stopped. Reason: {reason}")


log_program_start()
log_program_stop("Maintenance mode")
