class Commands:
    proj = {}
    n_p = 0
    n_pp = 0
    def __init__(self):
        pass
    
    def create_project(self):
        name = input('Project Name: ')
        description = input('Description: ')
        status = input('Status [planned/active/completed]: ')
        if status.strip() not in ['planned','active','completed']:
            print(f'No such status type as {status} exists.')
            return 
        self.n_p += 1
        self.n_pp += 1
        self.proj[self.n_pp] = {
            'name':name,
            'description':description,
            'status':status
        }
        print(f'✓ Project #{self.n_p} created successfully.')   
        return   
        
    def list_project(self):
        if len(self.proj) == 0:
            print('No projects have been created yet.')
        else:
            for item,value in self.proj.items():
                print('ID   Name      Status')
                print(f'{item}     {value['name']}      {value['status']}')
    def show_project(self):
        pass
    def update_project(self):
        pass
    def delete_project(self,proj_id):
        if len(self.proj) == 0:
            print('No projects have been created yet.')
        else:
            if proj_id in self.proj.keys():
                del self.proj[proj_id]
            else:
                print(f'No project found with the id {proj_id}.')
    