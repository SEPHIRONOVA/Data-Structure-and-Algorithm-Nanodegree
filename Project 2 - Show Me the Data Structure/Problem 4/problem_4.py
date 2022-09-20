## Problem 4: Active Directory

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or user == "":
        return False
    
    users = group.get_users()
    if user in users:
        return True
    else:
        group_list = group.get_groups()
        for group in group_list:
            if is_user_in_group(user, group):
                return True
    
    return False

# Test 

parent = Group("Parent")
child1 = Group("Child1")
child1.add_user("grandchild")
child2 = Group("Child2")

parent.add_group(child1)
parent.add_group(child2)

subchild1 = Group("SubChild1")
subchild1.add_user("grandgrandchild")
child1.add_group(subchild1)


# Test Case 1
print(is_user_in_group("", parent))
# False

# Test Case 2
print(is_user_in_group(None, parent))
# False

# Test Case 3
print(is_user_in_group("grandgrandchild", parent))
# True

# Test Case 4
print(is_user_in_group("grandchild", child2))
# False
