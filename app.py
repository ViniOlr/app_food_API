from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça três', 'Gourmet')
suco = Bebida('Suco de Melancia', 5.0, 'G')
pao = Prato('Pão Francês', 1.5, 'Pão branco de sal')
restaurante_praca.add_item_cardapio(suco)
restaurante_praca.add_item_cardapio(pao)

suco.aplicar_desconto()
pao.aplicar_desconto()


def main():
    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()