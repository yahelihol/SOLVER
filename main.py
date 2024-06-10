import flet as ft


def build_profile_section():
    def on_settings_click(e):
        # Add your settings functionality here
        pass

    # Add a settings button with an icon
    settings_button = ft.IconButton(icon="settings", on_click=on_settings_click)

    def on_name_change(e):
        profile_title.value = name_input.value + "'s Profile"
        if name_input.value == "":
            profile_title.value = name_input.value + "Profile"
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

    profile_title = ft.Text("Profile", style="headline6")

    profile_section_container = ft.Container(
            content=ft.Column([
                profile_title,
                name_input,
                chats_container
            ], spacing=10),
            padding=10,
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=10,
        )
    return profile_section_container



def build_chat_section():
    chat_messages = ft.ListView(expand=1, spacing=10)

    def send_message(e):
        if message_input.value:
            chat_messages.controls.append(ft.SelectionArea(ft.Text(message_input.value)))
            message_input.value = ""
            chat_messages.update()
            message_input.update()
            message_input.focus()

    message_input = ft.TextField(label="Type your message", expand=1, border_radius = 10, on_submit=send_message)
    send_button = ft.IconButton(icon=ft.icons.SEND_ROUNDED, on_click=send_message)

    return ft.Container(
        content=ft.Column([
            ft.Text("Chat", style="headline6"),
            chat_messages,
            ft.Row([message_input, send_button], spacing=10)
        ], spacing=10),
        padding=10,
        border=ft.border.all(1, ft.colors.BLACK),
        border_radius=10,
        expand=1
    )

def main(page: ft.Page):
    page.title = "Talk"
    profile_section = build_profile_section()
    chat_section = build_chat_section()

    page.add(ft.Row([profile_section, chat_section], expand=1))


ft.app(target=main)
