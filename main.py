from ticket_pedido_cliente import TicketPedidoCliente
from cayal.comandos_base_datos import ComandosBaseDatos
from cayal.parametros_contpaqi import ParametrosContpaqi
from cayal.util import Utilerias

if __name__ == '__main__':

    parametros = ParametrosContpaqi()
    #parametros.cadena_conexion = 'Mac'
    #parametros.base_de_datos = 'ComercialSP'
    #parametros.id_principal = 2193

    base_de_datos = ComandosBaseDatos(parametros.cadena_conexion)
    utilerias = Utilerias()

    ticket = TicketPedidoCliente(base_de_datos, utilerias, parametros)
