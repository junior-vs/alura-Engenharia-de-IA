# Architecture Documentation

## Clean Architecture Layers

### 1. Domain Layer (Enterprise Business Rules)
The innermost layer containing:
- **Entities**: Core business objects with identity
- **Value Objects**: Immutable objects defined by their attributes
- **Repository Interfaces**: Abstract definitions for data access
- **Domain Services**: Business logic that doesn't belong to a single entity
- **Domain Events**: Events representing business state changes
- **Exceptions**: Domain-specific errors

**Dependencies**: None (completely independent)

### 2. Application Layer (Application Business Rules)
Contains use cases that orchestrate the flow of data:
- **Use Cases**: Application-specific business rules
- **DTOs**: Data transfer objects for crossing boundaries
- **Interfaces**: Abstractions for external services
- **Application Services**: Coordinate use cases

**Dependencies**: Domain Layer only

### 3. Infrastructure Layer (Frameworks & Drivers)
Implementation details:
- **Database**: ORM models, repositories, migrations
- **External Services**: Third-party integrations
- **Messaging**: Event bus, message queue implementations
- **Logging**: Structured logging setup
- **Config**: Environment and configuration management

**Dependencies**: Domain and Application layers

### 4. Presentation Layer (Interface Adapters)
User-facing interfaces:
- **API**: RESTful HTTP endpoints (FastAPI)
- **CLI**: Command-line interface (Click)
- **Controllers**: Handle requests and responses
- **Serializers**: Transform data for presentation
- **Validators**: Input validation

**Dependencies**: Application layer

## SOLID Principles Applied

### Single Responsibility Principle (SRP)
- Each use case has one reason to change
- Repositories handle only data persistence
- Controllers handle only HTTP concerns

### Open/Closed Principle (OCP)
- New use cases added without modifying existing code
- Repository pattern allows different implementations

### Liskov Substitution Principle (LSP)
- Repository implementations are interchangeable
- Mock repositories for testing

### Interface Segregation Principle (ISP)
- Focused repository interfaces
- Specific DTOs for each operation

### Dependency Inversion Principle (DIP)
- High-level modules depend on abstractions
- Repository interfaces in domain, implementations in infrastructure
- Dependency injection throughout

## Domain-Driven Design (DDD)

### Strategic Design
- **Bounded Contexts**: Clear module boundaries
- **Ubiquitous Language**: Domain concepts in code

### Tactical Design
- **Entities**: Objects with identity (Document)
- **Value Objects**: Immutable descriptive objects
- **Aggregates**: Consistency boundaries
- **Repositories**: Collection-like interfaces for aggregates
- **Domain Events**: State change notifications
- **Domain Services**: Stateless operations

## Dependency Flow

```
Presentation → Application → Domain ← Infrastructure
```

All dependencies point inward toward the domain.

## Testing Strategy

### Unit Tests
- Test domain logic in isolation
- Test use cases with mock repositories
- Fast, no external dependencies

### Integration Tests
- Test API endpoints
- Test database operations
- Test external service integrations

### E2E Tests
- Test complete workflows
- Test CLI commands
- Test API scenarios

## Best Practices

1. **Keep domain pure**: No framework dependencies in domain layer
2. **Use dependency injection**: Pass dependencies through constructors
3. **Program to interfaces**: Depend on abstractions, not implementations
4. **Immutability**: Prefer immutable data structures
5. **Functional core, imperative shell**: Pure functions in domain, side effects at boundaries
6. **Fail fast**: Validate at boundaries
7. **Explicit over implicit**: Clear, readable code over clever code
