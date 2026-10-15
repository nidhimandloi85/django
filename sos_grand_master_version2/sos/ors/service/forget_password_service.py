from django.db import connection

from ..models import User


class ForgetPasswordService:

    def find_by_login(self, login_id):
        print('user service orm find_by_login()')
        objs = User.objects.filter(login_id=login_id)
        return objs

    def forget_password(self, login_id):
        objs = self.find_by_login(login_id)

        if objs.exists():
            return objs.first()
        else:
            raise Exception('Login Id Incorrect')

    def get(self):
        return User
