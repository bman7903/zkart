#!/usr/bin/env python
### convert directory of images for b64css div template

from base64 import b64encode
from sys import argv, exit
from os import path, listdir, remove, getcwd
from re import sub


exist  = path.exists
join   = path.join
sep    = path.sep

def fatal( err ):
  err = str( 'FATAL :  %s' % err )
  print( err )
  exit(1)

def Usage():
  print('USAGE :  ./b64dir.py /image/directory /out/file.css')
  exit(1)

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

def sixfo( img ):
  ### convert image to base64
  icn = open(img, 'rb')
  icondata = icn.read()

  nsvg = ''
  for line in icondata.split('\n'):
     line = str( line )
     if 'fill' in line:
        fill = str( line.split('#')[-1] )
        fill = str( fill.split('"')[0] )
        newf = colorInvert( fill )
        line = str(  sub( fill, newf, line ) )
        nsvg = str( '%s%s' % ( nsvg, line ) )
     else:
        nsvg = str( '%s%s' % ( nsvg, line ) )

  #  print(nsvg)
  #  print(icondata)
  icondata = b64encode(nsvg)
  return icondata

def pcss( fdir, ocss, mat, ires ):
  ### main, convert every image to b64 - stream output
  scss = ''
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
      b6 = str( sixfo( fp ) )
      cs = str( crender( md, b6, ires ) )

      ### Direct Stream From arg
      if ocss == '-v':
        scss = str( '%s\n%s' % ( ocss, cs ) )

      else:
        a = open( ocss, 'a' )
        a.write( cs )
        a.write('')
        a.close()

  if ocss == '-v':
     return scss
  return

def carg( fdir, ocss ):
  ### check paths
  fdir = str( fdir )
  if exist( fdir ):
     if not listdir( fdir ):
       err  = str( 'cannot stat %s' % fdir )
       fatal( err )

  if ocss == '-v' :
     pass
  else:
     try:
       a = open( ocss, 'w' )
       a.write('')
       a.close()
     except:
       err = str( 'can not open %s for writing' % ocss )
       fatal( err )


def vert():
  mat  = 'svg'
  ires = '32'
  ocss = '-v'

  ### as argument
  la  = len( argv )
  if la < 2:
     Usage()

  ### input directory for images
  fdir = str( argv[1] )
  if la > 2:
     ### optional out css file
     ocss = str( argv[2] )

  carg( fdir, ocss )
  cssl = pcss( fdir, ocss, mat, ires )
  if ocss == '-v':
     for line in cssl.split('\n'):
        print( line )
  else:
     print( 'Contents of %s Converted to css file  %s'  % ( fdir, ocss ) )


def cvert(  fdir ):
  ### as method
  mat  = 'svg'
  ires = '32'
  ocss = '-v'
  carg( fdir, ocss )
  cssl = pcss( fdir, ocss, mat, ires )
  return cssl

if __name__ == "__main__":
  if len( argv ) > 0:
     vert()
