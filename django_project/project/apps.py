from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'
    verbose_name = '书籍管理'  # 模型的详细名称，重命名
