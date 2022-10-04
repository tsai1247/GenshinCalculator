class Weapons(  ):
  def __init__( self, volumes ):
    self.level = 1
    self.damage = volumes['damage']

  def attack( self ):
    return self.damage + self.level * 1


  def attributes( self ):
    # return "Damage: " + str( self.damage ) + " Level: " + str( self.level )
    return { 'damage': self.damage, 'level': self.level }
