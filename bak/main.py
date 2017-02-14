import webapp2

#from metric.header import headerz





class MainPage(webapp2.RequestHandler):
  def do( self, proc ):
     raw  = self.request
     proc = str( proc )

     HTML = '<html><body>mwahaha</body></hmtl>'

     self.response.headers['Content-Type'] = 'text/html'
     self.response.write(HTML)


  def post( self, proc=None ):
     self.do('POST')

  def get( self, proc=None ):
     self.do('GET')



app = webapp2.WSGIApplication([
    ( '/', MainPage,),
], debug=True,)
