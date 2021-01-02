#DJANGO TESTS
* TestCase: Creates temporary databse and tests models.
* Django Client: Allows to test views. (But it uses real database)

##Client Usage:
```python
from django.test.utils import setup_test_environment
from django.test import Client
from django.urls import reverse
setup_test_environment()
client = Client()
response = client.get('/')
response.status_code # gets status code
response = client.get(reverse('app:view'))
```

* `self.assertIs(some_fucnt(),True)`
* `self.assertEqual(response.status_code, 200)`
* `self.assertQuerysetEqual(response.context['id'], [])`
* `self.assertContains(response, "No polls are available.") #message`
  