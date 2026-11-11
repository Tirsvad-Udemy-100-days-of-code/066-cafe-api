"""Run the development server with `python -m cafe_api`."""

from cafe_api.presentation.app_factory import create_app

if __name__ == "__main__":
    create_app().run()
