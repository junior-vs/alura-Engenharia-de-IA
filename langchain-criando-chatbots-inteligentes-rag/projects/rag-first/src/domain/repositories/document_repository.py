"""Repository interface for documents."""
from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from domain.entities.document import Document


class IDocumentRepository(ABC):
    """Interface for document repository following Repository pattern."""

    @abstractmethod
    async def save(self, document: Document) -> Document:
        """Save a document."""
        pass

    @abstractmethod
    async def find_by_id(self, document_id: UUID) -> Optional[Document]:
        """Find a document by ID."""
        pass

    @abstractmethod
    async def find_all(self, skip: int = 0, limit: int = 100) -> list[Document]:
        """Find all documents with pagination."""
        pass

    @abstractmethod
    async def delete(self, document_id: UUID) -> bool:
        """Delete a document."""
        pass
