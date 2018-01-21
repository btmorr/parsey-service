import logging
from waitress import serve
from pyramid.config import Configurator
from parsey import handlers


log = logging.getLogger(__name__)


def main():
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(handlers.hello_world, route_name='hello')

        config.add_route('echo', '/echo')
        config.add_view(handlers.echo, route_name='echo')

        config.add_route('parse', '/parse', request_method='POST')
        config.add_view(handlers.parse, route_name='parse')

        srv = config.make_wsgi_app()

    host = '0.0.0.0'
    port = 6543
    log.info("Starting PMcP server on {}:{}".format(host, port))
    serve(srv, host=host, port=port)


if __name__ == '__main__':
    fmt = '%(asctime)-15s %(name)s %(levelname)s [Line %(lineno)s] %(message)s'
    logging.basicConfig(format=fmt, level=logging.DEBUG)

    main()
