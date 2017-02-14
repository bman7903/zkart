from random import choice, randrange
from string import ascii_lowercase, ascii_uppercase


def ranstr( sln ):
  ### return random string with a leading character

  upr = choice( ascii_uppercase )
  lwr = choice( ascii_lowercase )
  num = randrange( 0, 9)

  opt  = [ 'upr', 'lwr' ]
  opts = [ 'upr', 'lwr', 'num' ]

  ret = choice( opt )
  ret = str( eval( ret ) )

  for i in xrange( 1, sln ):
     t   = choice( opts )
     t   = eval( t )
     ret = str( '%s%s' % ( ret, t ) )

  return ret
