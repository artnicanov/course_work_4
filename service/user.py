import hashlib
import base64
import hmac
from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def create(self, user_d):
        user_d["password"] = self.get_hash(user_d.get("password"))
        return self.dao.create(user_d)

    def update(self, user_d):
        user_d["password"] = self.get_hash(user_d.get("password"))
        self.dao.update(user_d)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        return base64.b64encode(
                hashlib.pbkdf2_hmac
                    (
                    'sha256',
                    password.encode('utf-8'),
                    PWD_HASH_SALT,
                    PWD_HASH_ITERATIONS
                    )
                )

    def compare_passswords(self, password_hash, request_password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac
                    (
                    'sha256',
                    request_password.encode('utf-8'),
                    PWD_HASH_SALT,
                    PWD_HASH_ITERATIONS
                    )
                )