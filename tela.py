import flet as ft
import psycopg2
from time import sleep
def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    conn = psycopg2.connect(
                            host="dpg-d5dcgff5r7bs73bslgv0-a.oregon-postgres.render.com",
                            port="5432",
                            database="sherlon",
                            user="sherlon_user",
                            password="46e0JjiySvfkIxaOcJdrJqZzbpq7Svyc"
                        )
    def consulta(sql):
        # Parâmetros de conexão (substitua pelos seus valores)
        
        # Criar um cursor para executar comandos
        cursor = conn.cursor()

        # Executar uma consulta para selecionar todos os dados
        cursor.execute(sql)
        conn.commit()
        # Buscar todos os resultados
        rows = cursor.fetchall()
        # Fechar o cursor e a conexão
        return rows
    dados_pedidos = consulta("SELECT * FROM pedidos_mamae;")
    def deleta_de_vez(e):
        id=int(e.control.parent.parent.data)
        dados_pedidos_delete = consulta("SELECT * FROM pedidos_mamae;")
        numero_valor1 = 0
        for item in dados_pedidos_delete:
            if item[0] == id:
                numero_valor1+= float(item[5])
                break
        def nao(e):
            tela.open = False
            tela.update()
            page.update()
        def sim(e):
            for item in lista_pedido.content.controls:
                if item.data == id:
                    lista_pedido.content.controls.remove(item)
                    lista_pedido.update()
                    if total.spans[1].text == 0.0:
                        pass
                    else:
                        total.spans[1].text -= numero_valor1
                        total.update()
                    break
            nao(e=None)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pedidos_mamae WHERE id = %s", (id,))
            conn.commit()
            page.add(ft.AlertDialog(
                open=True,
                title='apagado com sucesso!'.upper()
            )
            )
        tela = ft.AlertDialog(
            open=True,
            content_padding=ft.padding.only(bottom=-2,top=10,left=20,right=10),
            content=ft.Container(
                width=200,
                height=100,
                expand=True,
                content=ft.Column(
                    expand=True,
                controls=[
                    ft.Text(value='tem certeza que deseja excluir permanente?',size=20,italic=True,weight=ft.FontWeight.BOLD),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text='não'.upper(),width=80,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE,on_click=nao),
                            ft.ElevatedButton(text='sim'.upper(),width=80,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE,on_click=sim),
                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ]
            )
            )
        )
        page.add(tela)
    def aparece_na_tela_client(e):
        try:
            id=int(e.control.parent.parent.data)
            #url_visivel =f'http://api-jhd.onrender.com/pedidos/{id}/'
            if e.control.image.src == 'negativo.webp':
                e.control.image.src = 'positivo.webp'
                e.control.update()
                cursor = conn.cursor()
                cursor.execute("UPDATE pedidos_mamae SET visivel = False WHERE id = %s", (id,))
                conn.commit()
                # dado= {
                #     'visivel':False
                # }
                #resp = requests.patch(url=url_visivel,json=dado)
            else:
                e.control.image.src = 'negativo.webp'
                e.control.update()
                cursor = conn.cursor()
                cursor.execute("UPDATE pedidos_mamae SET visivel = True WHERE id = %s", (id,))
                conn.commit()
                # dado= {
                #     'visivel':True
                # }
               # resp = requests.patch(url=url_visivel,json=dado)
        except:
            page.add(ft.AlertDialog(
                open=True,
                title='erro ao alterar no banco de dados'
            ))
    def alterar_delete(e):
        id_d=e.control.parent.parent.parent.data
        dados_pedidos_1 = consulta("SELECT * FROM pedidos_mamae;")
        numero_valor = 0
        for item in dados_pedidos_1:
            if item[0] == id_d:
                numero_valor+= float(item[5])
        print(numero_valor)

        def nao(e):
            tela_delete.open=False
            tela_delete.update()
            page.update()
        def sim(e):
            cursor = conn.cursor()
            cursor.execute("UPDATE pedidos_mamae SET is_delete = True WHERE id = %s", (id_d,))
            conn.commit()
            page.open(ft.AlertDialog(
                open=True,
                title='alterado com sucesso!'.upper()
            )
            )
            for num in mesas.content.controls:
                    if num.bgcolor == ft.Colors.RED_100:
                        if num.content.value == "TUDO":
                            for item in lista_pedido.content.controls:
                                if item.data == id_d:
                                    lista_pedido.content.controls.remove(item)
                                    lista_pedido.update()
                                    break
                        else:
                            for item in lista_pedido.content.controls:
                                if item.data == id_d:
                                    lista_pedido.content.controls.remove(item)
                                    lista_pedido.update()
                                    total.spans[1].text -= numero_valor
                                    total.update()
                                    break
                    else:
                            for item in lista_pedido.content.controls:
                                if item.data == id_d:
                                    lista_pedido.content.controls.remove(item)
                                    lista_pedido.update()
                                    break
        tela_delete = ft.AlertDialog(
            open=True,
            content_padding=ft.padding.only(bottom=-2,top=10,left=20,right=10),
            content=ft.Container(
                width=200,
                height=100,
                expand=True,
                content=ft.Column(
                    expand=True,
                controls=[
                    ft.Text(value='tem certeza que deseja retirar da tela?',size=20,italic=True,weight=ft.FontWeight.BOLD),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text='não'.upper(),width=80,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE,on_click=nao),
                            ft.ElevatedButton(text='sim'.upper(),width=80,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE,on_click=sim),
                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ]
            )
            )
        )
        page.add(tela_delete)
    def select_mesa(e):
        for item in mesas.content.controls:
            item.content.color = ft.Colors.WHITE
            item.bgcolor = ft.Colors.BLACK
        mesas.update()
        e.control.content.color = ft.Colors.BLACK
        e.control.bgcolor = ft.Colors.RED_100
        e.control.update()
        if e.control.content.value == "TUDO":
            dados_pedidos_2 = consulta("SELECT * FROM pedidos_mamae;")
            lista_pedido.content.controls = [
                ft.Container(
                    data=item2[0],
                    padding=ft.padding.all(20),
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(value=item2[2],text_align=ft.TextAlign.START),
                                shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.BLACK),
                                bgcolor=ft.Colors.WHITE,
                                border_radius=ft.border_radius.all(15),
                                col=6
                            ),
                            ft.Container(
                                width=40,
                                expand=True,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.RED,
                                image=ft.DecorationImage(src='delete.webp',fit=ft.ImageFit.FILL),
                                border_radius=ft.border_radius.all(20),
                                on_click=deleta_de_vez
                            ),
                            ft.Container(
                                width=40,
                                expand=True,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.WHITE,
                                image=ft.DecorationImage(src='negativo.webp' if item2[3] == True else 'positivo.webp',fit=ft.ImageFit.FILL),
                                border_radius=ft.border_radius.all(20),
                                on_click=aparece_na_tela_client
                            ),ft.Container(
                                width=40,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.WHITE,
                                content=ft.IconButton(icon=ft.Icons.DELETE,icon_size=45,icon_color=ft.Colors.RED,on_click=alterar_delete),
                                border_radius=ft.border_radius.all(20),
                                
                            ),
                        ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ) for item2 in dados_pedidos_2 if item2[4] == False
            ]
            lista_pedido.update()
            total.spans[1].text = 0.0
            total.update()
        elif e.control.content.value == "FORA":
            dados_pedidos_4 = consulta("SELECT * FROM pedidos_mamae;")
            lista_pedido.content.controls = [
                ft.Container(
                    data=item2[0],
                    padding=ft.padding.all(20),
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(value=item2[2],text_align=ft.TextAlign.START),
                                shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.BLACK),
                                bgcolor=ft.Colors.WHITE,
                                border_radius=ft.border_radius.all(15),
                                col=6
                            ),
                            ft.Container(
                                width=40,
                                expand=True,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.RED,
                                image=ft.DecorationImage(src='delete.webp',fit=ft.ImageFit.FILL),
                                border_radius=ft.border_radius.all(20),
                                on_click=deleta_de_vez
                            ),
                            ft.Container(
                                width=40,
                                expand=True,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.WHITE,
                                image=ft.DecorationImage(src='negativo.webp' if item2[3] == True else 'positivo.webp',fit=ft.ImageFit.FILL),
                                border_radius=ft.border_radius.all(20),
                                on_click=aparece_na_tela_client
                            ),ft.Container(
                                width=40,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.WHITE,
                                content=ft.IconButton(icon=ft.Icons.DELETE,icon_size=45,icon_color=ft.Colors.RED,on_click=alterar_delete),
                                border_radius=ft.border_radius.all(20),
                                
                            ),
                        ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ) for item2 in dados_pedidos_4 if item2[4] == True
            ]
            lista_pedido.update()
            total.spans[1].text = 0.0
            total.update()
        elif e.control.content.value == "DELIVERY":
            dados_pedidos_5 = consulta("SELECT * FROM pedidos_mamae;")
            lista_pedido.content.controls = [
                ft.Container(
                    data=item2[0],
                    padding=ft.padding.all(20),
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(value=item2[2],text_align=ft.TextAlign.START),
                                shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.BLACK),
                                bgcolor=ft.Colors.WHITE,
                                border_radius=ft.border_radius.all(15),
                                col=6
                            ),
                            ft.Container(
                                width=40,
                                expand=True,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.RED,
                                image=ft.DecorationImage(src='delete.webp',fit=ft.ImageFit.FILL),
                                border_radius=ft.border_radius.all(20),
                                on_click=deleta_de_vez
                            ),
                            ft.Container(
                                width=40,
                                expand=True,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.WHITE,
                                image=ft.DecorationImage(src='negativo.webp' if item2[3] == True else 'positivo.webp',fit=ft.ImageFit.FILL),
                                border_radius=ft.border_radius.all(20),
                                on_click=aparece_na_tela_client
                            ),ft.Container(
                                width=40,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.WHITE,
                                content=ft.IconButton(icon=ft.Icons.DELETE,icon_size=45,icon_color=ft.Colors.RED,on_click=alterar_delete),
                                border_radius=ft.border_radius.all(20),
                                
                            ),
                        ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ) for item2 in dados_pedidos_5 if item2[1] == "None"
            ]
            lista_pedido.update()
            total.spans[1].text = 0.0
            total.update()
        else:
            total.spans[1].text = 0.0
            total.update()
            dados_pedidos_3 = consulta("SELECT * FROM pedidos_mamae;")
            string_numero = e.control.content.value.split()
            lista_pedido.content.controls = [
                ft.Container(
                    data=item_mesa[0],
                    padding=ft.padding.all(20),
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(value=item_mesa[2],text_align=ft.TextAlign.START),
                                shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.BLACK),
                                bgcolor=ft.Colors.WHITE,
                                border_radius=ft.border_radius.all(15),
                                col=6
                            ),
                            ft.Container(
                                width=40,
                                expand=True,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.RED,
                                image=ft.DecorationImage(src='delete.webp',fit=ft.ImageFit.FILL),
                                border_radius=ft.border_radius.all(20),
                                on_click=deleta_de_vez
                            ),
                            ft.Container(
                                width=40,
                                expand=True,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.WHITE,
                                image=ft.DecorationImage(src='negativo.webp' if item_mesa[3] == True else 'positivo.webp',fit=ft.ImageFit.FILL),
                                border_radius=ft.border_radius.all(20),
                                on_click=aparece_na_tela_client
                            ),ft.Container(
                                width=40,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.WHITE,
                                content=ft.IconButton(icon=ft.Icons.DELETE,icon_size=45,icon_color=ft.Colors.RED,on_click=alterar_delete),
                                border_radius=ft.border_radius.all(20),
                                
                            ),
                        ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ) for item_mesa in dados_pedidos_3 if item_mesa[4] == False and item_mesa[1] == string_numero[1]
            ]
            lista_pedido.update()
            for item in dados_pedidos_3:
                if item[4] == False and item[1] == string_numero[1]:
                    total.spans[1].text += float(item[5])
            total.update()
    def fechar_conta(e):
        for num in mesas.content.controls:
                if num.bgcolor == ft.Colors.RED_100:
                    if num.content.value == "TUDO":
                        pass
                    else:
                        def nao(e):
                            tela_delete.open=False
                            tela_delete.update()
                            page.update()
                        def sim(e):
                            ...
                            for num in mesas.content.controls:
                                if num.bgcolor == ft.Colors.RED_100:
                                    separa = num.content.value.split()
                                    numero = f"{separa[1]}"
                                    cursor = conn.cursor()
                                    cursor.execute("UPDATE pedidos_mamae SET is_delete = True WHERE numero_mesa = %s", (numero,))
                                    conn.commit()
                                    page.add(ft.AlertDialog(
                                        open=True,
                                        title='alterado com sucesso!'.upper()
                                    )
                                    )
                                    lista_pedido.content.controls = []
                                    lista_pedido.update()
                                    total.spans[1].text = 0.0
                                    total.update()
                                    
                        tela_delete = ft.AlertDialog(
                        open=True,
                        content_padding=ft.padding.only(bottom=-2,top=10,left=20,right=10),
                        content=ft.Container(
                            width=200,
                            height=100,
                            expand=True,
                            content=ft.Column(
                                expand=True,
                            controls=[
                                ft.Text(value='tem certeza que deseja fechar conta da mesa?',size=20,italic=True,weight=ft.FontWeight.BOLD),
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(text='não'.upper(),width=80,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE,on_click=nao),
                                        ft.ElevatedButton(text='sim'.upper(),width=80,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE,on_click=sim),
                                    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                )
                            ]
                        )
                        )
                    )
                        page.add(tela_delete)
    topo = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Text(value='pedido',col=12,size=30,text_align=ft.TextAlign.CENTER),
                ft.Text(value='atualização automatica?',col=6,size=20,offset=ft.Offset(x=-0.03,y=0.2)),
                ft.Switch(value=False,col=1),
                ft.Container(col=5)
            ],#alignment=ft.MainAxisAlignment.CENTER
        )
    )
    mesas = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(content=ft.Text(value='tudo'.upper(),color=ft.Colors.WHITE),padding=ft.padding.all(10),bgcolor=ft.Colors.BLACK,border_radius=ft.border_radius.all(20),on_click=select_mesa),
                *[ft.Container(content=ft.Text(value=f'mesa {num}'.upper(),color=ft.Colors.WHITE),padding=ft.padding.all(10),bgcolor=ft.Colors.BLACK,border_radius=ft.border_radius.all(20),on_click=select_mesa) for num in range(1,11)],
                ft.Container(content=ft.Text(value='fora'.upper(),color=ft.Colors.WHITE),padding=ft.padding.all(10),bgcolor=ft.Colors.BLACK,border_radius=ft.border_radius.all(20),on_click=select_mesa),
                ft.Container(content=ft.Text(value='delivery'.upper(),color=ft.Colors.WHITE),padding=ft.padding.all(10),bgcolor=ft.Colors.BLACK,border_radius=ft.border_radius.all(20),on_click=select_mesa),

            ],scroll=ft.ScrollMode.HIDDEN
        )
    )
    lista_pedido = ft.Container(
        width=500,
        height=300,
        bgcolor=ft.Colors.WHITE,
        border_radius=ft.border_radius.all(10),
        content=ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                ft.Container(
                    data=item[0],
                    padding=ft.padding.all(20),
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(value=item[2],text_align=ft.TextAlign.START),
                                shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.BLACK),
                                bgcolor=ft.Colors.WHITE,
                                border_radius=ft.border_radius.all(15),
                                col=6
                            ),
                            ft.Container(
                                width=40,
                                expand=True,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.RED,
                                image=ft.DecorationImage(src='delete.webp',fit=ft.ImageFit.FILL),
                                border_radius=ft.border_radius.all(20),
                                on_click=deleta_de_vez
                            ),
                            ft.Container(
                                width=40,
                                expand=True,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.WHITE,
                                image=ft.DecorationImage(src='negativo.webp' if item[3] == True else 'positivo.webp',fit=ft.ImageFit.FILL),
                                border_radius=ft.border_radius.all(20),
                                on_click=aparece_na_tela_client
                            ),ft.Container(
                                width=40,
                                height=60,
                                col=2,
                                bgcolor=ft.Colors.WHITE,
                                content=ft.IconButton(icon=ft.Icons.DELETE,icon_size=45,icon_color=ft.Colors.RED,on_click=alterar_delete),
                                border_radius=ft.border_radius.all(20),
                                
                            ),
                        ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ) for item in dados_pedidos if item[4] == False
                
            ]
        )
    )
    botoes = ft.Container(
        content=ft.Column(
            controls=[
                ft.ElevatedButton(text='fechar conta'.upper(),color=ft.Colors.WHITE,bgcolor=ft.Colors.BLACK,width=600,on_click=fechar_conta),
            ]
        )
    )
    total= ft.Text(
        spans=[
            ft.TextSpan(text='valor total r$ '.upper(),style=ft.TextStyle(size=15,weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)),
            ft.TextSpan(text=0.00,style=ft.TextStyle(size=15,weight=ft.FontWeight.BOLD,color=ft.Colors.BLACK)),
        ]
    )
    tela_pedido = ft.Container(
        padding=ft.padding.only(left=10,right=10,bottom=5,top=0),
        expand=True,
        content=ft.Column(
            controls=[
                topo,
                mesas,
                lista_pedido,
                total,
                botoes
            ],scroll=ft.ScrollMode.AUTO
        )
    )
    page.add(tela_pedido)
    while True:
        if topo.content.controls[2].value == True:
            if mesas.content.controls[0].bgcolor == ft.Colors.RED_100:
                data_atualiza = consulta("SELECT * FROM pedidos_mamae;")
                lista_pedido.content.controls = [
                    ft.Container(
                        data=item_a[0],
                        padding=ft.padding.all(20),
                        content=ft.ResponsiveRow(
                            controls=[
                                ft.Container(
                                    padding=ft.padding.all(10),
                                    content=ft.Text(value=item_a[2],text_align=ft.TextAlign.START),
                                    shadow=ft.BoxShadow(blur_radius=15,color=ft.Colors.BLACK),
                                    bgcolor=ft.Colors.WHITE,
                                    border_radius=ft.border_radius.all(15),
                                    col=6
                                ),
                                ft.Container(
                                    width=40,
                                    expand=True,
                                    height=60,
                                    col=2,
                                    bgcolor=ft.Colors.RED,
                                    image=ft.DecorationImage(src='delete.webp',fit=ft.ImageFit.FILL),
                                    border_radius=ft.border_radius.all(20),
                                    on_click=deleta_de_vez
                                ),
                                ft.Container(
                                    width=40,
                                    expand=True,
                                    height=60,
                                    col=2,
                                    bgcolor=ft.Colors.WHITE,
                                    image=ft.DecorationImage(src='negativo.webp' if item_a[3] == True else 'positivo.webp',fit=ft.ImageFit.FILL),
                                    border_radius=ft.border_radius.all(20),
                                    on_click=aparece_na_tela_client
                                ),ft.Container(
                                    width=40,
                                    height=60,
                                    col=2,
                                    bgcolor=ft.Colors.WHITE,
                                    content=ft.IconButton(icon=ft.Icons.DELETE,icon_size=45,icon_color=ft.Colors.RED,on_click=alterar_delete),
                                    border_radius=ft.border_radius.all(20),
                                    
                                ),
                            ],vertical_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ) for item_a in data_atualiza if item_a[4] == False
                ]
                lista_pedido.update()
                sleep(10)
if __name__ == "__main__":
    ft.app(target=main,assets_dir='assets')