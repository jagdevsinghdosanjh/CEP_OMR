import logging

def setup_logger(name="omr_logger", log_file="omr_debug.log", level=logging.INFO):
    """
    Sets up a logger for debugging and diagnostics.
    """
    formatter = logging.Formatter('%(asctime)s — %(levelname)s — %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

# Example usage
logger = setup_logger()

def log_bubble_count(count):
    logger.info(f"🟢 Detected {count} bubbles")

def log_response_mapping(mapped, expected):
    logger.info(f"✅ Mapped {mapped}/{expected} responses")

def log_metadata(metadata):
    logger.info(f"📋 Metadata: {metadata}")
