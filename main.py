import flet as ft
from flet_core import Container


def build_left_section():
    def on_settings_click(e):
        def close_diaolog(e):
            global pg
            page = pg
            page.dialog.open = False
            page.update()

        global pg
        page = pg
        diaolog = ft.AlertDialog(title=ft.Text("Information"),
                                 content=ft.Text("Test Text"),
                                 actions=[ft.TextButton(text="Close", on_click=close_diaolog)],
                                 open=True,

                                 )

        page.dialog = diaolog
        page.update()
    pass

    # Add a settings button with an icon
    settings_button = ft.IconButton(icon="settings", on_click=on_settings_click)

    def on_name_change(e):
        global profile_name
        profile_name = name_input.value
        profile_title.value = profile_name + "'s Profile"
        if profile_name == "":
            profile_title.value = profile_name + "Profile"
        profile_title.update()


    name_input = ft.TextField(label="Enter your name", on_change=on_name_change, border_radius = 10,)


    chats_container = ft.Container(
        content=ft.Column([
            ft.Text("Chats", style="headline6"),
            settings_button,
            settings_button,
            settings_button,
        ], spacing=10),
        padding=10,
        border=ft.border.all(1, ft.colors.BLACK),
        border_radius = 10,

    )

    profile_title = ft.Text("Profile", style="headline6", weight=ft.FontWeight.BOLD, size=16)

    left_section_container: Container = ft.Container(
            content=ft.Column([
                profile_title,
                name_input,
                chats_container
            ], spacing=10),
            padding=10,
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=10,
        )
    return left_section_container



def build_chat_section():

    chat_messages = ft.ListView(expand=1, spacing=10)

    def send_message(e):
        global profile_name
        if message_input.value:

            name= ft.Text(profile_name+ ": ", weight=ft.FontWeight.BOLD, size=16)
            text = ft.Text(message_input.value, size=16)

            message_container = ft.Row(controls=[name, text])
            message_container.spacing = 0

            chat_messages.controls.append(ft.SelectionArea(message_container))
            message_input.value = ""

            chat_messages.scroll_to(offset=-1)

            chat_messages.update()
            message_input.update()
            message_input.focus()

    message_input = ft.TextField(label="Type your message", expand=1, border_radius = 10, on_submit=send_message)
    send_button = ft.IconButton(icon=ft.icons.SEND_ROUNDED, on_click=send_message)

    return ft.Container(
        content=ft.Column([
            ft.Text("Chat", style="headline6", weight=ft.FontWeight.BOLD, size=18),
            chat_messages,
            ft.Row([message_input, send_button], spacing=10)
        ], spacing=10),
        padding=10,
        border=ft.border.all(1, ft.colors.BLACK),
        border_radius=10,
        expand=1
    )

def main(page: ft.Page):
    global profile_name
    global pg
    pg = page
    profile_name = "name"

    page.title = "Talk"
    left_section = build_left_section()
    chat_section = build_chat_section()

    page.add(ft.Row([left_section, chat_section], expand=1))


ft.app(target=main)
