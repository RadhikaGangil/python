from flask import Flask
app=Flask(__name__)  #creating the Flask class object

@app.route('/') # if you put @ before any name it becomes a decorator
def home():
    return ("<Center><H3><OL><LI><A Href=http://www.google.com>Connect To Google</A></LI><LI><A Href=http://www.microsoft.com>Connect To Microsoft</Li></OL></A></Center></H3><BR>")

if __name__=='__main__':
    app.run(port=3290,debug=True)