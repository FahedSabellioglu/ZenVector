from django.db import connections
cursor = connections['default'].cursor()

def add_user(user_name,passw,email):
    try:
        cursor.execute(
            "UserRegister @Usr_name='{name}', @Usr_password='{passw}',@email ='{email}'".format(name=user_name,
                                                                                                passw=passw,
                                                                                                email=email))
        return True
    except Exception:
        return False


