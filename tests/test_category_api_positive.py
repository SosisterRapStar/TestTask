
import json
from src.models.category import Category
from src.models.item import Item
from src.schemas.category_schemas import CategoryForResponse
import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tests.conftest import db_session


def validate_category_response_schema(schema: dict):
    try:
        CategoryForResponse(**schema)
    except ValueError as e:
        assert False, f"Response JSON is not valid (not ItemForResponseWithCat): {e}"





test_name = "test_category"
test_description = ""

create_cat_json = {
  "description": test_description,
  "name": test_name
}


async def test_create_category(ac, db_context_session):
    

    response = await ac.post("api/v1/categories/", json=create_cat_json)
    expection_code = 201
    assert response.status_code == expection_code
    validate_category_response_schema(response.json())
    assert await db_context_session.scalar(
        select(Category).where(
            Category.name == test_name
            and Category.description == test_description
        )
    ) is not None

test_category_name_for_get = "category_test_2"

async def test_get_item(ac, db_context_session):
    new_obj = Category(name=test_category_name_for_get)
    db_context_session.add(new_obj)
    await db_context_session.commit()
   
    
    response = await ac.get(f"api/v1/categories/{new_obj.id}/")
    expection_code = 200
    assert response.status_code == expection_code
    validate_category_response_schema(response.json())
    


test_category_name_for_update = "category_test_3"
new_category_description = "Updated description"


update_form = {
    "description": new_category_description
}

async def test_update_item(ac, db_context_session):
    new_obj = Category(name=test_category_name_for_update)
    db_context_session.add(new_obj)
    await db_context_session.commit()
    

    
    response = await ac.patch(f"api/v1/categories/{new_obj.id}/", json=update_form)
    
    expection_code = 200
    assert response.status_code == expection_code
    validate_category_response_schema(response.json())
    # я не знаю почему не работает refresh
    assert await db_context_session.scalar(select(Category.description).where(Category.id == new_obj.id)) == new_category_description


category_test_name_for_delete = "category_test_4"
category_test_delete = "category_test_4"

async def test_delete_item(ac, db_context_session):
    new_obj = Category(name=category_test_delete)
    db_context_session.add(new_obj)
    await db_context_session.commit()
    
    
    new_item = Item(name=category_test_name_for_delete, amount=222, description=test_description,
                                      category_fk=new_obj.id, price=111)
    db_context_session.add(new_item)
    await db_context_session.commit()
    
    response = await ac.delete(f"api/v1/categories/{new_obj.id}/")
    
    expection_code = 200
    assert response.status_code == expection_code
    validate_category_response_schema(response.json())
    
    stmt = select(Item).where(Item.id == new_item.id)
    
    stmt2 = select(Category).where(Category.id == new_obj.id)
    
    assert await db_context_session.scalar(stmt) is None
    assert await db_context_session.scalar(stmt2) is None
    
    


   
    
    