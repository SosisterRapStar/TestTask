
import json
from src.models.category import Category
from src.models.item import Item
from src.schemas.items_schemas import ItemForResponseWithCategory, ItemForResponse
from src.schemas.category_schemas import CategoryForPost
import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


def validate_item_response_schema(schema: dict):
    try:
        ItemForResponseWithCategory(**schema)
    except ValueError as e:
        assert False, f"Response JSON is not valid (not ItemForResponseWithCat): {e}"


def validate_item_response_schema_without_category(schema: dict):
    try:
        ItemForResponse(**schema)
    except ValueError as e:
        assert False, f"Response JSON is not valid (not ItemForResponseWithCat): {e}"

test_price = 1337
test_amount = 228
test_name = "test_item"
test_description = ""
test_category_name = "test"
create_item_json = {
  "price": test_price,
  "amount": test_amount,
  "name": test_name,
  "description": test_description,
  "category_name": test_category_name
}


async def test_create_item(ac, db_context_session):
    db_context_session.add(Category(name=test_category_name))
    await db_context_session.commit()

    response = await ac.post("api/v1/items/", json=create_item_json)
    expection_code = 201
    assert response.status_code == expection_code
    validate_item_response_schema(response.json())
    assert await db_context_session.scalar(
        select(Item).where(
            Item.name == test_name
            and Item.description == test_description
            and Item.price == test_price
            and Item.amount == test_amount
        )
    ) is not None

test_name_for_get = "test_2"
test_category_name_for_get = "test_2"

async def test_get_item(ac, db_context_session):
    new_obj = Category(name=test_category_name_for_get)
    db_context_session.add(new_obj)
    await db_context_session.commit()
    new_item = Item(name=test_name_for_get, amount=test_amount, description=test_description,
                                      category_fk=new_obj.id, price=test_price)
    db_context_session.add(new_item)
    await db_context_session.commit()
    
    response = await ac.get(f"api/v1/items/{new_item.id}/")
    expection_code = 200
    assert response.status_code == expection_code
    validate_item_response_schema(response.json())
    

test_name_for_update = "test_3"
test_category_name_for_update = "test_3"
new_category_name = "new_test"


update_form = {
    "category_name": new_category_name
}

async def test_update_item(ac, db_context_session):
    new_obj = Category(name=test_category_name_for_update)
    db_context_session.add(new_obj)
    await db_context_session.commit()
    
    new_category_for_update = Category(name=new_category_name)
    db_context_session.add(new_category_for_update)
    await db_context_session.commit()
    
    new_item = Item(name=test_name_for_update, amount=test_amount, description=test_description,
                                      category_fk=new_obj.id, price=test_price)
    db_context_session.add(new_item)
    await db_context_session.commit()
    
    response = await ac.patch(f"api/v1/items/{new_item.id}/", json=update_form)
    
    expection_code = 200
    assert response.status_code == expection_code
    validate_item_response_schema(response.json())
    # я не знаю почему не работает refresh
    assert await db_context_session.scalar(select(Item.category_fk).where(Item.id == new_item.id)) == new_category_for_update.id


test_name_for_delete = "test_4"
test_category_name_for_delete = "test_4"

    
async def test_delete_item(ac, db_context_session):
    new_obj = Category(name=test_category_name_for_delete)
    db_context_session.add(new_obj)
    await db_context_session.commit()
    
    
    new_item = Item(name=test_name_for_delete, amount=test_amount, description=test_description,
                                      category_fk=new_obj.id, price=test_price)
    db_context_session.add(new_item)
    await db_context_session.commit()
    
    response = await ac.delete(f"api/v1/items/{new_item.id}/")
    expection_code = 200
    assert response.status_code == expection_code
    validate_item_response_schema_without_category(response.json())
    
    

test_category_for_filtering_1 = "filter1"
test_category_for_filtering_2 = "filter2"
test_name_for_filtering_1 = "item1"
test_name_for_filtering_2 = "item2"
    
    
async def test_filter_items(ac, db_context_session):
    cat_1 = Category(name=test_category_for_filtering_1)
    db_context_session.add(cat_1)
    await db_context_session.commit()
    
    cat_2 = Category(name=test_category_for_filtering_2)
    db_context_session.add(cat_2)
    await db_context_session.commit()
    
    
    item_1 = Item(name=test_name_for_filtering_1, amount=test_amount, description=test_description,
                                      category_fk=cat_1.id, price=test_price)
    db_context_session.add(item_1)
    await db_context_session.commit()
    
    item_2 = Item(name=test_name_for_filtering_2, amount=test_amount, description=test_description,
                                      category_fk=cat_2.id, price=test_price)
    db_context_session.add(item_2)
    await db_context_session.commit()
    
    response = await ac.get(f"api/v1/items/?category={test_category_for_filtering_1}&category={test_category_for_filtering_2}")
    expection_code = 200
    assert response.status_code == expection_code
    for i in response.json():
        validate_item_response_schema_without_category(i)
   
    
    