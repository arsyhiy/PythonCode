import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('homedrive'), \
                                os.getenv('homepath'), \
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('home'), 'test.log')

print('сохраняем лог в ', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format= '%(asctime)s : %(levelname)s :%(message)s' ,
    filename= logging_file,
    filemode= 'w',
)

logging.debug('начало программы')
logging.info("какието действия")
logging.warning('программа умирает')