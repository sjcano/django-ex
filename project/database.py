import os

from django.conf import settings


engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}


def url():
    engine = os.getenv('DATABASE_ENGINE')
    host = os.getenv('{}_SERVICE_HOST'.format(service_name))
    port = os.getenv('{}_SERVICE_PORT'.format(service_name))
    user = os.getenv('DATABASE_USER')
    password = os.getenv('DATABASE_PASSWORD')
    name = os.getenv('DATABASE_NAME')
    # engine://user:password@host:port/name
    url = "%s://%s:%s@%s:%s/%s" % (engine, user, password, host, port, name)
    return url
    
def config():
    service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper()
    if service_name:
        # engine = engines.get(os.getenv('DATABASE_ENGINE'), engines['sqlite'])
        engine = engines.get(os.getenv('DATABASE_ENGINE'), engines['mysql'])
    else:
        engine = engines['sqlite']
    name = os.getenv('DATABASE_NAME')
    if not name and engine == engines['sqlite']:
        name = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    return {
        'ENGINE': engine,
        'NAME': name,
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('{}_SERVICE_HOST'.format(service_name)),
        'PORT': os.getenv('{}_SERVICE_PORT'.format(service_name)),
    }
