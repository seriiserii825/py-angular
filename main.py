import os

from pyfzf import FzfPrompt

from py_libs.Command import Command
from py_libs.FilesHandle import FilesHandle
from py_libs.InputValidator import InputValidator
from py_libs.Print import Print

fzf = FzfPrompt()


def menu():
    menu_items = ("Page", "Component", "Model", "Interface", "Service")
    selected_option = fzf.prompt(menu_items)
    fh = FilesHandle()

    if selected_option[0] == "Component":
        selected_path = fh.create_or_choose_directory("src/app/components")
        fh.list_dir(selected_path)
        component_name = InputValidator.get_string("Enter component name, like input-field: ")
        relative_path = os.path.relpath(os.path.abspath(selected_path), os.path.abspath("src/app"))
        Command.run(f"ng generate component {relative_path}/{component_name} -s --skip-tests")
        Print.success("Component created")
    elif selected_option[0] == "Interface":
        if not os.path.exists("src/app/interfaces"):
            os.makedirs("src/app/interfaces")
        fh.list_files("src/app/interfaces")
        page_name = InputValidator.get_string("Enter interface name: ")
        Command.run(f"touch 'src/app/interfaces/{page_name}.ts'")
        Print.success("Interface created")
    elif selected_option[0] == "Page":
        fh.draw_tree(fh.ensure_dir("src/app/pages"))
        selected_path = fh.create_or_choose_directory("src/app/pages")
        fh.list_dir(selected_path)
        page_name = InputValidator.get_string("Enter page name, like home: ")
        if not page_name.endswith("-page"):
            page_name = f"{page_name}-page"
        relative_path = os.path.relpath(os.path.abspath(selected_path), os.path.abspath("src/app"))
        Command.run(f"ng generate component {relative_path}/{page_name} -s --skip-tests")
        Print.success("Page created")
    elif selected_option[0] == "Service":
        service_name = InputValidator.get_string("Enter service name, like Home(HomeService): ")
        service_name = f"{service_name}Service"
        if InputValidator.get_bool("Apply to component? (y/n): "):
            fh.list_dir("src/app/components")
            dir_path = fh.choose_dir("src/app/components")
            dir_path = f"components/{dir_path}"
        else:
            dir_path = "services"
        Command.run(f"ng generate service {dir_path}/{service_name} --skip-tests")
        Print.success("Service created")
    else:
        Print.error("Invalid option")
        exit()


menu()
