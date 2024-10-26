from flask import Flask
app=Flask(__name__)

@app.route('/home/<uname>')
def home1(uname):
    return("<Marquee width=100% size=14 BgColor=Pink><Font Color=Red> Welcome To Orange</Font> </Marquee><Br><Br><Br><B><Font Size=6 Color=Orange>Welcome: "+uname+"</Font></B>")

if __name__=='__main__':
    app.run()



    