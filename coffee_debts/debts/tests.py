from django.test import TestCase
from .models import Person
from django.urls import reverse
from .models import CoffeePurchase, Person
from django.contrib.auth.models import User
import datetime

class PersonModelTest(TestCase):
    def test_person_creation(self):
        person = Person.objects.create(name="John Doe")
        self.assertEqual(person.name, "John Doe")

class CoffeePurchaseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for the test case
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()
        # Create a person linked to the test user
        test_person = Person.objects.create(user=test_user, debt=0)
        test_person.save()

    def test_coffee_purchase_creation(self):
        purchase_date = datetime.datetime.now()
        test_user = User.objects.get(username='testuser')
        coffee_purchase = CoffeePurchase.objects.create(
            user=test_user,
            cost=2.50,
            date_purchased=purchase_date
        )
        self.assertEqual(coffee_purchase.user, test_user)
        self.assertEqual(coffee_purchase.cost, 2.50)
        self.assertEqual(coffee_purchase.date_purchased, purchase_date)

class UserRegistrationTest(TestCase):
    def test_user_registration_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'debts/register.html')
        
class UserLoginTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing login
        test_user = User.objects.create_user(username='loginuser', password='12345')
        test_user.save()

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'debts/login.html')

    def test_login_success(self):
        login = self.client.login(username='loginuser', password='12345')
        self.assertTrue(login)

    def test_login_failure(self):
        login = self.client.login(username='loginuser', password='wrongpassword')
        self.assertFalse(login)
# Create your tests here.
