import logging


def exception_logger(exception, mode="console"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger(func.__name__)
                formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
                if mode == "console":
                    console_handler = logging.StreamHandler()
                    console_handler.setFormatter(formatter)
                    logger.addHandler(console_handler)
                elif mode == "file":
                    file_handler = logging.FileHandler("error.log")
                    file_handler.setFormatter(formatter)
                    logger.addHandler(file_handler)
                else:
                    raise ValueError("Invalid logging mode.")

                logger.setLevel(logging.ERROR)
                logger.error(f"{type(e).__name__}: {str(e)}")

        return wrapper

    return decorator


