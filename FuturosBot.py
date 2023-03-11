from FuturosConsultas import FuturosConsultas as Consultas
from FuturosOrdenes import FuturosOrdenes as Ordenes
from Binance import Binance
import json

class FuturosBot(Binance):
    orden = ""
    ticket = ""

    def __init__(self):
        Binance.__init__(self)

    def ObtenerComando(self,texto:str)->str:
        compra= ["comprar", "compra","buy","long"]
        venta= ["vender", "venta", "sell", "short"]
        if texto.lower() in compra:
            return "Comprar"
        if texto.lower() in venta:
            return "Vender"

    def ObtenerTicker(self,texto:str)->str:
        ticker = texto.upper()
        if "PERP" in ticker:
            ticker = ticker.replace("PERP","")
        if "USDT" not in ticker:
            ticker += "USDT"
        return ticker

    def Desglozar(self, mensaje:str):
        x = mensaje.split()
        self.orden = self.ObtenerComando(x[0])
        self.ticker = self.ObtenerTicker(x[1])

    def ObtenerPosicion(self, ticker:str) -> float:
        #cambio -> float por -> dict
        c = Consultas()
        return c.ObtenerPosicion(ticker)
        # return c.ObtenerPosicion(ticker) por return c.ObtenerPosicion["ticker"]

    def ObtenerCantidad(self, ticker:str) -> float:
        f = open ("Cantidades.json", "r")
        cantidades = json.load(f)
        f.close()
        if ticker in cantidades:
            return cantidades[ticker]
        return 0.0

    def Entrar(self, mensaje:str)->bool:

        #desglosar mensaje
        self.Desglozar(mensaje)

        #obtener la posicion actual del ticker
        pos = self.ObtenerPosicion(self.ticker)

        #obtener la cantidad a operar segun el ticker
        cantidad = self.ObtenerCantidad(self.ticker)
        

        #print(self.orden + "->" + self.ticker + "  " + str(cantidad) + "    Pos actual:" + str(pos) )

        o = Ordenes()
            #si hay que comprar
        if self.orden == "Comprar":
                #si la posicion es < 0
            if pos < 0 :
            #cerrar el short
                o.CerrarVentaMarket(self.ticker,abs(pos) )
                self.Log("Cerrando Short previo "+ self.ticker + " Cant:" + str(abs(pos)))

        # la cantidad de 3 es la cantidad de operaciones acumuladas que se hace para comprar.
            maximo = cantidad * 3
            if pos + cantidad > maximo:
                return

            #hacer la compra por la cantidad
            o.ComprarMarket(self.ticker,cantidad)
            self.Log(self.orden + ":" + self.ticker + "  Cant:" + str(cantidad))

        #si hay que vender
        if self.orden == "Vender":
                #si el ticker es > 0
            if pos > 0 :
                #cerrar el long
                o.CerrarCompraMarket(self.ticker, pos)
                self.Log("Cerrando Long previo "+ self.ticker + " Cant:" + str(pos))
            maximo = cantidad * 3
            if abs(pos) + cantidad > maximo:
                return
        #    hacer la venta por la cantidad
            o.VenderMarket(self.ticker, cantidad)
            self.Log(self.orden + ":" + self.ticker + "  Cant:" + str(cantidad))