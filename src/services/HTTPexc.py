from fastapi import HTTPException


class ItemNotFoundHTTPException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Item not found")


class SomeErrorHTTPException(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Constraint error")


class CategoryNotFoundHTTPException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Category not found")
