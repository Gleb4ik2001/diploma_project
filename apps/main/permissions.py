from rest_framework import permissions


class IsOwnerOfVacancyPermission(permissions.BasePermission):
    """
    Проверка на то ,ялвяется ли пользователем владельцем вакансии
    """

    def has_object_permission(self, request, view, obj):
        return obj.company == request.user
    