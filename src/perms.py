def can_delete(user, resource):
    return user.is_admin or resource.owner == user.id
