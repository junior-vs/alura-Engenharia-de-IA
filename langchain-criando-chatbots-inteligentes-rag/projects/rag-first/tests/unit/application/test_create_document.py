"""Example test for CreateDocumentUseCase."""
import pytest
from uuid import UUID

from application.use_cases.create_document import CreateDocumentUseCase
from application.dto.document_dto import CreateDocumentDTO
from infrastructure.database.repositories.in_memory_document_repository import (
    InMemoryDocumentRepository,
)


@pytest.mark.asyncio
async def test_create_document_use_case() -> None:
    """Test creating a document."""
    # Arrange
    repository = InMemoryDocumentRepository()
    use_case = CreateDocumentUseCase(document_repository=repository)
    dto = CreateDocumentDTO(
        title="Test Document",
        content="This is test content",
        metadata={"author": "Test Author"},
    )

    # Act
    result = await use_case.execute(dto)

    # Assert
    assert result.title == "Test Document"
    assert result.content == "This is test content"
    assert result.metadata == {"author": "Test Author"}
    assert isinstance(result.id, UUID)
    
    # Verify it was saved
    saved_doc = await repository.find_by_id(result.id)
    assert saved_doc is not None
    assert saved_doc.title == "Test Document"
