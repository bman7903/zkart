from re import sub


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



def tsec( sec ):
  ### trim section to add alterd
  new  = []
  cfsn = [ 'COLOR', 'RES SMALL', 'RESOURCE' ]

  for c in cfsn:
     c = str( c )

     if c == sec:
       pass

     else:
       new.append( c )

  return new


def upcfg( new, sec, cur ):
  ### overwrite cfg: new 2 section 2 current 2 file


  def colr(  new ):
     ovr  = icc = prc = acc = hlc = lkc = txc = tlc  = ''

     for arg in new.split( '&' ):
       arg = str( arg )

       if '%' in arg:
          arg = str( sub( '%23', '#', arg ) )

       opt = str( arg.split('=')[-1] )

       if arg.startswith( 'iconc' ):
          icc = opt
       if arg.startswith( 'primec' ):
          prc = opt
       if arg.startswith( 'acrc' ):
          acc = opt
       if arg.startswith( 'highc' ):
          hlc = opt
       if arg.startswith( 'lcrc' ):
          lkc = opt
       if arg.startswith( 'txtc' ):
          txc = opt
       if arg.startswith( 'ttlc' ):
          tlc = opt

     ovr = str( '''### COLOR START\n\nicon-color: %s\nprimary-color: %s\naccent-color: %s\n
highlight-color: %s\nlink-color: %s\ntext-color: %s\ntitle-color: %s\n\n### COLOR END''' % ( icc, prc, acc, hlc, lkc, txc, tlc ) )
     return ovr



  ### add unalterd section to new
  ret  = ''
  x    = 1
  unlt = tsec( sec )

  if sec  == 'COLOR':
     ovr = colr( new )

  for c in unlt:
     c   = str( c )
     cfs = pcfg( cur, c )
     lc  = len( cfs )

     for f in cfs:
       f = str( f )

       if x == 1:
          ret = str( '%s### %s START\n' % ( ret, c) )

       ret = str( '%s\n%s' % ( ret, f ) )

       if x == lc:
          ret = str( '%s\n\n### %s END\n\n' % ( ret, c ) )
          x   = 1

       else:
          x = x + 1

  ret = str( '%s\n\n%s' % ( ret, ovr ) )

  return ret
