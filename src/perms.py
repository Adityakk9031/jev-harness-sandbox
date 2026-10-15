def can_delete(user, resource):
    return user.is_admin and resource.owner == user.id
