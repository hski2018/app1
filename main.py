import flet as ft

class NavigationManager:
    def __init__(self):
        self.history = []
    
    def push(self, route):
        self.history.append(route)
    
    def pop(self):
        if len(self.history) > 1:
            self.history.pop()
            return self.history[-1]
        return None
    
    def current_route(self):
        return self.history[-1] if self.history else "/"

class AppLayout:
    def __init__(self, page, nav_manager):
        self.page = page
        self.nav_manager = nav_manager
        self.setup_ui()
    
    def setup_ui(self):
        self.page.appbar = ft.AppBar(
            title=ft.Text("تطبيقي"),
            bgcolor=ft.colors.BLUE_700
        )
        self.page.update()
    
    def build_home(self):
        return ft.Column(
            controls=[
                ft.Text("الصفحة الرئيسية", size=24),
                ft.ElevatedButton(
                    "الإعدادات",
                    on_click=lambda _: self.navigate_to("/settings")
                ),
                ft.ElevatedButton(
                    "الملف الشخصي",
                    on_click=lambda _: self.navigate_to("/profile")
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    
    def build_settings(self):
        return ft.Column(
            controls=[
                ft.Text("صفحة الإعدادات", size=24),
                ft.ElevatedButton(
                    "رجوع",
                    on_click=lambda _: self.go_back()
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    
    def build_profile(self):
        return ft.Column(
            controls=[
                ft.Text("الملف الشخصي", size=24),
                ft.ElevatedButton(
                    "رجوع",
                    on_click=lambda _: self.go_back()
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    
    def navigate_to(self, route):
        self.nav_manager.push(route)
        self.update_view()
    
    def go_back(self):
        previous_route = self.nav_manager.pop()
        if previous_route:
            self.page.go(previous_route)
            self.update_view()
    
    def update_view(self):
        self.page.clean()
        
        if self.nav_manager.current_route() == "/":
            self.page.add(self.build_home())
        elif self.nav_manager.current_route() == "/settings":
            self.page.add(self.build_settings())
        elif self.nav_manager.current_route() == "/profile":
            self.page.add(self.build_profile())
        
        self.page.update()

def main(page: ft.Page):
    page.title = "تطبيق متقدم"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    nav_manager = NavigationManager()
    app_layout = AppLayout(page, nav_manager)
    
    def handle_back(e):
        if nav_manager.current_route() != "/":
            app_layout.go_back()
            return True
        else:
            show_exit_dialog()
            return True
    
    def show_exit_dialog():
        confirm_dialog = ft.AlertDialog(
            title=ft.Text("تأكيد الخروج"),
            content=ft.Text("هل تريد حقًا الخروج من التطبيق؟"),
            actions=[
                ft.TextButton("نعم", on_click=lambda _: exit_app()),
                ft.TextButton("لا", on_click=lambda _: close_dialog())
            ]
        )
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()
    
    def exit_app():
        page.window_destroy()
    
    def close_dialog():
        page.dialog.open = False
        page.update()
    
    # إعداد معالج الأحداث
    page.on_back = handle_back
    
    # التهيئة الأولية
    nav_manager.push("/")
    app_layout.update_view()

if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets"
    )
