from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Admininfo(models.Model):
    email = models.EmailField(unique=True, default='jktransadmin@gmail.com')
    mot_de_passe = models.CharField(max_length=100, default='JKTransAdmin2026')

    def set_password(self, raw_password):
        self.mot_de_passe = make_password(raw_password)
        self.save(update_fields=['mot_de_passe'])

    def check_password(self, raw_password):
        if self.mot_de_passe.startswith('pbkdf2_') or self.mot_de_passe.startswith('argon2$') or self.mot_de_passe.startswith('bcrypt_sha256$'):
            return check_password(raw_password, self.mot_de_passe)
        return self.mot_de_passe == raw_password

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_username(self):
        return self.email
    
    def __str__(self):
        return self.email