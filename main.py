import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,m):
        ''' /m_row '''
        
        
        print(9,type(m))

        m = int(m) if m is not None else 9

       
        html ='''
        <html>
        <body>
        <table>
        '''
        for i in range(1,m+1):
            html +='<TR>'
            for j in range(1,i+1):
                html +='<TD>%dx%d=%d</TD>'%(i,j,i*j)
            html +='</TR>'

        html  +='''
        </table>
        </body>
        </html>
        '''

        self.write(html)

application = tornado.web.Application([
    (r"(?:/([0-9]+))?", MainHandler),
],debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
