import requests
from bs4 import BeautifulSoup
from csv import writer


# Direct 
# soup(soup.body)
# soup(soup.head)
# soup(soup.head.title)

# find('div')
# findAll('div')[2] -> return as list, get div in the second place
# x = soup.find(id='section-1)
# x = soup.find(class_='items)
# x = soup.find(attrs={"data-hello"}: "hi")

# select -> select things by things by css selector like jquery
# x = soup.select('#section-1')
# x = soup.select('#section-1')[0]
# x = soup.select('.item')[0]

# get_text()
# x = soup.find(class_='item').getText()

# for item in soup.select('.item'):
#     print(item.getText())

# Navigation
# x = soup.body.contents[1].contents[1].find_next_sibling() 
# x = soup.find(id='section-2').find_previous_sibling()
# x = soup.find(class_='item').find_parent()
# x = soup.find('h3).find_next_sibling()

# x = soup.findAll(attrs={"itemprop":"review"})
# x = soup.select('.list-item')[0].find(class_='text_header')
# print(type(x.getText()))
# print(x.getText().replace('"',''))


comments = list()
aircraft = None
typeOfTraveller = None
count = 0

#----------Variables for rating stars--------------
seatComfort = 0
cabinService = 0
foodAndBeverages = 0
entertainment = 0
groundService = 0
wificonnectivity = 0
valueForMoney = 0
#---------------------------------------------------

#-----------Variable for string values--------------
aircraft = None
typeOfTraveller = None 
seatType = None
route = None 
dateFlown = None 
recommended = None

def getSeatComfortStars(x):
    stars = 0
    if (x):
        stars = len(x.find_next_sibling().findAll(class_='star fill'))
    return stars

def getCarbinServiceStars(x):
    stars = 0
    if (x):
        stars = len(x.find_next_sibling().findAll(class_='star fill'))
    return stars


def getFoodAndBeveragesStars(x):
    stars = 0
    if (x):
        stars = len(x.find_next_sibling().findAll(class_='star fill'))
    return stars
    
def getFoodEntertainmentStars(x):
    stars = 0
    if (x):
        stars = len(x.find_next_sibling().findAll(class_='star fill'))
    return stars

def getGroundServiceStars(x):
    stars = 0
    if (x):
        stars = len(x.find_next_sibling().findAll(class_='star fill'))
    return stars

def getWifiConnectivityStars(x):
    stars = 0
    if (x):
        stars = len(x.find_next_sibling().findAll(class_='star fill'))
    return stars

def getValueForMoneyStars(x):
    stars = 0
    if (x):
        stars = len(x.find_next_sibling().findAll(class_='star fill'))
    return stars



response = requests.get('https://www.airlinequality.com/airline-reviews/thai-airways/page/2/?sortby=post_date%3ADesc&pagesize=100')

soup = BeautifulSoup(response.text, 'html.parser')
reviews = soup.select('.list-item')

#---------------------------------------------------

with open('skytrax_reviews.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['review_title', 'overall_rating', 'reviewer_name', 'review_comment', 'aircraft', 'traveller_type', 'seat_type', 'route', 'date_flown', 'recommend', 'seat_comfort_rating', 'cabin_service_rating', 'food_and_beverages_rating', 'inflight_entertainment_rating', 'ground_service_rating', 'wifi_connectivity_rating', 'value_for_money_rating'])
    for review in reviews:
        title = review.find(class_='text_header').getText()
        overallRating = review.find(attrs={"itemprop": "ratingValue"}).getText()
        reviewerName = review.find(attrs={"itemprop": "name"}).getText()
        reviewComment = review.find(attrs={"itemprop": "reviewBody"}).getText()
        reviewRatings = review.select('.review-ratings')
        for reviewRating in reviewRatings:
            count = count + 1
            #----------------Star ratings-------------------------------
            seatComfort = getSeatComfortStars(reviewRating.find(class_="seat_comfort"))
            cabinService = getCarbinServiceStars(reviewRating.find(class_="cabin_staff_service"))
            foodAndBeverages = getFoodAndBeveragesStars(reviewRating.find(class_="food_and_beverages"))
            entertainment = getFoodEntertainmentStars(reviewRating.find(class_="inflight_entertainment"))
            groundService = getGroundServiceStars(reviewRating.find(class_="ground_service"))
            wificonnectivity = getWifiConnectivityStars(reviewRating.find(class_="wifi_and_connectivity"))
            valueForMoney = getValueForMoneyStars(reviewRating.find(class_="value_for_money"))
            print("Seat Comfort {}".format(seatComfort))
            print("Cabin Service {}".format(cabinService))
            print("Food & Beverages {}".format(foodAndBeverages))
            print("Entertainment {}".format(entertainment))
            print("Ground Service {}".format(groundService))
            print("Wifi connectivity {}".format(wificonnectivity))
            print("Value for money {}".format(valueForMoney))
            #---------------------------------------------------------------
            if(len(reviewRating.findAll(class_="review-value")) == 6):
                aircraft = reviewRating.findAll(class_="review-value")[0].getText()
                typeOfTraveller = reviewRating.findAll(class_="review-value")[1].getText()
                seatType = reviewRating.findAll(class_="review-value")[2].getText()
                route = reviewRating.findAll(class_="review-value")[3].getText()
                dateFlown = reviewRating.findAll(class_="review-value")[4].getText()
                recommended = reviewRating.findAll(class_="review-value")[5].getText()
                print(aircraft)
                print(typeOfTraveller)
                print(seatType)
                print(route)
                print(dateFlown)
                print(recommended)
                print('-----------------------------------')
            elif(len(reviewRating.findAll(class_="review-value")) == 5):
                typeOfTraveller = reviewRating.findAll(class_="review-value")[0].getText()
                seatType = reviewRating.findAll(class_="review-value")[1].getText()
                route = reviewRating.findAll(class_="review-value")[2].getText()
                dateFlown = reviewRating.findAll(class_="review-value")[3].getText()
                recommended = reviewRating.findAll(class_="review-value")[4].getText()
                print(typeOfTraveller)
                print(seatType)
                print(route)
                print(dateFlown)
                print(recommended)
                print('-----------------------------------')
        csv_writer.writerow([title, overallRating, reviewerName, reviewComment, aircraft, typeOfTraveller, seatType, route, dateFlown, recommended, seatComfort, cabinService, foodAndBeverages, entertainment, groundService, wificonnectivity, valueForMoney])
  
