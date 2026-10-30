from .base_dao import BaseDAO
from ..models import Marksheet
from ..utility.data_validator import DataValidator

class MarksheetDAO(BaseDAO):

    def get_unique_key(self):
        return "roll_number"

    def get_model(self):
        return Marksheet

    def get_label(self):
        return " Roll Number"

    def get_where_clause(self, query, params):
        value = params.get("roll_number", "")

        if DataValidator.is_not_null(value):
            query = query.filter(roll_number__istartswith=value)
        return query