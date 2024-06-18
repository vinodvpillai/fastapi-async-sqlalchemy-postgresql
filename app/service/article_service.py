from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.article_repository import ArticleRepository
from app.dto.article_dto import ArticleCreateDTO, ArticleUpdateDTO

class ArticleService:

    def __init__(self, db: AsyncSession):
        self.repository = ArticleRepository(db)

    async def get_article(self, article_id: int):
        return await self.repository.get_article(article_id)

    async def create_article(self, article: ArticleCreateDTO):
        return await self.repository.create_article(article)

    async def update_article(self, article_id: int, article: ArticleUpdateDTO):
        return await self.repository.update_article(article_id, article)

    async def delete_article(self, article_id: int):
        return await self.repository.delete_article(article_id)

    async def get_articles(self, skip: int = 0, limit: int = 10):
        return await self.repository.get_articles(skip, limit)
