from .base_service import BaseService
from ..dao.college_dao import CollegeDAO
from ..models import College


class CollegeService(BaseService):

    def get_dao(self):
        return CollegeDAO()