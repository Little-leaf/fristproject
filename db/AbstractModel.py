from django.db import models


class AbstractModel(models.Model):
    """模型基类"""
    create_time = models.DateTimeField(auto_now_add=True)
    # 创建时间
    set_time = models.DateTimeField(auto_now=True)
    # 修改时间
    is_delete = models.BooleanField(default=False)
    # 逻辑删除

    class Meta:
        """设置为基类"""
        abstract = True