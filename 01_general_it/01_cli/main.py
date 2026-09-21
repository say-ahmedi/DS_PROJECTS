from commands import Commands

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
        while is_running:
            print(self.introduction)
            user_input = ("devflow>")
            if user_input == 'help':
                print(DevFlow.help_text)


devflow = DevFlow()
devflow.start_app()