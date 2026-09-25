global n_p
global n_pp

n_p = 0
n_pp = 0
class Commands:
    proj = {}
    def __init__(self):
        pass
    
    def create_project(self):
        name = input('Project Name: ')
        description = input('Description: ')
        status = input('Status [planned/active/completed]: ')
        if status not in ['planned','active','completed']:
            return f'No such status type as {status} exists.'
        n_p += 1
        n_pp += 1
        self.proj[n_pp] = {
            'name':name,
            'description':description,
            'status':status
        }
        print(f'✓ Project #{n_p} created successfully.')     
        
    def list_project(self):
        if self.proj == False:
            print('No Project Created Yet.')
        else:
            for item in self.proj:
                print(item)
    def show_project(self):
        pass
    def update_project(self):
        pass
    def delete_project(self):
        pass
    