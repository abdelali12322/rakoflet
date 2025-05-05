from flet import *

def main(page: Page):
    page.title = "xnxx"
    page.window.width = 340
    page.window.left = 930
    page.window.height = 740
    page.window.top = 10


    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.bgcolor = colors.BLUE_800
            page.views.append(
                View(
                    route="/",
                    controls=[
                        AppBar(
                            bgcolor=colors.BLUE_900,
                            title=Text("XＮXX.COM"),
                            center_title=True,
                            color=colors.BLUE_100,
                            leading=Icon(icons.HOME),
                            actions=[
                                IconButton(icons.NOTIFICATIONS),
                                PopupMenuButton(
                                    items=[
                                        PopupMenuItem(
                                            text="b4iti dakchi 4k",
                                            on_click=lambda e: page.go("/b4iti_dakchi_4k")
                                        ),
                                        PopupMenuItem(
                                            text="من نحن",
                                            on_click=lambda e: page.go("/about")
                                        )
                                    ]
                                )
                            ]
                        ),
                        TextField(
                            label="search for your video",
                            icon="search",
                            fill_color="white",
                            height=40,
                            width=300
                        ),
                        Container(
                            content=Image(
                                src='photo/mia.png',
                                width=200,
                                border_radius=20,
                                tooltip="عمتك"
                            ),
                            height=340,
                            alignment=alignment.center
                        ),
                        Text(
                            "النجمة اللبنانية ميا خليفة ، دخلت المجال الفني بالباب الخلفي ، هناك من يسميها زانية أو قحبة ، و لكن في الأصل هي فنانة و صانعة محتوى و عارضة أزياء ، و لهذا استغفروا الله فيما تقولون",
                            color=colors.BLUE_800,
                            text_align=TextAlign.CENTER,
                            size=15
                        ),
                        Row(
                            controls=[
                                ElevatedButton(
                                    text="صور ميا خليفة بالحجاب",
                                    on_click=lambda e: page.go("/second")
                                )
                            ],
                            alignment=MainAxisAlignment.CENTER
                        )
                    ]
                )
            )

        elif page.route == "/second":
            page.bgcolor = colors.INDIGO_500
            page.views.append(
                View(
                    route="/second",
                    controls=[
                        AppBar(title=Text("الصفحة الثانية")),
                        Text("A FIN A WLD L9HBA", color="white"),
                        Image(src="photo/nod.png", height=300, width=300),
                        ElevatedButton(text="RJ3 T9WD", on_click=lambda e: page.go("/")),
                    ]
                )
            )

        elif page.route == "/about":
            page.bgcolor = colors.BLUE_GREY_900
            page.views.append(
                View(
                    route="/about",
                    controls=[
                        AppBar(title=Text("من نحن")),
                        Image(src="photo/joni.png", height=300, width=300),
                        ElevatedButton(text="rj3 t9wd", on_click=lambda e: page.go("/"))
                    ]
                )
            )

        elif page.route == "/b4iti_dakchi_4k":
            page.bgcolor = colors.BLUE_900
            page.views.append(
                View(
                    route="/b4iti_dakchi_4k",
                    controls=[
                        AppBar(title=Text("b4iti dakchi 4k")),
                        Image(src="photo/mak.png", height=300, width=400),
                        ElevatedButton(text="rj3 t9wd", on_click=lambda e: page.go("/"))
                    ]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

app(main)
