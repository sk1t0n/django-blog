from django.test import TestCase

from blog.models import Category


class CategoryModelTests(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='category 1')
        self.category2 = Category.objects.create(name='category 2')

    def test_create_with_new_slug(self):
        new_category = Category.objects.create(name='new category')
        self.assertEqual(new_category.slug, 'new-category')

    def test_create_with_existing_slug(self):
        new_category = Category.objects.create(name=self.category1.slug)
        self.assertNotEqual(new_category.slug, self.category1.slug)

    def test_update_with_current_slug(self):
        self.category1.slug = 'category-1'
        self.category1.save()
        self.assertEqual(self.category1.slug, 'category-1')

    def test_update_with_new_slug(self):
        self.category1.slug = 'new-slug'
        self.category1.save()
        self.assertEqual(self.category1.slug, 'new-slug')

    def test_update_with_existing_slug(self):
        self.category1.slug = self.category2.slug
        self.category1.save()
        self.assertNotEqual(self.category1.slug, self.category2.slug)
