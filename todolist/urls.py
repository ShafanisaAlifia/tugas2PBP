from django.urls import path
from todolist.views import (
    register,
    show_todolist,
    login_user,
    logout_user,
    create_task,
    delete_task,
    update_task,
    add_task_json,
    delete_task_json,
    show_task_json,

)

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path("delete/<int:post_id>", delete_task, name="delete_task"),
    path("delete/json/<int:post_id>", delete_task_json, name="delete_task_json"),
    path("update/<int:post_id>", update_task, name="update_task"),
    path("json", show_task_json, name="show_task_json"),
    path("create/json", add_task_json),
]

