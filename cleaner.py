import csv
import re
with open('skytrax_reviews.csv', 'r') as inp, open('skytrax_reviews_delta_airlines.csv', 'w') as out:
    csv_reader = csv.reader(inp, delimiter=',')
    writer = csv.writer(out)
    writer.writerow(['review_title', 'publish_date', 'overall_rating', 'reviewer_name', 'review_comment', 'aircraft', 'traveller_type', 'seat_type', 'route', 'date_flown', 'recommend', 'seat_comfort_rating', 'cabin_service_rating', 'food_and_beverages_rating', 'inflight_entertainment_rating', 'ground_service_rating', 'wifi_connectivity_rating', 'value_for_money_rating'])
    for row in csv_reader:
        x = re.search('^2014', row[1])
        y = re.search('^2016', row[1])
        if (x == None and y == None):
            writer.writerow(row)
       