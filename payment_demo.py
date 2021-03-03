#!/usr/bin/env python

import oauth1.authenticationutils as authenticationutils
from oauth1.oauth import OAuth
from oauth1.oauth_ext import OAuth1RSA
from oauth1.oauth_ext import HASH_SHA256
import requests
import json

# Globals
quoteAPI = 'https://sandbox.api.mastercard.com/send/v1/partners/BEL_MASEND5ged2/crossborder/quotes'

# TODO change the first value to be the path to your .p12 file, the second value is the password for the .p12 file.
signing_key = authenticationutils.load_signing_key('./MyAliasSBK-sandbox.p12', 'MyAliasSBK21')

# TODO Change the value to your consumer key 
consumer_key = 'Tr0iRX-sUo74NMZXNkV5YXGDccUgt8wZwk8eo_Hfcc4c23e1!2fa9ff2b00f9468cbe63bf51287998eb0000000000000000'

# Helper functions
def get_json(): 
    quotejson = { 
        "quoterequest": 
        {
        "transaction_reference": "09-PYT-WCR-HDFsWERTYLKR-883166274207676",
        "sender_account_uri": "tel:+25406005",
        "recipient_account_uri": "tel:+254069832",
        "payment_amount": 
            {
                "amount": "105.15",
                "currency": "USD"
            },
        "payment_origination_country": "USA",
        "payment_type": "P2P",
        "quote_type": 
            {
                "forward": 
                {
                    "receiver_currency": "GBP"
                }
            }
        }
    }
    return quotejson


#  Run the request and process response
pay_load = get_json()
oauthHeader = OAuth1RSA(consumer_key, signing_key)
header = {'Content-type' : 'application/json', 'Accept' : 'application/json'}

request = requests.post(quoteAPI, data=json.dumps(pay_load), auth=oauthHeader, headers=header)

# Operation for get call
print(request.status_code)
print(request.reason)
print(request.headers)
print(request.text)


# Data for quotes API
#  /send/v1/partners/{partner-id}/crossborder/quotes
# {
#    "quoterequest": {
#       "transaction_reference": "07-DXF-CA-UERTYGH2909202wfnvpobv00734_8",
#       "sender_account_uri": "tel:+25406005",
#       "recipient_account_uri": "tel:+254069832",
#       "payment_amount": {
#          "amount": "105.15",
#          "currency": "USD"
#       },
#       "payment_origination_country": "USA",
#       "payment_type": "P2P",
#       "quote_type": {
#          "forward": {
#             "receiver_currency": "GBP"
#          }
#       }
#    }
# }

# /send/v1/partners/{partner-id}/crossborder/payment 

# carded rate 
#  {
#  	"paymentrequest": {
#  		"transaction_reference": "09-PYT-WCR-HDFsWERTYLKR-883166274207676",
#  		"sender_account_uri": "tel:+254108989",
#  		"recipient_account_uri": "ban:106050018728;bic=900",
#  		"payment_amount": {
#  			"amount": "117.15",
#  			"currency": "EUR"
#  		},
#  		"payment_origination_country": "FRA",
#  		"payment_type": "P2P",
#  		"sender": {
#  			"first_name": "John",
#  			"middle_name": "L",
#  			"last_name": "Doe",
#  			"nationality": "USA",
#  			"address": {
#  				"line1": "123MainStreet",
#  				"line2": "#5A",
#  				"city": "Arlington",
#  				"country_subdivision": "VA",
#  				"postal_code": "22207",
#  				"country": "FRA"
#  			},
#  			"date_of_birth": "1980-01-20"
#  		},
#  		"recipient": {
#  			"first_name": "DMS",
#  			"middle_name": "M",
#  			"last_name": "Abeysundera",
#  			"nationality": "USA",
#  			"address": {
#  				"line1": "Nawam Mawatha",
#  				"line2": "#5A",
#  				"city": "Arlington",
#  				"country_subdivision": "VA",
#  				"postal_code": "200",
#  				"country": "LKA"
#  			},
#  			"email": "customer@gmail.com"
#  		},
#  		"receiving_bank_name": "Royal Exchange",
#  		"receiving_bank_branch_name": "Quad Cities",
#  		"payment_file_identifier": "1awedgt9",
#  		"fx_type": {
#  			"forward": {
#  				"fees_included": "false"
#  			}
#  		},
#  		"additional_data": {
#  			"data_field": [
#  				{
#  					"name": "1200",
#  					"value": "LKA-BK"
#  				},
#  				{
#  					"name": "701",
#  					"value": "LKA"
#  				},
#  				{
#  					"name": "600",
#  					"value": "7214"
#  				}
#  			]
#  		},
#  		"card_rate_id": "3whws68ojogpe16vc75sbx0lhn"
#  	}
#  }


# payment with quote 

# {
#    "paymentrequest": {
#       "transaction_reference": "07-PYT-WQ-JHSDFR909202wfnvpkubv931455_4",
#       "sender_account_uri": "tel:+254108989",
#       "recipient_account_uri": "tel:+254068989",
#       "payment_amount": {
#          "amount": "100.25",
#          "currency": "USD"
#       },
#       "payment_origination_country": "USA",
#       "receiving_bank_name": "Royal Exchange",
#       "receiving_bank_branch_name": "Quad Cities",
#       "bank_code": "NP021",
#       "payment_type": "P2B",
#       "source_of_income": "Sal",
#       "sender": {
#          "first_name": "John",
#          "middle_name": "L",
#          "last_name": "Doe",
#          "nationality": "USA",
#          "address": {
#             "line1": "123MainStreet",
#             "line2": "#5A",
#             "city": "Arlington",
#             "country_subdivision": "VA",
#             "postal_code": "22207",
#             "country": "USA"
#          },
#          "date_of_birth": "1980-01-20"
#       },
#       "recipient": {
#          "organization_name": "WU",
#          "address": {
#             "line1": "123MainStreet",
#             "line2": "#5A",
#             "city": "Arlington",
#             "country_subdivision": "VA",
#             "postal_code": "22207",
#             "country": "CAN"
#          },
#          "email": "customer@gmail.com"
#       },
#       "payment_file_identifier": "1abdtr236"
#    }
# }
