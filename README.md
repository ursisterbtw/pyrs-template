# 🐍 pyrs-template 🦀

## Python + Rust Template with Shared Library Support

This template provides a development environment for Python and Rust projects with shared library capabilities.

### Features:
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