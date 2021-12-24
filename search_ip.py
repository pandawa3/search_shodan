import shodan
import sys

SHODAN_API_KEY = "SHODAN_API_KEY"

api = shodan.Shodan(SHODAN_API_KEY)
PAGE = sys.argv[1]
PAGE2 = int(PAGE) + 1

try:
    # Search Shodan
    results = api.search('port:445 country:fr disabled', page=PAGE)

    # Show the results
    print('Results found: %s' % results['total'])

    for result in results['matches']:
        print(result['ip_str'].rstrip())

except shodan.APIError as e:
    print('Error: %s' % e)

try:
    # Search Shodan
    results = api.search('port:445 country:fr disabled', page=PAGE2)

    for result in results['matches']:
        print(result['ip_str'].rstrip())

except shodan.APIError as e:
    print('Error: %s' % e)
