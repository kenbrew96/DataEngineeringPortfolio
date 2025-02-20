import logging

def setup_application_logging():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Application logging setup completed.')

if __name__ == '__main__':
    setup_application_logging()

