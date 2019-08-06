import logging
import logging.config

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename='app.log'
# )
logging.config.fileConfig('logging.cnf')

logging.debug('debug mess')
logging.info('info mess')
logging.warn('warn mess')
logging.error('err mess')
logging.critical('critical mess')
