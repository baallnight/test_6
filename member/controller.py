from member.model import MemberDAO

class MemberController:
    def __init__(self):
        self._dao = MemberDAO()
        #self._dao.create()
        #self._dao.insert_many()

    def login_check(self, userid, password):
        m = self._dao
        data = m.login_check(userid, password)

        view = ''
        if data is None: view = 'index.html'
        else:             view = 'home.html'

        return view

