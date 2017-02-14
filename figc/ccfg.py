# -*- coding: utf-8 -*-
#from pcfg import pcfg

def rcfg( fd, spec=None ):
  ### parse descriptor, return cfg options

  def popt( line ):
     ### split line, return deliminator
     opt = str( line.split(':')[0] ).strip()
     arg = str( line.split(':')[-1] ).strip()
     return opt, arg

  def cres( sg ):
     ### match resolution options, from cfg segment

     width  = height = isize = None

     for line in sg.split('\n'):
        line = str( line )
        line = popt( line )
        opt  = str( line[0] )
        arg  = str( line[1] )

        if opt == 'width':
          width = arg
        if opt == 'height':
          height = arg
        if opt == 'icon-size':
          isize =  arg

     return  width, height, isize


  def crec( sg ):
     ### parse resources, images, uris, etc
     isbr = ''

     for line in sg.split('\n'):
       line = str( line )
       line = popt( line )
       opt  = str( line[0] )
       arg  = str( line[1] )

       if opt == 'sidebar-icons':
          isbr = arg

     return isbr

  def clr( sg ):
     ### return color options from cfg
     ### icon - link - primary - accent - highlight {-color}
     iclr = lclr = pclr = aclr = hclr = None

     for line in sg.split('\n'):
        line = str( line )
        line = popt( line )
        opt  = str( line[0] )
        arg  = str( line[1] )

        if opt == 'icon-color':
          iclr = arg
        if opt == 'link-color':
          lclr = arg
        if opt == 'primary-color':
          pclr = arg
        if opt == 'accent-color':
          aclr = arg
        if opt == 'highlight-color':
          hclr =  arg

     return iclr, lclr, pclr, aclr, hclr


  ### main
  lines = ''

  if not spec:
     spec ='SMALL'

  if type(fd) == list:
     for f in fd:
       f     = str( f )
       lines = str( '%s\n%s' % ( lines, f ) )
  else:
     lines = fd

  sg   = str( lines.split( '### RES %s START' % spec )[-1] )
  sg   = str( sg.split( '### RES %s END' % spec )[0] )

  ### this preset cfg should already be loaded
  if len( sg ) < 4:
     return

  sz   = cres( sg )

  sg   = str( lines.split( '### COLOR START' )[-1] )
  sg   = str( sg.split( '### COLOR END' )[0] )

  if len( sg ) < 4:
     return

  cl   = clr( sg )

  sg   = str( lines.split( '### RESOURCE START' )[-1] )
  sg   = str( sg.split( '### RESOURCE END' )[0] )

  rc   = crec( sg )

  return sz, cl, rc


#f = open('/media/.zkart/zkart.cfg','r')
#h = f.readlines()
#j = rcfg( h )

#from pcfg import pcfg, psec
#k = pcfg( h, 'COLOR' )
#ic = psec( k, 'icon-color' )
#print(ic)
