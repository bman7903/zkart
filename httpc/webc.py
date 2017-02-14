# -*- coding: utf-8 -*-

def webc( mthd, pth, vars=None ):
  ### parse mathod, path, vars, return html

  ### bounds
  if pth:
     mthd = str( mthd )
     pth  = str( pth )
  else:
     return


  def body( head ):
     html = str( '''\
<div id="header-wrapper"><div id="header">
  <center><div class="zkart"/></center>
</div></div>

<div id="content-wrapper" >
  <a id="users"     href="#entance"><div class="user"> </a></div>
</div>

<div id="maltent-wrapper" ><br><br><br>
<br><br><div><div class="column-left"><br>
  <a id="new"      href="#newp"><div class="new"></div></a><br>
  <a id="calender" href="#calp"><div class="calender"></div></a><br>
  <a id="items"    href="#itmp"><div class="items"></div></a><br>
  <a id="metrics"  href="#metp"><div class="metrics"></div></a><br>
  <a id="ordering" href="#ordp"><div class="ordering"></div></a><br>
  <a id="pictures" href="#picp"><div class="pictures"></div></a><br>
  <a id="pricing"  href="#prip"><div class="pricing"></div></a><br>
</div></div>
<div class="column-center">
mooo<br>%s<br><br><br><br>

</div>
<div class="column-right"></div>

<!--
<div id="wrapper">
  <form action="/" method="post" type="image" class="bi"><div class="bi"></div></form>

  <br><br><br><br>-->
  <div id="footerwrap"><div id="footer">
   <div class="column-left"> <a href="#savep"><div class="save"></div></a></div>
   <div class="column-center"><label>Some Tail</div>
   <div class="column-right"> <a href="#confp"><div class="conf"></div></a></div>
</div>
</div>''' % head )
     return html


  def lost():
     html = 'are you lost, would like some candy?'
     return html

  def landing():
     html = str( body() )
     return html

  ### main
#  try:
#     ret  = eval( mthd )
#     ret  = str( ret() )
#     return ret
#  except:
#     return 'The Wizard is unavailable at the moment.'

  if mthd == 'body':
     src = str( body( vars ) )
     return src
