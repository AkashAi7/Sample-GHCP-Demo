# GitHub Copilot Custom Instructions

These instructions are automatically picked up by GitHub Copilot to provide consistent coding style and repository-specific context.

## Coding Standards
- **Always use Python Type Hints** for function signatures.
- **Prefer f-strings** over `.format()` or `%` formatting.
- **Async First**: Use `async`/`await` for I/O bound operations when using libraries like `azure-cosmos`.
- **Documentation**: All public methods in `services/` must have a docstring following the Google Python Style Guide.

## Project Context
- This is a Smart Home Energy Monitor project.
- Data models are located in `models/`.
- Logic is strictly separated into `services/`.
- We use `azure-cosmos` for data persistence.
