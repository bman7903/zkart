

def sidebar():
  sbr = '''\
  .modalPage {
                position: absolute;
                font-family: Arial, Helvetica, sans-serif;
                top: 80;
                right: 0;
                bottom: 0;
                left: 40;
                margin-left:20;
                padding-left: 50;
                width: 505px;  height: 460px;
                background: rgba(0,0,0,0.8);
                z-index: 99999;
                opacity:0;
                border-radius: 25px;
                -webkit-transition: opacity 1s ease-in;
                -moz-transition: opacity 1s ease-in;
                transition: opacity 1s ease-in;
                pointer-events: none;
        }

        .modalPage:target {
                opacity:1;
                position: fixed;
                top: 80; left: 40; right: 0; bottom: 0;
                pointer-events: auto;
                width: 505px; height: 460px;
                border-radius: 25px;
        }

        .modalPage > div {
                margin-top: 30;
                top 80:
                left:5; right: 5;
                margin-top: 10;
                margin-right: 5;
                margin-left: 2;
                padding-left: 2;
                margin-bottom: 5;
                width: 530px;
                height: 440px;

                position: absolute;
                border-radius: 25px;
                background: -moz-linear-gradient(#fff, #999);
                background: -webkit-linear-gradient(#fff, #999);
                background: -o-linear-gradient(#fff, #999);
        }

  '''

  dbr = '''\
  .modalDialog {
                position: absolute;
                font-family: Arial, Helvetica, sans-serif;
                top: 80;
                right: 0;
                bottom: 0;
                left: 40;
                margin-left:20;
                padding-left:20;
                width: 265px;  height: 120px;
                background: rgba(0,0,0,0.8);
                z-index: 99999;
                opacity:0;
                border-radius: 25px;
                -webkit-transition: opacity 1s ease-in;
                -moz-transition: opacity 1s ease-in;
                transition: opacity 1s ease-in;
                pointer-events: none;
        }

        .modalDialog:target {
                opacity:1;
                position: fixed;
                top: 80; left: 40; right: 0; bottom: 0;
                pointer-events: auto;
                width: 265px; height: 120px;
                border-radius: 25px;
        }

        .modalDialog > div {
                margin-top: 30;
                top 80:
                left:5; right: 5;
                margin-top: 10;
                margin-right: 5;
                margin-left: 2;
                padding-left: 2;
                margin-bottom: 5;
                width: 265px;
                height: 100px;

                position: absolute;
                border-radius: 25px;
                background: -moz-linear-gradient(#fff, #999);
                background: -webkit-linear-gradient(#fff, #999);
                background: -o-linear-gradient(#fff, #999);
        }

  '''

  rbr = '''\
  .modalPopup {
                position: absolute;
                font-family: Arial, Helvetica, sans-serif;
                top: 80;
                right: 0;
                bottom: 0;
                left: 40;
                margin-left:5;
                padding-left:5;
                margin-top:4; padding-top:4;
                margin-bottom:4; padding-bottom:4;
                width: 390px;  height: 50px;
                background: rgba(0,0,0,0.8);
                z-index: 99999;
                opacity:0;
                border-radius: 25px;
                -webkit-transition: opacity 1s ease-in;
                -moz-transition: opacity 1s ease-in;
                transition: opacity 1s ease-in;
                pointer-events: none;
        }

        .modalPopup:target {
                opacity:1;
                position: fixed;
                top: 80; left: 40; right: 0; bottom: 0;
                pointer-events: auto;
                width: 410px; height: 95px;
                border-radius: 25px;
                padding-left:5;
                margin-left:5;
        }

        .modalPopup > div {
                top 80:
                left:5; right: 5;
                margin-right: 5;
                margin-left: 2;
                padding-left: 2;
                width: 390px;
                margin-top;5;
                margin-bottom:5;
                height: 50x;
                position: absolute;
                border-radius: 25px;
                background: -moz-linear-gradient(#fff, #999);
                background: -webkit-linear-gradient(#fff, #999);
                background: -o-linear-gradient(#fff, #999);
        }

  '''



  src = str( '%s\n\n%s\n\n%s' % ( sbr, dbr , rbr ) )
  return src
