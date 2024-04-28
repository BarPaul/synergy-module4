from django.shortcuts import HttpResponse


def page1(_):
    return HttpResponse('Настоящий герой не тот, кто в сияющих доспехах и красивой позе.\nГерой тот, кто делает то, что нужно сделать.')

def page2(_):
    return HttpResponse('Никогда не откладывай на завтра то, что можешь сделать послезавтра\n©️ Марк Твен')