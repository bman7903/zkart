from . import pcfg

psec = pcfg.psec
pcfg = pcfg.pcfg

def spages( lns, whl ):

  def pnew():
     src = ''' \
<div id="newp" class="modalPage"><div>
  <a href="#close" title="Close" class="close">X</a>

  <form action="#" enctype="multipart/form-data">
     <div class="c-left">
     <div>TITLE:    <br></div>
     <div>CATEGORY: <br></div>
     <div>DESCRIPTION: <br><br><br><br></div>
     <div>PRICE:    <br></div>
     <div>PIECESPR: <br></div>
     <div>QUANTITY: <br></div>



    <div class="f-bottom">
           <input type="submit" class="styled-button-5" id="newitem" name="newitem" value="Commit" data="dtails" action="#"/>
    </form></div>

     </div>
      <div class="c-center"><div class="form-style-6">
 <div><input type="text" name="title"><br><br></div>
 <div><input type="text" name="category"><br><br></div>
 <div><textarea name="description" rows="10" cols="30" resize="none"> DESCRIPTION</textarea><br><br></div>
 <div><input type="text" name="price"><br><br></div>
 <div><input type="text" name="pcspr" value="1"><br><br></div>
 <div><input type="text" name="totalq" value="unlimited"><br><br></div>

</div></div></div></div>

'''
     return src


  def pcal():
     src = ''' \
<div id="calp" class="modalPage"><div>
  <a href="#close" title="Close" class="close">X</a>

  <h2>Calender Box</h2>
   <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>

</div></div>

'''
     return src


  def pitm():
     src = ''' \
<div id="itmp" class="modalPage"><div>
  <a href="#close" class="close">X</a>

  <h2>Items Box</h2>

  <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>

</div></div>

'''
     return src


  def pmet():
     src = ''' \
<div id="metp" class="modalPage"><div>
  <a href="#close" class="close">X</a>

  <h2>Metric Box</h2>
  <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>

</div></div>

'''
     return src

  def pord():
     src = ''' \

<div id="ordp" class="modalPage"><div>
  <a href="#close" title="Close" class="close">X</a>

  <h2>Orders Box</h2>
  <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>

</div></div>

'''
     return src


  def ppic():
     src = ''' \
<div id="picp" class="modalPage"><div>
  <a href="#close" title="Close" class="close">X</a>

  <h2>Picture Box</h2>
  <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>

</div></div>

'''
     return src


  def ppri():
     src = ''' \
<div id="prip" class="modalPage"><div>
  <a href="#close" title="Close" class="close">X</a>

  <h2>Pricing Box</h2>
  <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>

</div></div>

'''
     return src


  def dbse():
     src = ''' \
<div id="database" class="modalPage"><div>
  <a href="#confp" class="close">&lt;</a>
  <a href="#close" class="closel">X</a>

  <h2>Database Box</h2>
  <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>

</div></div>

'''
     return src


  def crdz():
     src = ''' \
<div id="creds" class="modalPage"><div>
  <a href="#confp" class="close">&lt;</a>
  <a href="#close" class="closel">X</a>

  <h2>Creds  Box</h2>
  <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>

</div></div>

'''
     return src


  def imgz():
     src = ''' \
<div id="images" class="modalPage"><div>
  <a href="#confp" class="close">&lt;</a>
  <a href="#close" class="closel">X</a>

  <h2>images Box</h2>
  <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>

 </div></div>

'''
     return src


  def userz():
     src = ''' \
<div id="userz" class="modalPage"><div>
  <a href="#confp" class="close">&lt;</a>
  <a href="#close" class="closel">X</a>

  <h2>Users Box</h2>
   </center><h5><hr =""\></h5><br>

  <select id="uzern">
  <option> Rahoul Utilizator</option>
  </select>      <a id="plusmin"  href="#plusmin"><div class="plusmin" onclick="rmin('uzr')"></div></a>


</div></div>

'''
     return src


  def lgz():
     src = ''' \
<div id="logs" class="modalPage"><div>
  <a href="#confp" class="close">&lt;</a>

  <h2>Logs Box</h2>
  <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>
</div></div>

'''
     return src


  def hlp():
     src = ''' \
<div id="help" class="modalPage"><div>
  <a href="#confp" class="close">&lt;</a>

  <h2>Help Box</h2>
  <p>This is a sample modal box that can be created using the powers of CSS3.</p>
  <p>You could do a lot of things here like have a pop-up ad that shows when your></p>

</div></div>

'''
     return src


  def pcnf():
     src = ''' \
<div id="confp" class="modalPage"><div>
  <a href="#close" class="close">X</a><br><center>

      <a id="paint"     href="#pntp">     <div class="paint">    </div></a>
      <a id="database"  href="#database"> <div class="database"> </div></a>
      <a id="creds"     href="#creds">    <div class="lock">     </div></a>
      <a id="images"    href="#images">   <div class="images">   </div></a>
      <a id="userz"     href="#userz">    <div class="userz">     </div></a>
      <a id="logs"      href="#logs">     <div class="logs">     </div></a>
      <a id="help"      href="#help">     <div class="help">     </div></a>

  </center><h5><hr =""\></h5><br>

<select id="kartn">
 <option> MyKart</option>
</select>      <a id="plusmin"  href="#plusmin"><div class="plusmin" onclick="rmin('krt')"></div></a>


</div></div>

'''
     return src

  def ppnt( clr ):
     icr = str( psec( clr, 'icon-color' ) )
     lcr = str( psec( clr, 'link-color' ) )
     pcr = str( psec( clr, 'primary-color' ) )
     acr = str( psec( clr, 'accent-color' ) )
     hcr = str( psec( clr, 'highlight-color' ) )
     txt = str( psec( clr, 'text-color' ) )
     ttl = str( psec( clr, 'title-color' ) )

     syl = str('''\
     <style>
section.icrx button  { color: #fff; height: 20px: width: 10px; margin-right: 1;  margin-top: 5; background-color: %s; text-shadow: -1px 1px #417cb8; border: none; }
section.lcrx button  { color: #fff; height: 20px: width: 10px; margin-right: 1;  margin-top: 5; background-color: %s; text-shadow: -1px 1px #417cb8; border: none; }
section.pcrx button  { color: #fff; height: 20px: width: 10px; margin-right: 1;  margin-top: 5; background-color: %s; text-shadow: -1px 1px #417cb8; border: none; }
section.acrx button  { color: #fff; height: 20px: width: 10px; margin-right: 1;  margin-top: 5; background-color: %s; text-shadow: -1px 1px #417cb8; border: none; }
section.hcrx button  { color: #fff; height: 20px: width: 10px; margin-right: 1;  margin-top: 5; background-color: %s; text-shadow: -1px 1px #417cb8; border: none; }
section.txtx button  { color: #fff; height: 20px: width: 10px; margin-right: 1;  margin-top: 5; background-color: %s; text-shadow: -1px 1px #417cb8; border: none; }
section.ttlx button  { color: #fff; height: 20px: width: 10px; margin-right: 1;  margin-top: 5; background-color: %s; text-shadow: -1px 1px #417cb8; border: none; }

     </style>
''' % ( icr, lcr, pcr, acr, hcr, txt, ttl ) )

     src = str( ''' \
<div id="pntp" class="modalPage"><div>
  <a href="#confp" class="close">&lt;</a>
  <a href="#close" class="closel">X</a>
  <h2>Color Box</h2>


  <div class="c-l"><br>
  <section class="icrx"><button id="icrb" class="btn" onclick="window.location.href='#whlp'; sselect('icri')">&nbsp;</button> ICON      </section>
  <section class="pcrx"><button id="pcrb" class="btn" onclick="window.location.href='#whlp'; sselect('pcri')">&nbsp;</button> PRIMARY   </section>
  <section class="acrx"><button id="acrb" class="btn" onclick="window.location.href='#whlp'; sselect('acri')">&nbsp;</button> ACCENT    </section>
  <section class="hcrx"><button id="hcrb" class="btn" onclick="window.location.href='#whlp'; sselect('hcri')">&nbsp;</button> HIGHLIGHT </section>
  <section class="lcrx"><button id="lcrb" class="btn" onclick="window.location.href='#whlp'; sselect('lcri')">&nbsp;</button> LINK      </section>
  <section class="txtx"><button id="txtb" class="btn" onclick="window.location.href='#whlp'; sselect('txti')">&nbsp;</button> TEXT      </section>
  <section class="ttlx"><button id="ttlb" class="btn" onclick="window.location.href='#whlp'; sselect('ttli')">&nbsp;</button> TITLE     </section>
  </div>


  <div class="c-r"><form action="#">
  <input name="iconc"  type="text" id="icri" value="%s"></input>
  <input name="primec" type="text" id="pcri" value="%s"></input>
  <input name="acrc"   type="text" id="acri" value="%s"></input>
  <input name="highc"  type="text" id="hcri" value="%s"></input>
  <input name="lcrc"   type="text" id="lcri" value="%s"></input>
  <input name="txtc"   type="text" id="txti" value="%s"></input>
  <input name="ttlc"   type="text" id="ttli" value="%s"></input>

  <br><pre>paint stuff
  <input type="submit" class="styled-button-5" id="saveclr" name="saveclr" value="SaveClr" /></form></div>
  <input id="cslct" type="hidden"></input>
</div></div>

''' % ( icr, pcr, acr, hcr, lcr, txt, ttl ) )

     src = str( '%s\n%s' % ( syl, src ) )
     return src

  def pwhl( whl ):
     src = ''' \
<div id="whlp" class="modalPage"><div>
  <a href="#pntp"  class="close"  > &lt; </a>
  <a href="#close" class="closel" > X    </a>
  %s

  <section onclick="window.location.href='#pntp'; setcc();"><center>
  <button>SET</button>&emsp;<button class="btn" id="prv" onclick="window.location.href='#pntp'; setcc();"></button>
  <input type="text" id="tinput" value="wtf"></input>
  <button class="btn" id="hvb"></button>
  &emsp;<button>ADD^</button></center>

</section>
</div></div>

''' % whl
     return src


  def pmn():
     src = ''' \
<div id="plusmin"   class="modalDialog"><div>
  <a href="#userz"  class="close">&lt;</a>
  <a href="#close"  class="closel">X</a>
  <div class="i-l">

  <a href="#umit">
     <input type="submit" class="styled-button-5"  id="unew"     name="NEW"     value="NEW"    onclick="fjava('uname');"   >
     <input type="submit" class="styled-button-5"  id="urename"  name="RENAME"  value="RENAME" onclick="fjava('urename');" >
     <input type="submit" class="styled-button-5"  id="ucopy"    name="COPY"    value="COPY"   onclick="fjava('ucopy');"   >
     <input type="submit" class="styled-button-5"  id="udelete"  name="DELETE"  value="DELETE" onclick="fjava('udelete');" ></a>
  </div></div></div>

</div></div></div>

'''
     return src

  def pmr():
     src = ''' \
<div id="umit" class="modalPopup"><div>
  <a href="#plusmin" class="close">&lt;</a>
  <a href="#close" class="closel">X</a>
   <div class="closem">POOP</div>
     <div class="i-l">
     <form style="{display: inline-block}">
         &nbsp;<input type="text"   id="urin" name="urin" value="">&nbsp;
               <input type="hidden" id="uref" name="uref" value="">
               <input type="text"   id="refu" name="refu" value="">
               <input type="submit" class="styled-button-5"  value="Commit" >
      </form></input></intput></input>

</div></div></div>

'''
     return src



  ### main
  clr = pcfg( lns, 'COLOR' )

  pn  = str( pnew() )
  pc  = str( pcal() )
  pi  = str( pitm() )
  pm  = str( pmet() )
  po  = str( pord() )
  pp  = str( ppic() )
  pr  = str( ppri() )
  pf  = str( pcnf() )
  pt  = str( ppnt( clr ) )
  pw  = str( pwhl( whl ) )
  db  = str( dbse() )
  cd  = str( crdz() )
  ig  = str( imgz() )
  uz  = str( userz() )
  lg  = str( lgz() )
  hp  = str( hlp() )
  pd  = str( pmn() )
  pz  = str( pmr() )

  src = str( '%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ( pd, pn, pz, pc, pi, pm, po, pp, pr, db, cd, ig, uz, lg, hp, pf, pt, pw ) )
  return src
