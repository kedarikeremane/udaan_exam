import sys
import random
import sqlite3 as db
from random import Random

def creating_que(queid, que, opt,ans):
    sql=''' create table if not exists questions(
        qid number,
        Question string,
        Options array,
        answer string,
        primary key(qid))'''
    cur.execute(sql)
    conn.commit()
    sql1='''insert into questions values(
             {},
             "{}",
                "{}",
                "{}")'''.format(queid,que,opt,ans)
    cur.execute(sql1)
    conn.commit()

def creating_quiz_table(quizid,quizname):
    sql='''create table if not exists quiz(
        quizid number,
        quizname string,
        primary key(quizid))'''
    cur.execute(sql)
    conn.commit()
    sql1='''insert into quiz values(
        {},
        "{}")'''.format(quizid,quizname)
    cur.execute(sql1)
    conn.commit()

def creating_rel_table(quizid,quesid):
    sql='''create table if not exists reltable(
        quizid number,
        queid number,
        foreign key(quizid,queid)
    )'''
    cur.execute(sql)
    conn.commit()
    sql='''insert into reltable values(
        {},
        {})'''.format(quizid,quesid)

def view(uinp):
    sql='''select quizname from quiz
        WHERE quizid={}'''.format(uinp)
    cur.execute(sql)
    results=cur.fetchall()
    print(results)

    

conn=db.connect("quiz.db")
cur=conn.cursor()
questionID=4
que="Is 5>4?"
options={'A':"true", "B":"false"}
ans="A"
creating_que(questionID,que,options,ans)
creating_que(questionID,que,options,ans)
creating_quiz_table(quizid=1, quizname="A")
creating_quiz_table(quizid=2, quizname="B")
creating_quiz_table(quizid=3, quizname="C")
creating_rel_table(quizid=1,quesid=1)
creating_rel_table(quizid=1,quesid=2)
creating_rel_table(quizid=2,quesid=3)

uin=input("enter quiz id to show qustions?")
view(uin)
