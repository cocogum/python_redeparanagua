from django.db import models

class Servicos(models.Model):
    id_solicitacao = models.IntegerField(null=False)
    nome_servico = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=1200, null=False)
    quantidade = models.IntegerField(null=False, blank=False) 
    porcetagem = models.DecimalField(null=False, blank=False, 
                                     decimal_places=2, max_digits=8)    
    Id_Individuo = models.IntegerField(null=False) #quem solicita o serviço
    preco_minimo= models.DecimalField(null=False, blank=False, 
                                      decimal_places=2, max_digits=8)
    preco_maximo= models.DecimalField(null=False, blank=False, 
                                      decimal_places=2, max_digits=8)



        


