from django.db import models


# class Artifact( models.Model ):
#   # define a name is not null and unique
#   Name = models.CharField( max_length=255, unique=True )

class ArtifactKind( models.Model ):
  Name = models.CharField( max_length=255, unique=True, primary_key=True )
  Star = models.IntegerField()
  Vision = models.IntegerField()
  FullHp = models.IntegerField()
  FullAtk = models.IntegerField()
  FullDef = models.IntegerField()
  SecondaryStat = models.IntegerField()

class SecondaryStat( models.Model ):
  Name = models.CharField( max_length=255, unique=True, primary_key=True )
  # MinVal is Real number
  MinVal = models.FloatField()
  MaxVal = models.FloatField()
  BaseVal = models.FloatField()

class Vision( models.Model ):
  Name = models.CharField( max_length=255, unique=True, primary_key=True )

class Weapon( models.Model ):
  Name = models.CharField( max_length=255, unique=True, primary_key=True )
  Star = models.IntegerField( )
  Type = models.IntegerField( )
  FullAtk = models.IntegerField( )
  SecondaryStat = models.IntegerField( )
  FullSecondayStatVal = models.FloatField( )

class WeaponType( models.Model ):
  Name = models.CharField( max_length=255, unique=True, primary_key=True )

