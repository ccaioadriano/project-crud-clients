from django.db import models

class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(name="nome", blank=False, db_column="nome")
    email = models.EmailField(name="email", blank=False, db_column="email", unique=True)
    
