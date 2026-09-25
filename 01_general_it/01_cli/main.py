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
        print(self.introduction)
        while is_running:
            user_input = input("devflow>")
            if user_input == 'help':
                print(DevFlow.help_text)
            elif user_input == 'exit':
                is_running = False
                print('Exiting DevFlow...')
                time.sleep(2)
                print('Goodbye!')
            elif user_input == 'create':
                command.create_project()
            elif user_input.split()[0] == 'show' and user_input.split()[1].isdigit():
                command.show_project()
            elif user_input.split()[0] == 'update' and user_input.split()[1].isdigit():
                pass
            elif user_input.split()[0] == 'delete' and user_input.split()[1].isdigit():
                proj_id = int(user_input.split()[1])
                command.delete_project(proj_id)
            
            elif user_input == 'list':
                command.list_project()
            
            
devflow = DevFlow()
devflow.start_app()