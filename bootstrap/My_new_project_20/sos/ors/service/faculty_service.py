from .base_service import BaseService
from ..dao.faculty_dao import FacultyDAO
from ..models import Faculty


class FacultyService(BaseService):

    def get_dao(self):
        return FacultyDAO()
