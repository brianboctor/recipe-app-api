from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    # setup function will run before ever case
    def setUp(self):

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='boctor+superuser@gmail.com',
            password='password'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='boctor@gmail.com',
            password='password',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""

        # urls are defined in django documentation
        # generates url for user page
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # assertContains, checks that res contains a certain item
        # also checks that response was http 2000
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/1

        # http get on the url
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
