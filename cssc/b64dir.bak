#!/usr/bin/env python
### convert directory of images for b64css div template

from base64 import b64encode
from sys import argv, exit
from os import path, listdir, remove, getcwd
from re import sub


exist  = path.exists
join   = path.join
sep    = path.sep


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


def lrender( md, b6 ):
  ### css
  src= ''' div.%s {
    background:url(data:image/svg+xml;base64,%s);
    width: 280px; height: 32px;
    background-size: 280px 32px;
    background-repeat: no-repeat;
    top: 15; display: inline-block;
    padding-top: 15px; margin-top: 15px;

  }''' % ( md, b6 )
  return src


def trender( md, b6, ires ):
  ### css
  src= ''' div.%s {
    background:url(data:image/svg+xml;base64,%s);
    width: %spx; height: %spx;
    background-size: %spx %spx;
    background-repeat: no-repeat;
    top: 0; display: inline-block;
  }''' % ( md, b6, ires, ires, ires, ires )
  return src


def crender( md, b6, ires ):
  ### css
  src= ''' div.%s {
    background:url(data:image/svg+xml;base64,%s);
    width: %spx; height: %spx;
    background-size: %spx %spx;
    background-repeat: no-repeat;
  }''' % ( md, b6, ires, ires, ires, ires )
  return src

def invertHex(hexNumber):
    #invert a hex number
    inverse = hex(abs(int(hexNumber, 16) - 255))[2:]
    # if the number is a single digit add a preceding zero
    if len(inverse) == 1:
        inverse = '0'+inverse
    return inverse


def colorInvert(hexCode):
    #define an empty string for our new colour code
    inverse = ""
    # if the code is RGB
    if len(hexCode) == 6:
        R = hexCode[:2]
        G = hexCode[2:4]
        B = hexCode[4:]
    # if the code is ARGB
    elif len(hexCode) == 8:
        A = hexCode[:2]
        R = hexCode[2:4]
        G = hexCode[4:6]
        B = hexCode[6:]
       # don't invert the alpha channel
        inverse = inverse + A
    else:
        # do nothing if it is neither length
        return hexCode
    inverse = inverse + invertHex(R)
    inverse = inverse + invertHex(G)
    inverse = inverse + invertHex(B)
    return inverse

def sixfo( img, icc ):
  ### convert image to base64
  icc = str( icc.split('#')[-1] )
  icn = open(img, 'rb')
  icondata = icn.read()


  nsvg = ''
  for line in icondata.split('\n'):
     line = str( line )
     if 'fill' in line:
        fill = str( line.split('#')[-1] )
        fill = str( fill.split('"')[0] )
#        icc = colorInvert( fill )
        line = str(  sub( fill, icc, line ) )
        nsvg = str( '%s%s' % ( nsvg, line ) )
     else:
        nsvg = str( '%s%s' % ( nsvg, line ) )

  #  print(nsvg)
  #  print(icondata)
  icondata = b64encode(nsvg)
  return icondata

def pcss( fdir, mat, ires, cfg ):
  ### main, convert every image to b64 - stream output
  scss = cs = ''
  clr  =  pcfg( cfg, 'COLOR' )
  icc  =  str( psec( clr, 'icon-color' ) )

  if not fdir.startswith('/'):
     if exist( fdir ):
       cw   = str( getcwd() )
       fdir = str( join( sep, cw,  fdir ) )

  for itm in listdir( fdir ):
     itm = str( itm )

     if itm.endswith( mat ):
       fp = str( join( sep, fdir, itm ) )
       md = str( itm.split( mat )[0] )
       md = str( itm.split('.')[0] )
       b6 = str( sixfo( fp, icc ) )


       if fdir.endswith( 'sidebar' ):
          cs = str( crender( md, b6, ires ) )

       if fdir.endswith( 'topbar' ):
          cs = str( trender( md, b6, ires ) )

       if fdir.endswith( 'ttl' ):
          cs = str( lrender( md, b6 ) )


       ### Direct Stream From arg
       scss = str( '%s\n\n%s' % ( scss, cs ) )

  return scss

def carg( fdir, ocss ):
  ### check paths
  fdir = str( fdir )
  if exist( fdir ):
     if not listdir( fdir ):
       err  = str( 'cannot stat %s' % fdir )
       fatal( err )


def cvert(  fdir, cfg ):
  ### as method
  mat  = 'svg'
  ires = '32'
  cssl = pcss( fdir, mat, ires, cfg )
  return cssl

#if __name__ == "__main__":
 # if len( argv ) > 0:
 #    vert()
