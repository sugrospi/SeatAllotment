# main.py

from flask import Blueprint, render_template, request , redirect , url_for
from flask_login import login_required, current_user
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/profile',methods =['POST'])
@login_required
def profile_post():
    C1 = request.form.get('C1')
    C2 = request.form.get('C2')
    C3 = request.form.get('C3')
    current_user.C1 = C1
    current_user.C2 = C2
    current_user.C3 = C3
    db.session.commit()
    return redirect(url_for('main.view'))

@main.route('/view')
@login_required
def view():
    all = User.query.all()
    N = len(all)
    wAllot = {'02': -1,'01': -1,'11': -1,'22': -1,'21': -1}
    def preference(man,college,m,m1,w):
        if m > m1:
            return True
        else:
            return False

    def seatallotment(man,college):
        wMan = [False for i in range(N)]
        length = len(college)
        wCollege = []
        wCollege_1 = []
        for i in range(length):
            wCollege.append(len(college.get(str(i))))
            wCollege_1.append(len(college.get(str(i))))

        tot = sum(wCollege)
        freeCount = N
        while(freeCount > 0):
            m = 0
            while(m<N):
                if(wMan[m] == False):
                    break
                m += 1
            if(m>=tot):
                break
            i = 0
            while i < length and wMan[m] == False:
                w = man[m][i]

                if(wCollege[w] > 0):
                    wAllot[str(w) + str(wCollege[w])] = m
                    wCollege[w] -=1
                    wMan[m] = True
                    freeCount -=1
                else:
                    for x in range(0,wCollege_1[w]):
                        m1 = wAllot[str(w) + str(x+1)]

                        if(preference(man,college,m,m1,w) == False):
                            wAllot[str(w) + str(x+1)] = m
                            wMan[m] = True
                            wMan[m1] = False
                i+=1
        print(wAllot)
        for i in range(tot,N):
            print("S"+str(i) + " No seat has been allocated")
    man = []
    for item in all:
        temp = []
        temp.append(item.C1)
        temp.append(item.C2)
        temp.append(item.C3)
        man.append(temp)
    college = {'0':[[0,1,2,3,4],[0,1,2,3,4]],'1':[[0,1,2,3,4]],'2':[[0,1,2,3,4],[0,1,2,3,4]]}
    seatallotment(man,college)
    values = wAllot.values()
    val = []
    for item in values:
        item+=1
        val.append(item)
    message = "no seat alloted"
    msg1 = ""
    if current_user.id in val:
        message = "Yes you have been alloted a seat"
        idx = val.index(current_user.id)
        if idx == 0 or idx == 1:
            msg1 = "You have been allocated a seat in E1"
        elif idx == 2:
            msg1 = "You have been allocated seat in E2"
        else:
            msg1 = "You have been allocated a seat in E3"
    return render_template("view.html",message = message,msg1=msg1)      #here what it does is it gets all of the users and pass them as objects to the render_template i.e to our page
