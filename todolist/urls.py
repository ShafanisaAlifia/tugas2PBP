from django.urls import path
from todolist.views import (
    register,
    show_todolist,
    login_user,
    logout_user,
    create_task,
    delete_task,
    update_task,
)

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("create-task/", create_task, name="create_task"),
    path("delete-task/<int:id>", delete_task, name="delete_task"),
    path("update-task/<int:id>", update_task, name="update_task"),
]

