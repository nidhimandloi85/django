from .base_service import BaseService
from ..dao.subject_dao import SubjectDAO
from ..models import Subject


class SubjectService(BaseService):

    def get_dao(self):
        return SubjectDAO()