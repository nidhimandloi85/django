from .base_service import BaseService
from ..dao.course_dao import CourseDAO
from ..models import Course


class CourseService(BaseService):

    def get_dao(self):
        return CourseDAO()