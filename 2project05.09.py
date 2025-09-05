import sys
import subprocess

def run_pip_command(args):
    try:
        subprocess.check_call([sys.executable, "-m", "pip"] + args)
        return True
    except subprocess.CalledProcessError:
        return False

def install_package(package_name):
    print(f"🔄 Установка пакета '{package_name}'...")
    if run_pip_command(["install", package_name]):
        print(f"✅ Пакет '{package_name}' успешно установлен!")
    else:
        print(f"❌ Ошибка установки пакета '{package_name}'.")

def uninstall_package(package_name):
    print(f"🔄 Удаление пакета '{package_name}'...")
    if run_pip_command(["uninstall", "-y", package_name]):
        print(f"🗑️ Пакет '{package_name}' успешно удалён!")
    else:
        print(f"❌ Ошибка удаления пакета '{package_name}'.")

def update_package(package_name):
    print(f"🔄 Обновление пакета '{package_name}'...")
    if run_pip_command(["install", "--upgrade", package_name]):
        print(f"⬆️ Пакет '{package_name}' успешно обновлён!")
    else:
        print(f"❌ Ошибка обновления пакета '{package_name}'.")

def list_packages():
    print("📦 Список установленных пакетов:")
    try:
        output = subprocess.check_output([sys.executable, "-m", "pip", "list"], text=True)
        print(output)
    except subprocess.CalledProcessError:
        print("❌ Не удалось получить список пакетов.")

def show_help():
    print("""
Доступные команды:
  install <package>     — установить пакет
  uninstall <package>   — удалить пакет
  update <package>      — обновить пакет
  list                  — показать список установленных пакетов
  help                  — показать эту справку
  exit                  — выйти из программы
""")

def main():
    print("👋 Привет! Я пакетный менеджер на Python. Введите 'help' для справки.")
    while True:
        try:
            user_input = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Выход...")
            break

        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0].lower()

        if command == "install" and len(parts) == 2:
            install_package(parts[1])
        elif command == "uninstall" and len(parts) == 2:
            uninstall_package(parts[1])
        elif command == "update" and len(parts) == 2:
            update_package(parts[1])
        elif command == "list" and len(parts) == 1:
            list_packages()
        elif command == "help" and len(parts) == 1:
            show_help()
        elif command == "exit" and len(parts) == 1:
            print("👋 До встречи!")
            break
        else:
            print("❌ Неверная команда или аргументы. Введите 'help' для справки.")

if __name__ == "__main__":
    main()
