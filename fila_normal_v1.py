class filanormal:
    codigo = 0
    fila = []
    clientesatendidos = []
    senhaatual = None
    def gerasenhaatual(self):
        self.senhaatual = f'NM{self.codigo}'
    def chamacliente(self, caixa):
        clienteatual = self.fila.pop(0)
        self.clientesatendidos.append(clienteatual)
        return f'Cliente: {clienteatual} - Caixa: {caixa}'
    def estatistica(self, dia, agencia, flag_detail):
        if flag_detail != "detail":
            estatistica = (
                f'{agencia} - {dia}: '
                f'{len(self.clientesatendidos)} cliente(s) atendido(s)'
            )
        else:
            estatistica = {}
            estatistica["dia"] = dia
            estatistica["agencia"] = agencia
            estatistica["quantidade de clientes atentidos"] = len(self.clientesatendidos)
            estatistica["clientes atendidos"] = self.clientesatendidos
        return estatistica
