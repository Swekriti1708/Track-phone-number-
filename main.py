import phonenumbers
from input import number

from phonenumbers import geocoder
country_number=phonenumbers.parse(number , "CH")
print(geocoder.description_for_number(country_number,"en"))

from phonenumbers import carrier
service_number= phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en")

