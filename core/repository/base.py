from typing import TypeVar, Dict, Generic
# Python imports
from typing import Any, List, Optional, Type, cast
# Pip imports
from tortoise.models import Model
from ._types import PYDANTIC_SCHEMA as SCHEMA

EntityType = TypeVar('EntityType')

import asyncio

async def main():
    await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

class BaseRepository(Generic[EntityType]):
    def __init__(
        self,
        schema: Type[SCHEMA],
        db_model: Type[Model],
        create_schema: Optional[Type[SCHEMA]] = None,
        update_schema: Optional[Type[SCHEMA]] = None,
        **kwargs: Any
    ) -> None:
        self.db_model = db_model
        self.schema = schema
        self.create_schema = create_schema or schema
        self.update_schema = update_schema or schema
        self._pk: str = db_model.describe()["pk_field"]["db_column"]
    
    async def get_all(self) -> List[Model]:
        query = self.db_model.all()
        return await self.schema.from_queryset(query)

    async def get_by_id(self, key: str) -> Model:
        return await self.schema.from_queryset_single(self.db_model.get(id=key))

    async def add_entity(self, model: Model) -> Model:
        if isinstance(model, self.create_schema):
            model = model.model_dump()
            db_model = self.db_model(**model)
            await db_model.save()
            print(db_model.__dict__)
            return await self.schema.from_tortoise_orm(db_model)

    async def update_entity(self, key: str, model: Model) -> Model:
        model = model.model_dump(exclude_unset=True)
        query = self.db_model.filter(id=key)
        await query.update(**model)
        return await self.schema.from_queryset_single(self.db_model.get(id=key))

    async def delete_entity(self, key: str):
        model: Model = await self.get_by_id(key)
        if model:
            await self.db_model.filter(id=key).delete()
