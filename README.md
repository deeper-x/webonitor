# Web On it (or write IT) 

![Python application](https://github.com/deeper-x/webonitor/workflows/Python%20application/badge.svg)

System service: writing a resource, it pushes content to the provider.
Web application: tail queue (in real time)   

## Getting Started

```bash
make run
```


### Prerequisites

- Python3.8 ([Download](https://www.python.org/downloads/))
- Docker
- RabbitMQ 

### Run

```bash
$ git clone <remote_url>
$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
$ python3.8 -m pip install pipenv
$ python3.8 -m pipenv --python 3.8
$ pipenv shell
$ pipenv install
$ python main.py
```

## Running the tests

```bash
make test
```


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Alberto de Prezzo** - 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



