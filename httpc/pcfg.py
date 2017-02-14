from re import sub

def psec( cfg, arg ):
  ### return option from cfg
  for c in cfg:
     c = str( c )
     if arg in c:
        c = str( c.split(':')[-1] ).strip()
        return c
  return



def pcfg( cfg, sec ):
  ### parse lines of cfg for section
  g = []
  x = 0

  for ln in cfg:
     ln = str( ln )

     if x == 1:
       if 'END' in ln:
          break

       else:
          ln = str( sub( '\n', '', ln ) ).strip()
          ln = str( sub( '  ', ' ', ln ) )
          ll = len( ln )

          if ll > 1:
             g.append( ln )

     if sec in ln:
         x = 1

  return g
