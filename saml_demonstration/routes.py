from ast import arg
from collections import namedtuple
from auth.v1 import auth_bp as auth_bp_v1
from auth.v2 import auth_bp as auth_bp_v2


def base(base_path, **opt_kwargs):
    final_base_path: str = '/{base}/{version}/{value}'
    def _wrapper(func):
        version = opt_kwargs.get('version', func.__name__)
        def wrapper(*args, **kwargs):
            args += (lambda value: {
                'url_prefix': final_base_path.format(
                        base = base_path.strip('/'),
                        version = version.strip('/'),
                        value = value.strip('/')
                    )
                },)
            return func(*args, **kwargs)
        return wrapper
    return _wrapper
    
def api_routes(app):
    @base('/api', version='v1')
    def v1(path):
        app.register_blueprint(auth_bp_v1, **path('/auth'))
    @base('/api')
    def v2(path):
        app.register_blueprint(auth_bp_v2, **path('/auth'))

    return namedtuple('routes','v1 v2')(
        v1=v1,
        v2=v2
    )
