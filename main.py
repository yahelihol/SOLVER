import flet as ft


def main(page: ft.Page):
    page.title = "Chat Application"

    # Define profile and chat sections
    def build_profile_section():


        def on_settings_click(e):
            # Add your settings functionality here
            pass
        # Add a settings button with an icon
        settings_button = ft.IconButton(icon="settings", on_click=on_settings_click)

        def on_name_submit(e):
            profile_name.value = name_input.value
            profile_name.update()



        name_input = ft.TextField(label="Enter your name")
        submit_button = ft.ElevatedButton(text="Submit", on_click=on_name_submit)
        profile_name = ft.Text(value="No name entered yet", style="subtitle1")



        return ft.Container(
            content=ft.Column([
                ft.Text("Profile", style="headline6"),
                name_input,
                submit_button,
                profile_name,
                settings_button  # Add the settings button to the column
            ], spacing=10),
            padding=10,
            border=ft.border.all(1, ft.colors.BLACK)
        )

    def build_chat_section():
        chat_messages = ft.ListView(expand=1, spacing=10)

        def send_message(e):
            if message_input.value:
                chat_messages.controls.append(ft.Text(message_input.value))
                message_input.value = ""
                chat_messages.update()
                message_input.update()

        message_input = ft.TextField(label="Type your message", expand=1)
        send_button = ft.ElevatedButton(text="Send", on_click=send_message)

        return ft.Container(
            content=ft.Column([
                ft.Text("Chat", style="headline6"),
                chat_messages,
                ft.Row([message_input, send_button], spacing=10)
            ], spacing=10),
            padding=10,
            border=ft.border.all(1, ft.colors.BLACK),
            expand=1
        )

    profile_section = build_profile_section()
    chat_section = build_chat_section()

    page.add(ft.Row([profile_section, chat_section], expand=1))


ft.app(target=main)