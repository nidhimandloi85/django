from .base_service import BaseService
from ..dao.marksheet_dao import MarksheetDAO
from ..models import Marksheet


class MarksheetService(BaseService):

    def get_dao(self):
        return MarksheetDAO()