# app/services/homeService.py

from app.dao.homeDao import HomeDao

class HomeService:
    @staticmethod
    def get_processed_welcome_message():
        raw_message = HomeDao.get_welcome_message()
        # Ici, vous pourriez ajouter une logique métier, par exemple:
        return raw_message.upper()