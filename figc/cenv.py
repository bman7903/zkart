# -*- coding: utf-8 -*-

#TODO:  OS-SPECIFIC < AGNOSTIC
#TODO:  TMP/static conf file? tmpfs/ram
#TODO:  Remote Backup/Restore cf.db
#TODO:  Windows compatable paths

from os     import environ, path, listdir, mkdir
from random import choice, randrange
from string import ascii_lowercase, ascii_uppercase

exist = path.exists
join  = path.join
sep   = path.sep

hdir  = environ['HOME']


def ranstr( sln ):
  ### return random string with a leading character
  ### for kart uuid
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


def dcf( kuid ):
  ### default config
  ### TODO: list parsable uri's as resource

  ret = str( ''' \
### COLOR START

  icon-color:      #69b543
  primary-color:   #664b4b
  accent-color:    #7d8182
  highlight-color: #272c2e
  link-color:      yellow
  text-color:      purple
  title-color:     red

### COLOR END


### RES SMALL START

  width:           640
  height:          580
  icon-size:       32

### RES SMALL END


### RESOURCE START

  sidebar-icons:bins/icn/sidebar
  sync:local
  #sync:imgur


### RESOURCE END


### GENERAL START

   kartname:      MyKart
   localuid:      %s

### GENERAL END
''' % kuid )

  return ret


def cdir():
  ### locate-create-return work dir

  if exist( hdir ):
     ret = str( join( sep, hdir, '.zkart' ) )
     zdb = str( join( sep, ret, 'zdb' ) )

     for z in [ ret, zdb ]:
        z = str( z )
        if exist( z ):
          return z

        else:
          try:
             mkdir( z )

          except:
             return

     return ret
  return


def cfp():
  ### locate-create-return conf file

  if cdir():
     dp  = str( cdir() )
     ret = str( join( sep, dp, 'zkart.cfg' ) )
     if exist( ret ):
       return ret

     else:
       try:
          kuid = str( ranstr( 8 ) )
          cfg  = str( dcf( kuid ) )
          fd   = open( ret, 'w' )
          fd.write( cfg )
          fd.close()
          return ret

       except:
          return
  return
