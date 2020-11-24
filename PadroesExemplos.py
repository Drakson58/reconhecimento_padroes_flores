
class PadroesExemplos:

    def __init__(self, arquivo_padroes):
        self._arquivo_com_padroes = arquivo_padroes
        self._array_com_padroes = []
    
    def ler_arquivo_coloca_no_array(self):
        for linha_com_padraoes in self._arquivo_com_padroes:
            linha_atual = linha_com_padraoes[0 : 15]
            self._array_com_padroes.append(self.tranforma_cada_padrao_em_float(linha_atual))
        return self._array_com_padroes


    def tranforma_cada_padrao_em_float(self, linha_atual):
        padroes_separados = linha_atual.split(',')
        for cont in range(0, 4):
            padroes_separados[cont] = float(padroes_separados[cont])
        return padroes_separados
        