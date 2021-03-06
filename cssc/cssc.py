# -*- coding: utf-8 -*-

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



def cssc( cfg ):
  ### parse main css by section

  def headc( hic, tlc ):
     print(hic)
     src = '''\
div#header-wrapper {
    background-color: %s;
    font-color:yellow;
    width:100%%;       top:0;
    left:0;           right:0;
    height:66px;
}

body>div#header-wrapper {
    position:fixed;
    margin:0 auto;
    top:0; left:0;
    right:0;
}

div#header {
    height:66px;
    left:0; right:0;
    font-color: yellow;
    margin:0 auto;
    background-color: %s;
    color: %s;
    font-style: oblique;
    font-size: 36px;
    text-align: center;
    left: 15; right: 15;
}

''' % ( hic, hic, tlc )
     return src

  def contc( acc ):
     src = str( '''\
div#content-wrapper {
    margin-left:0; top:66;
    voice-family: "\\"}\\""; 
    voice-family:inherit;
    padding-bottom:0px;
    background-color: %s;
    position:absolute;
}

body>div#content-wrapper {
    margin-left:0;
    background-color: %s;
    margin:0 auto; left: 0;
    top:66; right: 0;
    height:25; width:670px;
    position:fixed;
}

div#content {
    width:720px;
    margin:0 auto;
    background-color: %s;
}
''' % ( acc, acc, acc ) )
     return src

  def footc( acc ):
     src = str( '''\
div#footerwrap {
    width:100%%;
    position:absolute;
    bottom:25; left:0;
    right:0; height:50px;
}

body>div#footerwrap {
   position:absolute;
   left:0; right:0;
}

div#footer {
    height:50px; bottom:0;
    left: 0; right: 0;
    margin:0 auto;
    font-style: oblique;
    color: yellow;
    font-size: 22px;
    text-align: center;
    background-color: %s;
    position:fixed;
}
''' % acc )
     return src

  def malc( prc ):
     src = str( '''\

div#maltent-wrapper {
    background-color: %s;
    font-color: yellow;
    width:100%%;
    top:66;  left:75;
    right:0; potision: absolute;
    height:100%%;
}

body>div#maltent-wrapper {
    margin-left:0; background-color: %s;
    margin:0 auto;
    left: auto; right:0;
    position:fixed right: 15;
    z-index: -3; top:0;
    bottom:auto; width:640px;
}

div#maltent {
    width:719px;
    font-color: yellow;
    margin:0 auto;
    background-color: %s;
    color: #ff0a00;
    font-style: oblique;
    font-size: 36px;
    text-align: center;
    left: 15; right:  15;
    top:   0; bottom: auto;
}
''' % ( prc, prc, prc ) )
     return src


  def glblc( txc, lkc ):
     ### instance or wrapper based css
     src = str('''\
\\a:link { color: %s;
  text-decoration: none; }
label {   color: %s; }
h1 { text-align: center; }


.column-left{ float: left; width: 33%%; margin-left:5; margin-top:5; }
.column-right{ float: right; width: 33%%; margin-top:5; }
.column-center{ display: inline-block; width: 33%%; }
.c-left{ float: left; width:43%%; margin-left:5;  line-height: 2.5; padding-top: 15; top: 15;}
.c-center{ left:50; top:0; padding-left: 25; display: inline-block; width: 33%%; line-height:0.4;}
.f-bottom{ float: bottom; bottom:5; }
.c-l{ float: left; width: 33%%; margin-left:5; margin-top:5; font-size: 135%%;}
.c-r{ float: right; width: 43%%; margin-top:5; }
.cr{ float: right; width: 0%%; top:0; display: inline-block;}
.i-l{ inline-block; top: 0; left: 0; right: 0;}

a:link {
  text-decoration: none;
}

a:visited {
  text-decoration: none;
}

a:active {
  text-decoration: none;
}


body {background-color: #69b543;}

div#wrapper {
  width: 100%%;
  right: 0;
  left: 75;
}

body>div#wrapper-wrapper {
    width: 730px;    top: 90;
    left: 0;    right: 0;
    position: fixed;
    border: 1px solid black;
}

/* from pages */
.close {
  background: #606061;  color: #FFFFFF;
    line-height: 25px;  position: absolute;
         right: -12px;  text-align: center;
           top: -10px;  width: 24px;
             display:   inline-block;
 text-decoration: none;  font-weight: bold;
  -webkit-border-radius: 12px;  -moz-border-radius: 12px;
          border-radius: 12px;   -moz-box-shadow: 1px 1px 3px #000;
  -webkit-box-shadow: 1px 1px 3px #000;  box-shadow: 1px 1px 3px #000;
}

.close:hover { background: #00d9ff; }

.closel {
  background: #606061;  color: #FFFFFF;
    line-height: 25px;  position: absolute;
         left: -12px;  text-align: center;
           top: -10px;  width: 24px;
            display; inline-block;
 text-decoration: none;  font-weight: bold;
  -webkit-border-radius: 12px;  -moz-border-radius: 12px;
          border-radius: 12px;   -moz-box-shadow: 1px 1px 3px #000;
  -webkit-box-shadow: 1px 1px 3px #000;  box-shadow: 1px 1px 3px #000;
}

.closel:hover { background: #00d9ff; }

.closem {
  background: #606061;  color: #FFFFFF;
    line-height: 25px;  position: relative;
         left: 0px;  text-align: center;
         right: auto; margin-left: 60px;
         margin-right: 60px;
           top: -12px;
            display; inline-block;
 text-decoration: none;  font-weight: bold;
  -webkit-border-radius: 12px;  -moz-border-radius: 12px;
          border-radius: 12px;   -moz-box-shadow: 1px 1px 3px #000;
  -webkit-box-shadow: 1px 1px 3px #000;  box-shadow: 1px 1px 3px #000;
}


/* buttons */
.styled-button-5 {
	background-color:#ed8223;
	color:#fff;
	font-family:'Helvetica Neue',sans-serif;
	font-size:18px;
	line-height:30px;
        margin-top: 12px;
        margin-left 12px;

	-webkit-border-radius:20px;
	-moz-border-radius:20px;
	border:2px solid #ed8223;
	text-shadow:#C17C3A 0 -1px 0;
	width:120px;
	height:32px;
        disaplay: inline;
}

.styled-button-5:hover {
  color:purple;
  text-decoration: none;
  border:2px solid purple;
}


/* highlight form */
.form-style-6 input[type="submit"], .form-style-6 input[type="button"] {
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    width: 100%%;
    margin-top:3; margin-bottom: 3;
    padding: 5%%;
    background: #43d1af;
    border-bottom: 2px solid #30c29e;
    border-top-style: none;
    border-right-style: none;
    border-left-style: none;
    color: #fff;
    font-size: 14px;
}

/* orange circle button */
h8 {
       margin-left: 0;  margin-right: 0;
        align: center;  text-align: center;
    font-weight: bold;  length: 35px;
   box-shadow:inset 2px 2px 2px 2px black;
              display:  inline;
             position: relative;
             overflow: hidden;
}

h5  {
    font-family: times;
    font-size: 50%%;
    display: inline;
    padding-left: 25px;
    padding-right: 25px;
    padding-top:0;
    margin-bottom:10px;
}

h2 {
  padding-bottom:0;
  display: inline-block;
}

''' % ( txc, lkc ) )
     return src

  ### define colors from cfg
  clr  = pcfg( cfg, 'COLOR' )

  icc  = str( psec( clr, 'icon-color' ) )
  prc  = str( psec( clr, 'primary-color' ) )
  acc  = str( psec( clr, 'accent-color' ) )
  hic  = str( psec( clr, 'highlight-color' ) ).encode('utf-8')
  lkc  = str( psec( clr, 'link-color' ) )
  txc  = str( psec( clr, 'text-color' ) )
  tlc  = str( psec( clr, 'title-color' ) )

  ### pass colors through css template
  head = str( headc( hic, tlc ) )
  cont = str( contc( acc ) )
  foot = str( footc( acc ) )
  mal  = str( malc( prc ) )
  glbl = str( glblc( txc, lkc ) )
  src  = str( '%s\n\n%s\n\n%s\n\n%s\n\n%s\n' % ( head, cont, foot, mal, glbl ) )

  return src
