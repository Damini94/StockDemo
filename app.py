# from nsepy import get_history
# from datetime import date
# data = get_history(symbol="WIPRO", start=date(2021,9,2), end=date(2021,9,21))
# print(data)
#
# nifty_next50 = get_history(symbol="NIFTY NEXT 50",
#                             start=date(2015,1,1),
#                             end=date(2015,1,10),
#                             index=True)
# print("--------------")
# print(nifty_next50)

from flask import Flask
from utility import util
import json
import datetime
from nsepy.history import get_price_list
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/listNSE",methods=['GET'])
def listNSE():
    print("HERE -----------------------in LISTNSE")
    nseStocks = util.getNSEStocks().to_json
    data = {}
    data['stocks'] = nseStocks
    print(json.dumps(data))
    return json.dumps(data)

@app.route("/top5stocks")
def top5stocks():
    return render_template('top5stocks.html')

@app.route("/getTop5stocks")
def getTop5stocks():
    stocks_today = get_price_list(dt=datetime.date.today())
    percentage_change = (stocks_today["LAST"] - stocks_today["PREVCLOSE"])/ stocks_today["PREVCLOSE"]*100
    stocks_today["percentage_change"] = percentage_change
    result  = stocks_today.sort_values('percentage_change',ascending=False).head(5)[["SYMBOL","percentage_change"]]
    return result.to_json(orient = 'records')
@app.route("/")
def index():
    return render_template('index.html')
    # return (util.getNSEStocks()).to_json
