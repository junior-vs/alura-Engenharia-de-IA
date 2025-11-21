"""Example domain entity."""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4


@dataclass
class Entity:
    """Base entity class."""
    id: UUID
    created_at: datetime
    updated_at: datetime

    def __eq__(self, other: object) -> bool:
        """Check equality based on id."""
        if not isinstance(other, Entity):
            return False
        return self.id == other.id


# Example domain entity
@dataclass
class Document(Entity):
    """Document entity representing a document in the system."""
    title: str
    content: str
    metadata: Optional[dict[str, str]] = None
    
    @staticmethod
    def create(title: str, content: str, metadata: Optional[dict[str, str]] = None) -> "Document":
        """Factory method to create a new document."""
        now = datetime.utcnow()
        return Document(
            id=uuid4(),
            created_at=now,
            updated_at=now,
            title=title,
            content=content,
            metadata=metadata or {},
        )
