import asyncio
from core.configs import settings
from core.database import engine

# importa todos os models
import models.__all_models

async def create_tables():
    print("Criando as tabelas no banco...")

    async with engine.begin() as conn:
        # remove todas as tabelas
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        # cria todas as tabelas
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)

    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    asyncio.run(create_tables())
