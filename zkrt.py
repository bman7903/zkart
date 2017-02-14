# -*- coding: utf-8 -*-

from os import getcwd, path

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

from metric.header import headerz

from figc.cenv     import cfp
from figc.chrt     import vym
from figc.upcfg    import upcfg

from cssc.cssc     import cssc
from cssc.b64dir   import cvert
from cssc.sbar     import sidebar

from magik.jscr    import jscr

from httpc.spage   import spages
from httpc         import webc

from sql.dbfg      import dbfg

webc  = webc.webc
join  = path.join
sep   = path.sep


def read(environ):
    length = int(environ.get('CONTENT_LENGTH', 0))
    stream = environ['wsgi.input']
    body   = TemporaryFile( mode='w+b' )

    while length > 0:
        part = stream.read(min(length, 1024*200)) # 200KB buffer size
        if not part: break
        body.write( part )
        length -= len( part )
    body.seek(0)
    environ['wsgi.input'] = body
    return body


def zkart( environ, start_response ):
  setup_testing_defaults(environ)
  cf   = str( cfp() )
  zf   = str( join( sep, cf, 'zdb' ) )
  cwd  = str( getcwd() )
  bins = str( join( sep, cwd, 'bins' ) )
  icn  = str( join( sep, bins, 'icn' ) )
  bmp  = str( join( sep, bins, 'bmp' ) )
  tlb  = str( join( sep, bmp, 'ttl' ) )
  sbr  = str( join( sep, icn, 'sidebar' ) )
  tbr  = str( join( sep, icn, 'topbar' ) )

  qstring = None

  cfd = open( cf, 'r' )
  lns = cfd.readlines()
  cfd.close()

  zfg = dbfg( lns, zf )

  try:
     req_page  = str( environ['PATH_INFO'] )
     method    = str( environ['REQUEST_METHOD'] )
     rhost     = str( environ['REMOTE_HOST'] )

  except:
      return '<html><body>bad juju</body></hmtl>'

  try:
     qstring   = str( environ['QUERY_STRING'] )

  except:
      pass

  if qstring:
     if qstring.endswith( 'SaveClr' ):

       ncf     = upcfg( qstring, 'COLOR', lns )

       a = open( cf, 'w' )
       a.write( ncf )
       a.close()

       cfd     = open( cf, 'r' )
       lns     = cfd.readlines()
       cfd.close()


##### parse image on post todo: change qstring, add method
#  if 'title' in qstring:


#  try:
#       body    = read(environ)
#       print(body)
#       path    = FieldStorage(fp=body, environ=environ, keep_blank_values=True)
#       title   = str( path )
#       print( title )
      # title   = str( title.split("dtails', '")[-1] )
      # title   = str( title.split(",")[0] )
      # path    = path["dtails"].value
      # print(path)
#  except:
#        pass


  ### CSS
  cbar = str( cvert( sbr, lns ) )
  tbar = str( cvert( tbr, lns ) )
  tlc  = str( cvert( tlb, lns ) )
  csc  = str( cssc( lns ) )
  csp  = str( sidebar() )
  cs   = str( '%s\n%s\n%s\n%s\n%s\n' % ( cbar, tbar, tlc, csc, csp ) )

  ### JAVA
  jsp  = str( jscr() )

  ### HTML
  whl  = str( vym() )
  body = str( webc( 'body', '/', environ ) )
  pgs  = str( spages( lns, whl ) )

  ### Return Response
  html           = str( '<html><head><style>%s</style><script>%s</script></head><body>%s\n%s</body></html>' % ( cs, jsp, body, pgs ) )

  headers        = [ ('Server', 'ZenKart-0.0.0'),('Content-type', 'text/html'),( 'charset','utf-8') ]
  status         = '200 OK'

  start_response( status, headers )
  return html



def phew():
  try:
     from sys import argv
     port        = int( argv[1] )
  except:
     port        = 8080

  httpd          = make_server('127.0.0.1', port, zkart )


  print( "Accepting on port %d" % port )
  httpd.serve_forever()
  con.close()

phew()
