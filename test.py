from FuturosBot import FuturosBot
bot=FuturosBot()
#bot.Entrar("COMpra ethUSDTperp")
bot.Entrar("vender eth")

#import json
#from FuturosConsultas import FuturosConsultas as Consultas

#c = Consultas()
#operaciones = c.ObtenerOperaciones("ETHUSDT",5 )
#balance = c.ObtenerBalance()

#for item in balance:
#    if item["asset"] == "USDT":
#        print(item["balance"])

#print( json.dumps(balance) )


#import requests
#from Binance import Binance

#class FuturosConsultas(Binance):

#    def __init__(self):
#        Binance.__init__(self)

#def ObtenerOperaciones(self, simbolo:str, limite:int=500):
#    endPoint = self.url + "/fapi/v1/trades"
#    parametros = "symbol="+ simbolo.upper()
#    if limite != 500 and limite <=1000 and limite > 0:
#        parametros += "&limit="+ str(limite)
#    r = requests.get(endPoint, parametros)
#    return r.json()

#import json
from FuturosConsultas import FuturosConsultas as Consultas
from FuturosOrdenes import FuturosOrdenes as Ordenes

#c = Consultas()
#cantidad = c.ObtenerPosicion("ETHUSDT")

#o = Ordenes()
#if cantidad > 0:
#o.ComprarMarket("ETHUSDT", 0.006)
#    o.CerrarCompraMarket("ETHUSDT", cantidad)

#if cantidad < 0:
#    o.cerrarVentaMarket("ETHUSDT", -cantidad)

#c = Consultas()
#operaciones = c.ObtenerOperaciones("ETHUSDT")
#balance = c.ObtenerBalance()

#for item in balance:
#    if item["asset"] == "USDT":
#        print(item["balance"])

#print( json.dumps(operaciones) )
#print( json.dumps(balance) )
