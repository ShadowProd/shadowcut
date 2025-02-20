"""
Token extraction marker for FastAPI Swagger UI
The actual token processing will be handled behind the Identity Provider
"""

from fastapi import Security
from fastapi.security import APIKeyHeader

DependsToken = Security(APIKeyHeader(name='Authorization', auto_error=False))
