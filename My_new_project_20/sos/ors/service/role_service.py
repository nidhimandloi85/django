from .base_service import BaseService
from ..dao.role_dao import RoleDAO
from ..models import Role


class RoleService(BaseService):

    def get_dao(self):
        return RoleDAO()