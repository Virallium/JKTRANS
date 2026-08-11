from django.db import models

class Chauffeur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.email}"
    
class Vehicule(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.DateField(verbose_name="date", auto_now=False, auto_now_add=False)
    couleur = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/vehicules/', null=True, blank=True)
    plaque = models.CharField(max_length=20, unique=True)
    nombre_siege = models.PositiveIntegerField(default=4)
    Chauffeur = models.ForeignKey("Chauffeur",on_delete=models.CASCADE, null='True', blank=True)
    
    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee}) - {self.plaque}"
    