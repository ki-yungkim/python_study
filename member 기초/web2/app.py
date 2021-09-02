from flask import Flask, render_template
import routes.member_route as me
import web2.model.member as m

m_service = m.Service()

app = Flask(__name__)

app.register_blueprint(me.bp)

@app.route('/')
def root():
    arr = m_service.printAll()
    return render_template('member/list.html', mlist=arr)

if __name__ == '__main__':
    app.run()#flask 서버 실행
    