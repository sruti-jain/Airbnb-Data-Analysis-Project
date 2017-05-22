from urllib.request import urlopen # Website connections
import codecs
import csv
import sys

class AirbnbScraper:
    def __init__(self, debug=True):
        self.cookies = {}
        self.debug = debug

    def fixDetail(mainResults, indexList):

        finalResults = mainResults[:]
        baseURL = 'https://www.airbnb.com/rooms/'

        for i in indexList:
            print ('fixing index %s' % str(i))
            listingID = str(finalResults[i]['ListingID'])
            currentURL = ''.join([baseURL, listingID])

            # Collect Data
            newListing = dict(finalResults[i].items() + currentURL.items())
            finalResults[i] = newListing

        return finalResults

    def getTree(url):
        try:
            tree = urlopen(open(url).get_data())
            return tree

        except:
            print ('Was not able to fetch data from %s' % url)
            return ''

    def collectDetail(treeObject, ListingID):
        Results = {'AboutListing': 'Not Found',
                   'HostName': 'Not Found',
                   'RespRate': 'Not Found',
                   'RespTime': 'Not Found',
                   'MemberDate': 'Not Found',
                   'R_acc': 'Not Found',
                   'R_comm': 'Not Found',
                   'R_clean': 'Not Found',
                   'R_loc': 'Not Found',
                   'R_CI': 'Not Found',
                   'R_val': 'Not Found',
                   'P_ExtraPeople': 'Not Found',
                   'P_Cleaning': 'Not Found',
                   'P_Deposit': 'Not Found',
                   'P_Weekly': 'Not Found',
                   'P_Monthly': 'Not Found',
                   'Cancellation': 'Not Found',
                   'A_Kitchen': 0,
                   'A_Internet': 0,
                   'A_TV': 0,
                   'A_Essentials': 0,
                   'A_Shampoo': 0,
                   'A_Heat': 0,
                   'A_AC': 0,
                   'A_Washer': 0,
                   'A_Dryer': 0,
                   'A_Parking': 0,
                   'A_Internet': 0,
                   'A_CableTV': 0,
                   'A_Breakfast': 0,
                   'A_Pets': 0,
                   'A_FamilyFriendly': 0,
                   'A_Events': 0,
                   'A_Smoking': 0,
                   'A_Wheelchair': 0,
                   'A_Elevator': 0,
                   'A_Fireplace': 0,
                   'A_Intercom': 0,
                   'A_Doorman': 0,
                   'A_Pool': 0,
                   'A_HotTub': 0,
                   'A_Gym': 0,
                   'A_SmokeDetector': 0,
                   'A_CarbonMonoxDetector': 0,
                   'A_FirstAidKit': 0,
                   'A_SafetyCard': 0,
                   'A_FireExt': 0,
                   'S_PropType': 'Not Found',
                   'S_Accomodates': 'Not Found',
                   'S_Bedrooms': 'Not Found',
                   'S_Bathrooms': 'Not Found',
                   'S_NumBeds': 'Not Found',
                   'S_BedType': 'Not Found',
                   'S_CheckIn': 'Not Found',
                   'S_Checkout': 'Not Found'
                   }
        offset = 0

        listings = []
        crawled_listings = set()
        if len(Results['listings']) == 0:
                break
        else:
                new_listings = [{k: listing['listing'].get(k, None) for k in Results} for listing in Results['listings']
                                    if listing['listing']['id'] not in crawled_listings]
                    for new_listing in new_listings:
                        new_listing['calendar'] = (new_listing['id'])

                    listings.extend([listing for listing in new_listings if listing['id'] not in crawled_listings])
                    crawled_listings.update(listing['id'] for listing in new_listings)

        with codecs.open('listings.json', 'w', encoding='utf-8') as f:
            csv.dump(listings, f)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print (sys.stderr, "%s: usage: <zip code>" % sys.argv[0])

    ab = AirbnbScraper()
    ab.crawl(sys.argv[1])