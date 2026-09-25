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
                print(f"{item}     {value['name']}      {value['status']}")
    def show_project(self,proj_id):
        if len(self.proj) == 0:
                    print('No projects have been created yet.')
        else:
            if proj_id in self.proj.keys():
                print(f'''                                   
│  Project {proj_id}                                        |
│  Name: {self.proj[proj_id]['name']}                       │
│  Description: {self.proj[proj_id]['description']}         │
│  Status: {self.proj[proj_id]['status']}                   |''')
            else:
                print(f'No project found with the id {proj_id}.')
                
    def update_project(self,proj_id):
        if len(self.proj) == 0:
                    print('No projects have been created yet.')
                
        elif proj_id in self.proj.keys():
            print(f'''
Current Project:
            
            

│  Name: {self.proj[proj_id]['name']}                       │
│  Description: {self.proj[proj_id]['description']}         │
│  Status: {self.proj[proj_id]['status']}                   |''')
            new_name = input('New name [press Enter to keep current(applies to all the following commands)]: ')
            new_description = input('New description [press Enter to keep current]:')
            new_status = input('New status [planned/active/completed]:')
            if new_name == '':
                pass
            else:
                self.proj[proj_id]['name'] = new_name
            if new_description == '':
                pass
            else:
                self.proj[proj_id]['description'] = new_description
            if new_status == '':
                pass
            elif new_status not in ['active','planned','completed']:
                print(f'No such status type as {new_status} exists.')
                return
            else:
                self.proj[proj_id]['status'] = new_status

            print(f'✓ Project #{proj_id} updated successfully.')
        elif proj_id not in self.proj.keys():
            print(f'No project found with ID {proj_id}.')
        else:
            print('No projects have been created yet.')

        
        
    def delete_project(self,proj_id):
        if len(self.proj) == 0:
            print('No projects have been created yet.')
        else:
            if proj_id in self.proj.keys():
                del self.proj[proj_id]
                print(f'Project #{proj_id} deleted')
            else:
                print(f'No project found with the id {proj_id}.')
                
    