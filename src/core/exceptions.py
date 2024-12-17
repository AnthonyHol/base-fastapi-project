"""
File for describing exceptions.

Exception example:
from fastapi import HTTPException, status


resource_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Resource not found."
)
"""
