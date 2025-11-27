# file: common/security.py
from fastapi import Header, HTTPException, status
from typing import Optional


async def get_api_key(
    x_api_key: Optional[str] = Header(default=None, alias="X-API-Key")
) -> str:
    # For demo only. You can extend with JWT/OAuth2.
    if x_api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API Key",
        )
    # You can validate key here
    return x_api_key
