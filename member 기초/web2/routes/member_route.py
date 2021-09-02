from flask import request, render_template, redirect, Blueprint
import web2.model.member as m

m_service = m.Service()
bp = Blueprint('member', __name__, url_prefix='/member')

@bp.route('/list')
def mem_list():
    arr = m_service.printAll()
    return render_template('member/list.html', mlist=arr)

@bp.route('/add')
def mem_add_get():
    return render_template('member/addForm.html')

@bp.route('/add', methods=['POST'])
def mem_add_post():
    id = request.form['id']
    pw = request.form['pw']
    name = request.form['name']
    email = request.form['email']
    m_service.addMember(m.Member(id=id, pw=pw,name=name,email=email))
    return redirect('/member/list')

@bp.route('/get')
def mem_get():
    id = request.args.get('id', 'A', str)
    m = m_service.getMemberById(id)
    return render_template('member/detail.html', m=m)

@bp.route('/edit', methods=['POST'])
def mem_edit():
    id = request.form['id']
    pw = request.form['pw']
    name = request.form['name']
    email = request.form['email']
    m_service.editMember(m.Member(id=id, pw=pw, name=name, email=email))
    return redirect('/member/list')

@bp.route('/del')
def mem_del():
    id = request.args.get('id', 'A', str)
    m = m_service.delMember(id)
    return redirect('member/list')
