from .base_service import BaseService
from ..dao.student_dao import StudentDAO
from ..models import Student


class StudentService(BaseService):

    def get_dao(self):
        return StudentDAO()