import webapp2
from caesar import encrypt
import cgi

form = """
<!DOCTYPE html>
<html>
  <head>
    <title>Caesar Unit2 Homework2</title>
  </head>

  <body>
      <form method="post">
        <label><b>Rotation Amount:</b></label>
          <input type="text" name="rotation" value="%(rotation)s"
                    style="height: 20px; width: 50px">
      <br>
        <p><label><b>Secret Message:</b></label></p>
          <textarea name="text" value="%(text)s" style="height: 100px; width: 400px">
          </textarea>
      <br>
        <p><input type="submit" value="Submit"></p>
    </form>
  </body>
  <footer>
  </footer>
</html>
"""

def escape_html(s):
    return cgi.escape(s, quote = True)

class MainHandler(webapp2.RequestHandler):
    def write_form(self, rotation="", text=""):
        self.response.out.write(form % {"rotation": rotation,
                                        "text": text})

    def get(self):
        self.write_form()

    def post(self):
        user_rot = int(escape_html(self.request.get("rotation")))
        user_message = escape_html(self.request.get("text"))
        answer = encrypt(user_message, user_rot)
        self.write_form(user_rot, answer)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
