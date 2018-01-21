# Parsey McParseface as a Service

A simple Dockerized server to feed input strings to Parsey McParseface.

## Use

To build and run the server:

```bash
$ docker build -t pmpaas:0.1 .
$ docker run -p 6543:6543 -t pmpaas:0.1
```

Then make a POST request to http://localhost:6543/parse with a JSON body
containing the key 'input' and the sentence to be parsed as the value.
E.g.:

```json
{
  "input": "This is an example sentence."
}
```

The body of the server response will be the stdout from Parsey.

## Dev Notes

This project is currently in Python 2, as
[tensorflow](https://github.com/tensorflow) does not support Python 3.

In order to avoid having to cusomize the demo.sh file from syntaxnet,
the web server relies on being executed from a specific working
directory (specifically `/root/models/syntaxnet`). The way around this
would be to maintain a list of relative path roots used in demo.sh
(such as `bazel-bin`) and create symlinks for each of these in the
present working directory when the server is started (and then clean
them up after), but given that the server is Dockerized, it is more
expedient for now to leave the relative path requirment unmitigated.
