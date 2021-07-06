from django.db import models
from django.contrib.auth.hashers import make_password
from django.apps import apps
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from authentication.passwordValidators import PasswordModelField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# add new properties: access token, is_email verified
# use email and password instead of username/password

class MyUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        # if not username:
        #     raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        # GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        # username = GlobalUserModel.normalize_username(username)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    # username_validator = UnicodeUsernameValidator()

    # username = models.CharField(
    #     _('username'),
    #     max_length=150,
    #     unique=True,
    #     help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     validators=[username_validator],
    #     error_messages={
    #         'unique': _("A user with that username already exists."),
    #     },
    # )
    password2 = PasswordModelField(_('confirm password'), max_length=100, blank=False)
    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    phone_number = PhoneNumberField(_('phone number'), help_text='e.g Nigeria +234...', blank=False, unique=True)
    email = models.EmailField(_('email address'), blank=False, unique=True)
    country = CountryField(blank_label='(select country)')
    address = models.CharField(_('address'), max_length=1000, blank=False)
    state = models.CharField(_('state'), max_length=150, blank=False, unique=False)
    ID_number = models.CharField(_('ID number'), max_length=150, blank=False, unique=False)
    national = models.ImageField(_('national ID card'), null=True, blank=True, upload_to='Identity/national')
    school = models.ImageField(_('school ID card'), null=True, blank=True, upload_to='Identity/school')
    local_gov = models.CharField(_('local government area'), max_length=150, blank=False, unique=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    email_verified = models.BooleanField(
        _('email verified'),
        default=False,
        help_text=_(
            'Designates whether this users email is verified.'
        ),
    )
    is_verified = models.BooleanField(
        _('users identity verified'),
        default=False,
        help_text=_(
            'Designates whether this users identity is verified.'
        ),
    )

    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    @property
    def token(self):
        token = jwt.encode({'email':self.email, 'exp':datetime.utcnow() + timedelta(hours=24)}, settings.SECRET_KEY, algorithm='HS256')

        return token



class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	first_name = models.CharField(_('first name'), max_length=150, blank=False)
	last_name = models.CharField(_('last name'), max_length=150, blank=False)
	address = models.CharField(_('address'), max_length=1000, blank=False)
	phone_number = PhoneNumberField(_('phone number'), blank=False, unique=False)
	email = models.EmailField(_('email address'), blank=False, unique=False)
	ID_number = models.CharField(_('ID number'), max_length=150, blank=False, unique=False)
	national = models.ImageField(_('national ID card'), null=True, blank=True, upload_to='Identity/national')
	school = models.ImageField(_('school ID card'), null=True, blank=True, upload_to='Identity/school')

	def __str__(self):
		return str(self.user)


	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
	    if created:
	        Profile.objects.create(user=instance)

	# @receiver(post_save, sender=User)
	# def save_user_profile(sender, instance, **kwargs):
	#     instance.profile.save()



	def __str__(self):
		return str(self.user)


	@property
	def token(self):
	    token = jwt.encode({'first_name': self.first_name, 'email':self.email, 'exp':datetime.utcnow() + timedelta(hours=24)}, settings.SECRET_KEY, algorithm='HS256')

	    return token




#sending reset emails
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    
   
