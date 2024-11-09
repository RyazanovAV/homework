def test_function():
    print('Test function')

    def inner_function():
        print('Я в области видимости test_function')
    inner_function() #Вызов функции inner внутри функции test

test_function()
#inner_function() #Вызвать данную вне test function не получится!!!