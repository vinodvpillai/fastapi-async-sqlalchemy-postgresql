from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.model.article import Article
from app.dto.article_dto import ArticleCreateDTO, ArticleUpdateDTO

class ArticleRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_article(self, article_id: int):
        result = await self.db.execute(select(Article).where(Article.id == article_id))
        return result.scalar_one_or_none()

    async def create_article(self, article: ArticleCreateDTO):
        db_article = Article(**article.dict())
        self.db.add(db_article)
        await self.db.commit()
        await self.db.refresh(db_article)
        return db_article

    async def update_article(self, article_id: int, article: ArticleUpdateDTO):
        db_article = self.get_article(article_id)
        if db_article:
            update_data = article.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_article, key, value)
            await self.db.commit()
            await self.db.refresh(db_article)
        return db_article

    async def delete_article(self, article_id: int):
        db_article = self.get_article(article_id)
        if db_article:
            await self.db.delete(db_article)
            await self.db.commit()
        return db_article

    async def get_articles(self, skip: int = 0, limit: int = 10):
        return self.db.scalars(select(Article).offset(skip).limit(limit))
