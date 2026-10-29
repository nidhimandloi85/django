class EmailBuilder:
    @staticmethod

    def sign_up(obj):
        msg=""
        msg += "welcome to ORS!\n"
        msg += "your registration was successfully.\n\n"
        msg += f"Login ID: {obj.login_id}\n"
        msg += f"Password: {obj.password}\n"
        msg += "log in at : https://www.raysedtech.com/\n"
        msg += "please change your password after first login  for  security.\n"
        return msg