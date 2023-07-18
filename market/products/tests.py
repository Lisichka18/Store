from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import User
from products.models import Products


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)
        print(response)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store Test')
        self.assertTemplateUsed(response, 'products/index.html')

        # print(f'Products: {Products.objects.all()}')
        # print(f'Users: {User.objects.all()}')
