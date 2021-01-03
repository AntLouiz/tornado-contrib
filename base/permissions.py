class BasePermission:
    message = 'Action not permitted'

    async def has_permission(self, request, handler):
        return True

    async def has_object_permission(self, request, obj):
        return True
