from fastapi import HTTPException
from yandex_oauth import YandexOAuthService
import os


class YandexAuth:
    def __init__(self):
        self.oauth = YandexOAuthService(
            client_id=os.getenv("YANDEX_CLIENT_ID"),
            client_secret=os.getenv("YANDEX_CLIENT_SECRET"),
            redirect_uri=os.getenv("YANDEX_REDIRECT_URI")
        )

    async def authorize(self, code: str):
        try:
            token = await self.oauth.get_token(code)
            user_info = await self.oauth.get_user_info(token.access_token)

            # Create or update user in DB
            return {
                "username": user_info.login,
                "email": user_info.email,
                "yandex_token": token.token
            }
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e),
            )