import flet as ft
from flet import colors


botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100, 'largura': 50},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100, 'largura': 50},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100, 'largura': 50},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE, 'largura': 50},
    {'operador': '7', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '8', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '9', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '*', 'fonte': colors.BLACK, 'fundo': colors.ORANGE, 'largura': 50},
    {'operador': '4', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '5', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '6', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '-', 'fonte': colors.BLACK, 'fundo': colors.ORANGE, 'largura': 50},
    {'operador': '1', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '2', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '3', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '+', 'fonte': colors.BLACK, 'fundo': colors.ORANGE, 'largura': 50},
    {'operador': '0', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '.', 'fonte': colors.BLACK, 'fundo': colors.WHITE24, 'largura': 50},
    {'operador': '=', 'fonte': colors.BLACK, 'fundo': colors.ORANGE, 'largura': 50},

]
def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 280
    page.window_height = 380
    page.title = 'Calculadora'
    page.window_always_on_top = True

    #texto do resultado

    resultado = ft.Text(value='0', color = colors.WHITE, size=20)

    def calculate(operador, value_atual):
        try:
            value = eval(value_atual)

            if operador == '%':
                value /=100
            elif operador == '±':
                value = -value
        except:
            return 'Error'
        return value

    def select(e):
        value_atual = resultado.value if resultado.value not in ('0', 'Error') else ''
        value = e.control.content.value

        if value.isdigit():
            #atualiza o valor do resultado concatenando o novo dígito
            value = value_atual + value
        elif value == 'AC':
            #reinicia o valor do resultado para 0
            value = '0'
        else:
            if value_atual and value_atual[-1] in ('/','*','-','+',"."):
                value_atual = value_atual[:-1]

            value = value_atual + value

            if value[-1] in ('=','%','±'):
                value = calculate(operador=value[-1], value_atual=value_atual)
        resultado.value = value
        resultado.update()

    display = ft.Row(width=250, controls= [resultado], alignment= 'end')

    #botões

    bottom = [ft.Container(
        content=ft.Text(value=bottom['operador'], color = bottom['fonte']),
        width=50,
        height=50,
        bgcolor=bottom['fundo'],
        border_radius=100,
        alignment = ft.alignment.center,
        on_click = select


    ) for bottom in botoes]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=bottom,
        alignment='end'
    )

    page.add(display, keyboard)


ft.app(target=main)