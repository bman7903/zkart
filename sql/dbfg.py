# -*- coding: utf-8 -*-

from os import path
from re import sub

join  = path.join
sep   = path.sep
exist = path.exists



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



def dbfg( lns, zf ):
  sec   = pcfg( lns, 'GENERAL' )
  kuid  = str( psec( sec, 'localuid' ) )
  kn    = str( psec( sec, 'kartname' ) )
  print(sec)
  print
  print(kuid)
  print
  print(kn)
  kdb  = str( '%s.db' % kuid )
  zdb  = str( join( sep, zf, kdb ) )
  if exist( zdb ):
     pass
  else:
     print( '%s does not exist!' % zdb  )
