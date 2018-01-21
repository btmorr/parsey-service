import logging
import subprocess as sp
from pyramid.response import Response


log = logging.getLogger(__name__)


def hello_world(request):
    log.debug(request)
    return Response('<body><h1>Hello World!</h1></body>')


def echo(request):
    return Response(request.text)


def parse(request):
    parser_input = request.json['input']
    log.debug("Parsing: {}".format(parser_input))
    command = 'echo "{}" | syntaxnet/demo.sh 2> /dev/null'.format(parser_input)
    res = sp.check_output(command, shell=True).strip()
    return Response(res)
