def jscr():
  ### select, set - color, conf
  src = str( '''\
function sselect( fid )
{
   document.getElementById('cslct').value = fid;
}

function setcc()
{
  var clr = document.getElementById('tinput').value;
  var fig = document.getElementById('cslct').value;
  var pbx = fig.substring(0, fig.length - 1) + 'b';
  console.log( 'pbx ' + pbx );


  document.getElementById( fig ).value = clr;
  document.getElementById( pbx ).style.backgroundColor = clr;

}

function svclr()
{
  var icr = document.getElementById('icri').value;
  var pcr = document.getElementById('pcri').value;
  var acr = document.getElementById('acri').value;
  var hcr = document.getElementById('hcri').value;

  var lcr = document.getElementById('lcri').value;
  var txt = document.getElementById('txti').value;
  var ttl = document.getElementById('ttli').value;
  var str = icr + ' ' + pcr + ' ' + acr + ' ' + hcr + ' ' + lcr + ' ' +txt + ' ' + ttl;
  console.log( str );
}

function fjava( btn )
{
  document.getElementById( 'uref' ).value = btn;
  if ( btn == 'udelete' )
     document.getElementById( 'urin' ).value = "Delete User?";
  else
     document.getElementById( 'urin' ).value = "";
}

function rmin( str )
{
   document.getElementById( 'refu' ).value = str;
}


''' )
  return src



#'iconc=%2369b543&primec=%23664b4b&accentc=%237d8182&highc=%23272c2e&linkc=yellow&txtc=purple&ttlc=yellow'
