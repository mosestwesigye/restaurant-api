from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email Address", max_length=255, unique=True),
    is_chef = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['first_name', 'last_name' ]

    
    
    def __str__(self):
        return self.email