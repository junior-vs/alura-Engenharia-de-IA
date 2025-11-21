# RAG-First

A RAG (Retrieval-Augmented Generation) application built with Clean Architecture, Domain-Driven Design (DDD), and SOLID principles.

## 🏗️ Architecture

This project follows Clean Architecture principles with the following layers:

### Domain Layer (`src/domain/`)
- **entities/**: Core business entities
- **value_objects/**: Immutable value objects
- **repositories/**: Repository interfaces (abstractions)
- **services/**: Domain services containing business logic
- **events/**: Domain events for event-driven architecture
- **exceptions/**: Domain-specific exceptions

### Application Layer (`src/application/`)
- **use_cases/**: Application use cases (orchestration)
- **dto/**: Data Transfer Objects
- **interfaces/**: Application service interfaces
- **services/**: Application services

### Infrastructure Layer (`src/infrastructure/`)
- **database/**: Database implementations
  - **repositories/**: Repository implementations
  - **models/**: ORM models
  - **migrations/**: Database migrations
- **external_services/**: Third-party service integrations
- **messaging/**: Message broker implementations
- **logging/**: Logging configuration
- **config/**: Configuration management

### Presentation Layer (`src/presentation/`)
- **api/**: RESTful HTTP API (FastAPI)
  - **controllers/**: API controllers
  - **routes/**: Route definitions
  - **middleware/**: HTTP middleware
  - **serializers/**: Request/response serializers
  - **validators/**: Input validators
- **cli/**: Command-line interface (Click)
  - **commands/**: CLI command definitions
  - **handlers/**: Command handlers

### Shared (`src/shared/`)
- **utils/**: Common utilities
- **constants/**: Application constants
- **decorators/**: Reusable decorators
- **types/**: Custom type definitions

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip or poetry

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd rag-first

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

### Running the Application

#### REST API
```bash
rag-first-api
# or
uvicorn src.presentation.api.main:app --reload
```

#### CLI
```bash
rag-first --help
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test types
pytest tests/unit/
pytest tests/integration/
pytest tests/e2e/
```

## 📁 Project Structure

```
rag-first/
├── src/
│   ├── domain/              # Enterprise business rules
│   ├── application/         # Application business rules
│   ├── infrastructure/      # External implementations
│   ├── presentation/        # Interface adapters (API, CLI)
│   └── shared/             # Common utilities
├── tests/
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── e2e/                # End-to-end tests
├── config/                 # Configuration files
├── scripts/                # Utility scripts
├── docs/                   # Documentation
└── pyproject.toml         # Project configuration
```

## 🧪 Development

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
ruff src/ tests/

# Type checking
mypy src/
```

### Pre-commit Hooks

```bash
pre-commit install
pre-commit run --all-files
```

## 📝 License

MIT License
