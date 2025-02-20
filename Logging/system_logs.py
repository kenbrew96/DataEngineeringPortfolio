import logging

def setup_system_logging():
    logging.basicConfig(level=logging.INFO)
    logging.info('System logging setup completed.')

if __name__ == '__main__':
    setup_system_logging()

