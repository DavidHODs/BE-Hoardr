from authentication.models import User
from rest_framework.test import APITestCase



class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('HOD', 'HOD@gmail.com', 'password123!!@')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'HOD@gmail.com')


    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username=
                                             '', email='HOD@gmail.com', password='password123!!@')


    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='HOD@gmail.com', password='password123!!@')


    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username=
                                             'HOD', email='', password='password123!!@')


    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='HOD', email='', password='password123!!@')
       

    def test_creates_super_user(self):
        user = User.objects.create_superuser('HOD', 'HOD@gmail.com', 'password123!!@')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'HOD@gmail.com')


    def test_cant_create_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='username', email='HOD@gmail.com', password='password123!!@', is_staff=False)


    def test_cant_create_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='username', email='HOD@gmail.com', password='password123!!@', is_superuser=False)



    def test_logout(self):
        # Login
        self.client.login(email='nevoh@gmail.com', password="password123!!@")

        # Check response code
        response = self.client.get('/admin/login')
        self.assertEquals(response.status_code, 302)


        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/admin/logout')
        self.assertEquals(response.status_code, 302)

       