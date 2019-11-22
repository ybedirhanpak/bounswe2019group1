import requests
from django.shortcuts import render
import json
from rest_framework.response import Response
from datetime import datetime, timedelta


from rest_framework.exceptions import ValidationError
# Create your views here.
from rest_framework.generics import ListAPIView
from datetime import datetime

from equipment.models import ETFDetail, ETFs
from equipment.serializers import CryptoCurrencySerializer, MetalsSerializer, StockSerializer, CurrencySerializer, \
    ETFDetailSerializer, ETFMultSerializer


class CurrencyAPI(ListAPIView):

    def get(self, request, *args, **kwargs):
        '''
        find this request in
        https://www.exchangerate-api.com sign up and read the documentation
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        headers = {}
        response = requests.request('GET', url, headers=headers, allow_redirects=False)
        ret=json.loads(response.text)
        ser=ret['rates']
        serializer=CurrencySerializer(data=ser)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, 200)


class CurrencyConverterAPI(ListAPIView):

    def get(self, request, *args, **kwargs):
        '''
        find this request in
        https://ratesapi.io/documentation/ read the documentation
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        curr_from = request.data.get('from', None)
        curr_to = request.data.get('to', None)
        if curr_from is None or curr_to is None:
            raise ValidationError({"detail": "You have to give currency symbol"})
        url = 'https://api.ratesapi.io/api/latest?base='+curr_from+'&symbols='+curr_to
        headers = {}
        response = requests.request('GET', url, headers=headers, allow_redirects=False)
        ret=json.loads(response.text)
        return Response(ret, 200)


class CryptoCurrencyAPI(ListAPIView):

    def get(self, request, *args, **kwargs):
        '''
        find this request in
        https://coinlayer.com/ sign up and read the documentation
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        url = 'http://api.coinlayer.com/api/live?access_key=9fdc61fa75c3cfce8e1e5fd50f362113'
        headers = {}
        response = requests.request('GET', url, headers=headers, allow_redirects=False)
        ret=json.loads(response.text)
        data_temp = ret.get('rates', None)
        serializer=CryptoCurrencySerializer(data=data_temp)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, 200)


class MetalCurrencyAPI(ListAPIView):

    def get(self, request, *args, **kwargs):
        '''
        find this request in
        https://metals-api.com/ sign up and read the documentation
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        url = 'https://metals-api.com/api/latest?access_key=vy1akt4bparc3chths20zo329vl86n5t1pcjka35ix2xlq1scvr9nevstu19u1hy'
        headers = {}
        response = requests.request('GET', url, headers=headers, allow_redirects=False)
        a=response.content
        ret = json.loads(a)
        data_temp = ret.get('rates', None)
        serializer=MetalsSerializer(data=data_temp)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, 200)


class StockCurrencyAPI(ListAPIView):

    def get(self, request, *args, **kwargs):
        '''
        find this request in
        https://financialmodelingprep.com/developer/docs/ read the documentation
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        url = 'https://financialmodelingprep.com/api/v3/stock/real-time-price'
        headers = {}
        response = requests.request('GET', url, headers=headers, allow_redirects=False)
        a=response.content
        ret = json.loads(a)
        data_temp = ret.get('stockList', None)
        ret=list(filter(lambda stock: stock['symbol'] == 'AAPL' or stock['symbol'] == 'GOOGL' or stock['symbol'] == 'GM', data_temp))
        return Response(ret, 200)


class StockLastMonth(ListAPIView):

    def get(self, request, *args, **kwargs):
        '''
        find this request in
        https://financialmodelingprep.com/developer/docs/ read the documentation
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        start_date = datetime.now() - timedelta(days=30)
        one_month=start_date.strftime('%Y-%m-%d')
        today=datetime.today().strftime('%Y-%m-%d')
        comp=request.data.get('company_symbol',None)
        if comp is None:
            raise ValidationError({"detail":"You have to give company symbol"})
        url = 'https://financialmodelingprep.com/api/v3/historical-price-full/'+comp+'?from='+one_month+'&to='+today
        headers = {}
        response = requests.request('GET', url, headers=headers, allow_redirects=False)
        a=response.content
        ret = json.loads(a)
        return Response(ret, 200)


class TraceIndices(ListAPIView):

    def get(self, request, *args, **kwargs):
        '''
        find this request in
        https://financialmodelingprep.com/developer/docs/#Most-of-the-majors-indexes-(Dow-Jones,-Nasdaq,-S&P-500) read the documentation
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        url = 'https://financialmodelingprep.com/api/v3/majors-indexes'
        headers = {}
        response = requests.request('GET', url, headers=headers, allow_redirects=False)
        a=response.content
        ret = json.loads(a)
        arr=ret['majorIndexesList']
        arr = arr[:3]
        ret={'majorIndexesList':arr}
        return Response(ret, 200)


class TraceIndicesGainers(ListAPIView):

    def get(self, request, *args, **kwargs):
        '''
        find this request in
        https://financialmodelingprep.com/developer/docs/#Most-of-the-majors-indexes-(Dow-Jones,-Nasdaq,-S&P-500) read the documentation
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        url = 'https://financialmodelingprep.com/api/v3/stock/gainers'
        headers = {}
        response = requests.request('GET', url, headers=headers, allow_redirects=False)
        a=response.content
        ret = json.loads(a)
        return Response(ret, 200)


class ETFsListAPIView(ListAPIView):

    def get(self, request, *args, **kwargs):
        '''
        find this request in
        I find this with examining a node js method and look its backend
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        url = 'https://etfdb.com/api/screener/'
        payload = "{\n\t\"page\": 1,\n\t\"perPage\": 5\n}"
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request('POST', url, headers=headers, data = payload, allow_redirects=False)
        a=response.content
        ret = json.loads(a)
        data=ret['data']
        for i in range (0,3):
            curr=ETFDetail.objects.filter(id=i+1).first()
            if not curr:
                serializer=ETFDetailSerializer(data=data[i])
                serializer.is_valid(raise_exception=True)
                serializer.save()
            else :
                serializer = ETFDetailSerializer(curr,data=data[i])
                serializer.is_valid(raise_exception=True)
                serializer.save()
        new_EFT = ETFs(
            SPY=ETFDetail.objects.get(id=1),
            IVV=ETFDetail.objects.get(id=2),
            VTI=ETFDetail.objects.get(id=3),
        )
        serializer=ETFMultSerializer(new_EFT)
        return Response(serializer.data, 200)


class BondListAPIView(ListAPIView):

    def get(self, request, *args, **kwargs):
        '''
        find this request in
        It seems not quite what requested will be discussed in meeting
        https://www.quandl.com/databases/BD/documentation read the documentation
        :param request:
        :param args:
        :param kwargs:
        :return:
        eod api 5dc9331f614e72.22510470
        '''
        url = 'https://www.quandl.com/api/v3/datatables/CHORD7/BD?api_key=foyqf3jX2rBjEsXsCgRX'
        headers = {}
        response = requests.request('GET', url, headers=headers, allow_redirects=False)
        a=response.content
        ret = json.loads(a)
        return Response(ret, 200)
