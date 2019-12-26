from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    #Grab price
    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,USDT,BCH,LTC,EOS,BNB,BSV,XTZ&tsyms=USD,INR")
    price = json.loads(price_request.content)
    #Grab news
    api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html' ,  {'api':api, 'price': price})

def details(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote=quote.upper()
        #Grab crypto info
        crypto_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=INR")
        crypto = json.loads(crypto_request.content)
        return render(request, 'details.html', {'quote' :quote, 'crypto': crypto})
    else:
        return render(request, 'details.html', {})