# cdktf-docker-nginx-container

CDKTF app that deploys an NGINX container to Docker.

## Prerequisites

For this project you need Docker to be installed on your system.

## Installation

Install CDKTF:

```sh
npm install -g cdktf
```

Install Poetry + dotenv plugin:

```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry self add poetry-plugin-dotenv
```

Configure Poetry to create the virtualenv inside the project's root directory:

```sh
poetry config virtualenvs.in-project true
```

Create the virtualenv and install all the dependencies inside it:

```sh
poetry install
```

## Deployment

Synthesize the Terraform stack and deploy it:

```sh
cdktf deploy
```

## Cleanup

Destroy the Terraform stack:

```sh
cdktf destroy
```
