"""Start applicacion base"""

# Libraries
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """Main Handler"""
    def get(self):
        """Get Write Data"""
        self.write('Hello World')


def suma(a: int, b: int) -> int:
    """Sum the data"""
    return a + b
