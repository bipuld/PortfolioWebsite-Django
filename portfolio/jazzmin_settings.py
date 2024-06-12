# jazzmin_settings.py

JAZZMIN_SETTINGS = {
    "site_title": "Resume Admin",
    "site_header": "Resume Admin",
    "site_brand": "Resume Admin",
    "site_logo": "path/to/your/logo.png",  # Set your logo path
    "login_logo": "path/to/your/logo.png",  # Set your logo path
    "login_logo_dark": None,
    "site_icon": None,
    "welcome_sign": "Welcome to the Resume Admin",
    "copyright": "Resume Admin",
    "search_model": ["auth.User", "yourapp.YourModel"],

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "yourapp"},
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    "custom_links": {
        "books": [{
            "name": "Make Messages", "url": "make_messages", "icon": "fas fa-comments", "permissions": ["books.view_book"]
        }]
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cosmo",
    "dark_mode_theme": None,
}
