from os import path, getcwd
from re import sub

join  = path.join
sep   = path.sep
exist = path.exists


def bxcss( clz ):
  src = '''\
section.prv button  { color: #fff; height: 20px: width: 10px; margin-right: 1;  margin-top: 5; background-color: #000000; text-shadow: -1px 1px #417cb8; border: none; }
.btn              { width: 25px; height: 25px; -webkit-transform: perspective(1px) translateZ(0); transform: perspective(1px) translateZ(0); -webkit-transition-duration: 0.1s; transition-duration: 0.1s; -webkit-transition-property: transform; transition-property: transform; }
.btn:hover        { -webkit-transform: scale(1.4); transform: scale(1.4); -webkit-transition-duration: 0.1s; transition-duration: 0.1s;  -webkit-transition-property: transform; transition-property: transform; js:click(); }

section.hvb button  { color: #fff; height: 20px: width: 10px; margin-right: 1;  margin-top: 5; background-color: #000000; text-shadow: -1px 1px #417cb8; border: none; }

'''


  for c in clz:
     c = str( c )
     src = str( '''%s\
section.c%s button  { color: #fff; height: 20px: width: 10px; margin-right: 1;  margin-top: 5; background-color: #%s; text-shadow: -1px 1px #417cb8; border: none; }
''' % ( src, c, c ) )

  return src


def bxhtml( clz ):
  x   = 1
  rt  = []
  src = ''

  row = 13
  cl  = len( clz )

  for c in clz:
     c   = str( c )
     #cl  = str( '#%s' % c )
     src = str( '''%s\
<section class="c%s"><button class="btn" onClick="reply_click('%s')" onmouseover="hv_over('%s')"> </button></section>
''' % ( src, c, c, c ) )

     if ( x % row == 0 ):
          rt.append( src )
          src = ''
          x = x + 1

     else:
       x = x + 1

  src = str( '''%s<section class="c000000"><button class="btn"  onClick="reply_click(c000000)"> </button></section>''' % src )
  rt.append( src )

  x   = 0
  src = '<div id="column"><div class = "blocks"><table>'

  for r in rt:
     r   = str( r )
     src = str( '%s<td>%s</td>' % ( src, r ) )
     x   = x + 1

  src = str( '''%s\n</table></div>''' % src )
  return src

def bxjsp():
  src = '''\
function reply_click( hv_clr )
{
   var ful = '#' + hv_clr
   document.getElementById( 'tinput' ).value = ful;
   document.getElementById( 'prv' ).style.backgroundColor = ful;
}

function hv_over( hv_clr )
{
  var ful = '#' + hv_clr
  document.getElementById( 'hvb' ).style.backgroundColor = ful;
}

 '''
  return src

def pclrs( fp ):
  ### parse file for hex colors, return as array
  clz = []

  if exist( fp ):
     a   = open( fp, 'r' )

     for ln  in a.readlines():
       ln = str( ln )
       ln = str( sub( '\n', '', ln ) )
       la = len( ln )

       if la == 7:
          if ln.startswith('#'):
            ln = str( sub( '#', '', ln ) )
            clz.append( ln )

  else:
     return

  return clz


def vym():

  cwd = str( getcwd() )
  dp  = str( join( sep, cwd, 'figc'  ) )
  fp  = str( join( sep, dp, 'safe.txt' ) )
  clz = pclrs( fp )

  if clz:
     cs  = str( bxcss( clz ) )
     h5  = str( bxhtml( clz ) )
     jsp = str( bxjsp() )
     src = str( '\n\n<style>%s</style><script>%s</script>\n\n%s' % ( cs, jsp, h5 ) )
     return src

  else:
    return str( '%s color config not found' % fp )
