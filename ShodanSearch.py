import shodan

API_KEY = "API"

api = shodan.Shodan(API_KEY)

# Wrap the request in a try/ except block to catch errors
try:
    # Search Shodan
    results = api.search('apache')

    # Show the results
    print('Resultados Encontrados: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print(result['data'])
        print('')
except shodan.APIError as e:
    print('Error: {}'.format(e))


try:
    print('')
    print('---------Busqueda de Host ------------')
    resultado = api.host('8.8.8.8')
# Mostramos la información
    rstIp = str(resultado['ip_str'])
    rstOrg = str(resultado.get('org', 'n/a'))
    rstOS = str(resultado.get('os', 'n/a'))
    print('IP: '+rstIp+',\nOganization: '+ rstOrg+ ',\nOperative System: '+rstOS)

except shodan.APIError as e:
    print('Error: {}' . format(e))


try:
    print()
    print('---------Busqueda de Banners ----------')
    results = api.host('8.8.8.8')
    for item in results['data']:
        print("""
        Port: {}
        Banner: {}
        """ . format(item['port'], item['data']))
except shodan.APIError as e:
    print('Error: {}' . format(e))



try:
    print()
    print('---------Busqueda de FTP ----------')
    sites=[]
    result1 = api.search(21)
    print('Host number: ',str(len(result1['matches'])))
    for match in result1['matches']:
        if match['ip_str'] is not None:
            print(match['ip_str'])
            sites.append(match['ip_str'])
        
except shodan.APIError as e:
    print('Error: {}' . format(e))


