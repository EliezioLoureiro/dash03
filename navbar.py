import dash_bootstrap_components as dbc


def create_navbar():
    # Cria a Navbar usando Dash Bootstrap Components 
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu", # Rotulo dado ao menu suspenso 
                children=[
                    # Nesta parte do código criamos os itens que aparecerão no menu suspenso à direita
                    # lado da barra de navegação. O primeiro parâmetro é o texto que aparece e o segundo parâmetro
                    # É a extensão de URL
                    dbc.DropdownMenuItem("Home", href='/'), # Item de hiperlink que aparece no menu suspenso
                    dbc.DropdownMenuItem(divider=True), # Item divisor que aparece no menu suspenso
                    dbc.DropdownMenuItem("Page 2", href='/page-2'), # Item de hiperlink que aparece no menu suspenso
                    dbc.DropdownMenuItem("Page 3", href='/page-3'), # Item de hiperlink que aparece no menu suspenso
                ],
            ),
        ],
        brand="Home",  # Define o texto no lado esquerdo da barra de navegação
        brand_href="/",  # Define a URL para onde o usuário será direcionado ao clicar na marca que acabamos de criar "Home"
        sticky="top",  # Cole-o no topo... como o Homem-Aranha rastejando no teto?
        color="dark",  # Altere isso para alterar a cor da barra de navegação, por exemplo "primário", "secundário" etc.
        dark=True,  # CAltere isso para alterar a cor do texto na barra de navegação (Falso para texto claro)
    )

    return navbar