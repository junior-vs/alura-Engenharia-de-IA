"""Data Transfer Objects for documents."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from domain.entities.document import Document


@dataclass
class CreateDocumentDTO:
    """DTO for creating a document."""
    title: str
    content: str
    metadata: Optional[dict[str, str]] = None


@dataclass
class DocumentDTO:
    """DTO for document response."""
    id: UUID
    title: str
    content: str
    metadata: Optional[dict[str, str]]
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_entity(document: Document) -> "DocumentDTO":
        """Create DTO from domain entity."""
        return DocumentDTO(
            id=document.id,
            title=document.title,
            content=document.content,
            metadata=document.metadata,
            created_at=document.created_at,
            updated_at=document.updated_at,
        )
