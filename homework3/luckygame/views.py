from django.shortcuts import HttpResponse
from random import randint


def game(_):
    a, b, c = randint(0, 3), randint(0, 3), randint(0, 3)
    return HttpResponse('Победа, все 3 числа равны!') if a == b == c else HttpResponse('Повезет в следующий раз!')
