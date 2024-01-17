class Config:
    '''Base configuration class for the Flask app'''


class DevConfig(Config):
    '''Class for development configuration'''
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'W52ZXWUDGuUc1hq00eATyZchZL22mh0Y'
    OIDC_CLIENT_SECRETS = 'client_secrets.json'
    OIDC_ID_TOKEN_COOKIE_SECURE = False
    OIDC_REQUIRE_VERIFIED_EMAIL = False
    OIDC_USER_INFO_ENABLED = True
    OIDC_SCOPES = ['openid', 'email', 'profile']
    OIDC_INTROSPECTION_AUTH_METHOD = 'client_secret_post'
    FIRECREST_IP='http://kong:8000'
    MACHINES=['cluster']
    PARTITIONS={'cluster':['debug','batch','serial','gpu']}
    MICROSERVICES=['status', 'compute', 'utilities', 'storage', 'tasks']

    # machine for internal storage jobs, must be defined in MACHINES
    STORAGE_JOBS_MACHINE='cluster'
    HOME_DIR = '/home'
    CLIENT_PORT = 7000

    # SSL configuration
    USE_SSL = False
    SSL_PEM = ''
    SSL_KEY = ''
