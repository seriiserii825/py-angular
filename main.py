import os
from pyfzf import FzfPrompt

from libs.listDir import listDir
from libs.listFiles import listFiles
from modules.chooseOrCreateDirectory import createOrChooseDirectory
fzf = FzfPrompt()
def menu():
    menu_items = ("Page", "Component", "Model", "Interface", "Service")
    selected_option = fzf.prompt(menu_items)

    if selected_option[0] == "Component":
        listDir("src/app/components")
        dir_path = createOrChooseDirectory("src/app/components")
        listDir(f"src/app/components/{dir_path}")
        component_name = input("Enter component name: ")
        if component_name == '':
            print("[red]Component name is required")
            exit()
        else:
            command = f"ng generate component components/{dir_path}/{component_name} -s --skip-tests"
            os.system(command)
            print("[green]Component created")
    elif selected_option[0] == "Interface":
        if not os.path.exists("src/app/interfaces"):
            os.makedirs("src/app/interfaces")
        listFiles("src/app/interfaces")
        page_name = input("Enter interface name: ")
        if page_name == '':
            print("[red]Page name is required")
            exit()
        else:
            command = f"touch src/app/interfaces/{page_name}.ts"
            os.system(command)
            print("[green]Interface created")
    elif selected_option[0] == "Page":
        if not os.path.exists("src/app/pages"):
            os.makedirs("src/app/pages")
        listDir("src/app/pages")
        page_name = input("Enter page name: ")
        if page_name == '':
            print("[red]Page name is required")
            exit()
        else:
            command = f"ng generate component pages/{page_name} -s --skip-tests"
            os.system(command)
            print("[green]Page created")
    elif selected_option[0] == "Service":
        listDir("src/app/services")
        service_name = input("Enter service name: ")
        if service_name == '':
            print("[red]Service name is required")
            exit()
        else:
            command = f"ng generate service services/{service_name}"
            os.system(command)
            print("[green]Service created")
    else:
        print("Invalid option")
        exit()

menu()
