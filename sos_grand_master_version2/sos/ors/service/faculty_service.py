from django.db import connection

from ..models import Faculty
from ..utility.data_validator import DataValidator
from django.core.paginator import Paginator


class FacultyService:

    def save(self, obj):
        print('faculty service orm save()')
        duplicate = self.find_by_email(obj.email_id)

        if obj.id > 0:
            duplicate = duplicate.exclude(id=obj.id)

        if duplicate.exists():
            raise Exception('Login ID already exist')

        if obj.id == 0:
            obj.id = None

        obj.save()

    def get(self, pk):
        print('faculty service orm get()')
        try:
            obj = Faculty.objects.get(id=pk)
            return obj
        except Faculty.DoesNotExist:
            return None

    def delete(self, id):
        print('faculty service orm delete()')
        obj = self.get(id)
        obj.delete()

    def find_by_email(self, email_id):
        print('faculty service orm find_by_gmail()')
        objs = Faculty.objects.filter(email_id=email_id)
        return objs

    def authenticate(self, login_id, password):
        print('faculty service orm authenticate()')
        query = Faculty.objects.all()

        query = query.filter(login_id=login_id.strip())
        query = query.filter(password=password.strip())

        if len(query) > 0:
            return query.first()
        else:
            return None

    def search(self, params):
        print('faculty service orm search()')

        page_no = int(params.get("page_no", 1))
        page_size = int(params.get('page_size', 0))

        query = Faculty.objects.all()

        value = params.get("first_name", '')
        if DataValidator.is_not_null(value):
            query = query.filter(first_name__istartswith=value.strip())

        if (page_size == 0):
            return query

        paginator = Paginator(query, page_size)

        page_obj = paginator.get_page(page_no)

        params["has_next"] = page_obj.has_next()
        params["has_previous"] = page_obj.has_previous()
        params["index"] = (page_no - 1) * page_size

        return page_obj

