"""Use case for creating a document."""
from dataclasses import dataclass
from typing import Optional

from domain.entities.document import Document
from domain.repositories.document_repository import IDocumentRepository
from application.dto.document_dto import CreateDocumentDTO, DocumentDTO


@dataclass
class CreateDocumentUseCase:
    """Use case for creating a new document following Single Responsibility Principle."""
    
    document_repository: IDocumentRepository

    async def execute(self, dto: CreateDocumentDTO) -> DocumentDTO:
        """Execute the use case."""
        # Create domain entity
        document = Document.create(
            title=dto.title,
            content=dto.content,
            metadata=dto.metadata,
        )
        
        # Save using repository
        saved_document = await self.document_repository.save(document)
        
        # Return DTO
        return DocumentDTO.from_entity(saved_document)
