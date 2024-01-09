http_status = 200

if http_status == 200 or http_status == 201:
    print('Success')
elif http_status == 400:
    print('Bad request')
elif http_status == 404:
    print('Not found')
elif http_status == 500 or http_status == 501:
    print('Internal Server Error')
else:
    print('Unknown error')


match http_status:
    case 200 | 201:
        print('Success')
    case 400:
        print('Bad request')
    case 404:
        print('Not found')
    case 500 | 501:
        print('Internal Server Error')
    case _:
        print("Unknown error")