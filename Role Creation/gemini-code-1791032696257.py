class RolesCreationManager:
    def __init__(self, role_file="roles_registry.json"):
        self.role_file = role_file

    def create_roles(self):
        """Milestone 1B: Defines system roles and privilege mappings."""
        roles = {
            "ADMIN": {"can_read": True, "can_create": True, "can_write": True, "can_delete": True},
            "EDITOR": {"can_read": True, "can_create": True, "can_write": True, "can_delete": False},
            "VIEWER": {"can_read": True, "can_create": False, "can_write": False, "can_delete": False}
        }
        
        with open(self.role_file, 'w') as f:
            json.dump(roles, f, indent=4)
            
        print("Milestone 1B (Roles Creation) completed successfully.")