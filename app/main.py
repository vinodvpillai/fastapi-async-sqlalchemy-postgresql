from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.controller.article_controller import article_router
from app.core.log_middleware import LoggingMiddleware
from app.core.env_settings import settings
from app.core.database import sessionmanager, Base
from contextlib import asynccontextmanager
# Not required now integrated - Alembic for managing database migrations
#from app.core.initialize_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    # Database initialization - Create necessary tables
    # await init_db() 
    # Above line not required now integrated - Alembic for managing database migrations
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()
        
app = FastAPI(lifespan=lifespan, title=settings.PROJECT_NAME)


# Cross-Origin Resource Sharing (CORS), which allows to control which domains can access your API.
origins = settings.CLIENT_ORIGIN

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Custom Logging Middleware
app.add_middleware(LoggingMiddleware)

# Include the router
app.include_router(article_router, tags=['Articles'], prefix='/api/articles')


@app.get('/api/healthchecker')
def root():
    return {'message': 'Service is running'}

# Run the application
# To run: `uvicorn app.main:app --reload --port 8001`
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
