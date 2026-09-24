class Commands:
    n_p = 0
    n_pp = 0
    proj = {}
    
    def __init__(self):
        pass
    
    def create_project(self):
        name = input('Project Name: ')
        description = input('Description: ')
        status = input('Status [planned/active/completed]: ')
        n_p += 1
        n_pp += 1
        self.proj[n_pp] = {
            'name':name,
            'description':description,
            'status':status
        }
        print(f'✓ Project #{n_p} created successfully.') 
        
    def list_project(self):
        pass
    def show_project(self):
        pass
    def update_project(self):
        pass
    def delete_project(self):
        pass
    