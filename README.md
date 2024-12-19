# 🐍 pyrs-template 🦀

A development environment template for Python, Rust, and Node.js projects with shared library capabilities.

## Features

- Multi-stage Docker build with minimal final image
- Python 3.x and Rust toolchain
- Node.js 20.x with npm
- Pre-configured development container
- Pre-commit hooks for code quality
- GitHub Actions CI/CD
- VS Code integration

## Quick Start

### Prerequisites

- Docker
- VS Code with Dev Containers extension (optional)

### Development Container

Build the image:

```bash
docker buildx build . -f .devcontainer/Dockerfile -o type=docker -t pyrs-dev
```

Run the container:

```bash
docker run -it --name pyrs-dev -v "${PWD}:/app" pyrs-dev
```

Enter a running container:

```bash
docker exec -it pyrs-dev bash
```

### Clean Up

Stop and remove everything:

```bash
docker stop pyrs-dev
docker rm pyrs-dev
docker system prune -a --volumes
```

## Development

- Python code is formatted with `black` and linted with `ruff`
 Rust code is formatted with `rustfmt` and linted with `clippy`
 Node.js packages managed with `npm`

 Tests are run with `pytest` for Python and `cargo test` for Rust

## VS Code Integration

Open the project in VS Code and click "Reopen in Container" when prompted.

## License

MIT
