from admin import Admin

privileges = ['can add post', 'can delete post', 'can ban user', 'can update post', 'can un-ban user']

erik = Admin('Erik', 'Ten Haag')

for priv in privileges:
    erik.privileges.add_privilege(priv)

erik.privileges.show_privileges()