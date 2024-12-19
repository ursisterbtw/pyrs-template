# 🐍 pyrs-template 🦀

## Python + Rust Template with Shared Library Support

This template provides a development environment for Python and Rust projects with shared library capabilities.

### Features

- Pre-configured development container with Python and Rust
- Pre-commit hooks for code quality:
  - Ruff for Python linting and formatting
  - `cargo fmt` for Rust formatting
- VS Code integration with recommended extensions
- GitHub Actions for CI/CD

### Setup

1. Clone this repository
2. Open in VS Code with Dev Containers extension
3. Pre-commit hooks will be automatically installed

### Development

- Python code will be automatically formatted and linted using Ruff
- Rust code will be automatically formatted using `cargo fmt`
- All formatting checks will run before each commit

### Notes

#### Build the image (from the directory containing .devcontainer)

```bash
docker buildx build . -f .devcontainer/Dockerfile -o type=docker -t pyrs-dev
```

#### Run the container

```bash
docker run -it --name pyrs-dev -v "${PWD}:/app" pyrs-dev
```

#### If you want to enter a running container later

```bash
docker exec -it pyrs-dev bash
```

#### Stop and remove the container + all volumes

```bash
docker stop pyrs-dev
docker rm pyrs-dev
docker system prune -a --volumes
```

#### Rebuild and run the container

```bash
docker buildx build . -f .devcontainer/Dockerfile -o type=docker -t pyrs-dev
docker run -it --name pyrs-dev -v "${PWD}:/app" pyrs-dev
```
