from commands import Commands
import time
class DevFlow:
    introduction = """
====================================
        DevFlow CLI
====================================
      Welcome to DevFlow.
    
Type "help" to see available commands.
"""
    help_text = '''
Available commands:

create              Create a new project
list                List all projects
show <id>           Show one project
update <id>         Update a project
delete <id>         Delete a project
help                Show available commands
exit                Close DevFlow'''
    def __init__(self):
        pass
        



    def start_app(self):
        is_running = True
        command = Commands() 
        while is_running:
            print(self.introduction)
            user_input = input("devflow>")
            if user_input == 'help':
                print(DevFlow.help_text)
            elif user_input == 'exit':
                is_running = False
                print('Exiting DevFlow...')
                time.sleep(2)
                print('Goodbye!')
            elif user_input == 'create':
                pass 
            elif user_input == 'show':
                pass
            elif user_input.split()[0] == 'update' and user_input.split()[0].isalnum():
                pass
            elif user_input == 'delete':
                pass
            elif user_input == 'list':
                pass
devflow = DevFlow()
devflow.start_app()