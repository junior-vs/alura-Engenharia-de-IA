"""In-memory implementation of document repository for testing."""
from typing import Optional
from uuid import UUID

from domain.entities.document import Document
from domain.repositories.document_repository import IDocumentRepository


class InMemoryDocumentRepository(IDocumentRepository):
    """In-memory implementation following Dependency Inversion Principle."""

    def __init__(self) -> None:
        self._documents: dict[UUID, Document] = {}

    async def save(self, document: Document) -> Document:
        """Save a document."""
        self._documents[document.id] = document
        return document

    async def find_by_id(self, document_id: UUID) -> Optional[Document]:
        """Find a document by ID."""
        return self._documents.get(document_id)

    async def find_all(self, skip: int = 0, limit: int = 100) -> list[Document]:
        """Find all documents with pagination."""
        documents = list(self._documents.values())
        return documents[skip : skip + limit]

    async def delete(self, document_id: UUID) -> bool:
        """Delete a document."""
        if document_id in self._documents:
            del self._documents[document_id]
            return True
        return False
