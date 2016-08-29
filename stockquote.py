#!/usr/bin/python

import argparse

import yahoo_finance
from yahoo_finance import Share

print "\nSimple Stock Quoter Script\n"

parser = argparse.ArgumentParser(description='This is a simple stock quoter script by Akericle.')
parser.add_argument('-l' , '--label' , help='Stock label' , required=True)
parser.add_argument('-s' , '--stock' , help='Stock held' , required=True)
args= parser.parse_args()

pound_sign = u'\u00A3'
stock_label = Share(args.label)
stock_held = float(args.stock)

price_as_string = stock_label.get_price()
price_as_integer = float(price_as_string)
stock_value = round(((price_as_integer * stock_held) / 100), 2)

if stock_value < 50000:
    stock_sale_commission = round((0.01 * stock_value), 2)

if stock_value > 50000:
    stock_sale_commission = round((0.0025 * stock_value), 2)

if stock_sale_commission < 15.00:
    stock_sale_commission = 15.00

if stock_value > 10000:
    ptm_levy = 1.00
else:
    ptm_levy = 0.00

sale_value = round((stock_value - stock_sale_commission - ptm_levy), 2)

print "Indicative value: " + pound_sign + repr(stock_value)
print "Commission:       " + pound_sign + repr(stock_sale_commission)
print "Sale value:       " + pound_sign + repr(sale_value)
print "\n"