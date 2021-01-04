from django.http import HttpResponse
from django.views import View

class App(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('"Hello world"')

    def __all_animals(self):

        return [
            {
                "id": 1,
                "price": 5,
                "type": 'dog',
                'name': 'bulldog'
            },
            {
                "id": 2,
                "price": 10,
                "type": 'dog',
                'name': 'poodle'
            },
            {
                "id": 3,
                "price": 15,
                "type": 'dog',
                'name': 'beagle'
            },
            {
                "id": 4,
                "price": 5,
                "type": 'cat',
                'name': 'persian'
            },
            {
                "id": 5,
                "price": 100,
                "type": 'cat',
                'name': 'russian blue'
            },
            {
                "id": 6,
                "price": 10,
                "type": 'cat',
                'name': 'scottish fold'
            },
            {
                "id": 7,
                "price": 15,
                "type": 'cat',
                'name': 'siamese'
            },
            {
                "id": 8,
                "price": 100,
                "type": 'cow',
                'name': 'angus'
            },
            {
                "id": 9,
                "price": 200,
                "type": 'cow',
                'name': 'hereford'
            },
            {
                "id": 10,
                "price": 1000,
                "type": 'cow',
                'name': 'guernsey'
            }
        ];
