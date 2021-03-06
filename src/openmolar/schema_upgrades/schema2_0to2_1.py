# -*- coding: utf-8 -*-
# Copyright (c) 2012 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# See the GNU General Public License for more details.

'''
This module provides a function 'run' which will move data
to schema 2_1
'''
from __future__ import division

import logging
import sys
from openmolar.settings import localsettings
from openmolar.dbtools import schema_version
from openmolar import connect

from PyQt4 import QtGui, QtCore


logging.basicConfig()

SQLSTRINGS = [
'drop table if exists currtrtmt2',

'''
create table currtrtmt2 (
  courseno   int(11) unsigned not null auto_increment ,
  serialno   int(11)     ,
  examt      varchar(10) NOT NULL default '',
  examd      date        ,
  accd       date        ,
  cmpd       date        ,
  xraypl     varchar(56) NOT NULL default '' ,
  periopl    varchar(56) NOT NULL default '' ,
  anaespl    varchar(56) NOT NULL default '' ,
  otherpl    varchar(56) NOT NULL default '' ,
  ndupl      varchar(56) NOT NULL default '' ,
  ndlpl      varchar(56) NOT NULL default '' ,
  odupl      varchar(56) NOT NULL default '' ,
  odlpl      varchar(56) NOT NULL default '' ,
  custompl   varchar(56) NOT NULL default '' ,
  ur8pl      varchar(34) NOT NULL default '' ,
  ur7pl      varchar(34) NOT NULL default '' ,
  ur6pl      varchar(34) NOT NULL default '' ,
  ur5pl      varchar(34) NOT NULL default '' ,
  ur4pl      varchar(34) NOT NULL default '' ,
  ur3pl      varchar(34) NOT NULL default '' ,
  ur2pl      varchar(34) NOT NULL default '' ,
  ur1pl      varchar(34) NOT NULL default '' ,
  ul1pl      varchar(34) NOT NULL default '' ,
  ul2pl      varchar(34) NOT NULL default '' ,
  ul3pl      varchar(34) NOT NULL default '' ,
  ul4pl      varchar(34) NOT NULL default '' ,
  ul5pl      varchar(34) NOT NULL default '' ,
  ul6pl      varchar(34) NOT NULL default '' ,
  ul7pl      varchar(34) NOT NULL default '' ,
  ul8pl      varchar(34) NOT NULL default '' ,
  ll8pl      varchar(34) NOT NULL default '' ,
  ll7pl      varchar(34) NOT NULL default '' ,
  ll6pl      varchar(34) NOT NULL default '' ,
  ll5pl      varchar(34) NOT NULL default '' ,
  ll4pl      varchar(34) NOT NULL default '' ,
  ll3pl      varchar(34) NOT NULL default '' ,
  ll2pl      varchar(34) NOT NULL default '' ,
  ll1pl      varchar(34) NOT NULL default '' ,
  lr1pl      varchar(34) NOT NULL default '' ,
  lr2pl      varchar(34) NOT NULL default '' ,
  lr3pl      varchar(34) NOT NULL default '' ,
  lr4pl      varchar(34) NOT NULL default '' ,
  lr5pl      varchar(34) NOT NULL default '' ,
  lr6pl      varchar(34) NOT NULL default '' ,
  lr7pl      varchar(34) NOT NULL default '' ,
  lr8pl      varchar(34) NOT NULL default '' ,
  ur8cmp     varchar(34) NOT NULL default '' ,
  ur7cmp     varchar(34) NOT NULL default '' ,
  ur6cmp     varchar(34) NOT NULL default '' ,
  ur5cmp     varchar(34) NOT NULL default '' ,
  ur4cmp     varchar(34) NOT NULL default '' ,
  ur3cmp     varchar(34) NOT NULL default '' ,
  ur2cmp     varchar(34) NOT NULL default '' ,
  ur1cmp     varchar(34) NOT NULL default '' ,
  ul1cmp     varchar(34) NOT NULL default '' ,
  ul2cmp     varchar(34) NOT NULL default '' ,
  ul3cmp     varchar(34) NOT NULL default '' ,
  ul4cmp     varchar(34) NOT NULL default '' ,
  ul5cmp     varchar(34) NOT NULL default '' ,
  ul6cmp     varchar(34) NOT NULL default '' ,
  ul7cmp     varchar(34) NOT NULL default '' ,
  ul8cmp     varchar(34) NOT NULL default '' ,
  ll8cmp     varchar(34) NOT NULL default '' ,
  ll7cmp     varchar(34) NOT NULL default '' ,
  ll6cmp     varchar(34) NOT NULL default '' ,
  ll5cmp     varchar(34) NOT NULL default '' ,
  ll4cmp     varchar(34) NOT NULL default '' ,
  ll3cmp     varchar(34) NOT NULL default '' ,
  ll2cmp     varchar(34) NOT NULL default '' ,
  ll1cmp     varchar(34) NOT NULL default '' ,
  lr1cmp     varchar(34) NOT NULL default '' ,
  lr2cmp     varchar(34) NOT NULL default '' ,
  lr3cmp     varchar(34) NOT NULL default '' ,
  lr4cmp     varchar(34) NOT NULL default '' ,
  lr5cmp     varchar(34) NOT NULL default '' ,
  lr6cmp     varchar(34) NOT NULL default '' ,
  lr7cmp     varchar(34) NOT NULL default '' ,
  lr8cmp     varchar(34) NOT NULL default '' ,
  xraycmp    varchar(56) NOT NULL default '' ,
  periocmp   varchar(56) NOT NULL default '' ,
  anaescmp   varchar(56) NOT NULL default '' ,
  othercmp   varchar(56) NOT NULL default '' ,
  nducmp     varchar(56) NOT NULL default '' ,
  ndlcmp     varchar(56) NOT NULL default '' ,
  oducmp     varchar(56) NOT NULL default '' ,
  odlcmp     varchar(56) NOT NULL default '' ,
  customcmp  varchar(56)NOT NULL default '' ,
PRIMARY KEY (courseno),
INDEX (serialno)
)'''
]


SOURCE_QUERY = '''
SELECT courseno, serialno, examt, examd, accd, cmpd,
xraypl, periopl, anaespl, otherpl, ndupl, ndlpl,
odupl, odlpl, custompl,
ur8pl, ur7pl, ur6pl, ur5pl, ur4pl, ur3pl, ur2pl, ur1pl, ul1pl, ul2pl,
ul3pl, ul4pl, ul5pl, ul6pl, ul7pl, ul8pl, ll8pl, ll7pl, ll6pl, ll5pl, ll4pl,
ll3pl, ll2pl, ll1pl, lr1pl, lr2pl, lr3pl, lr4pl, lr5pl, lr6pl, lr7pl, lr8pl,
ur8cmp, ur7cmp, ur6cmp, ur5cmp, ur4cmp, ur3cmp, ur2cmp, ur1cmp, ul1cmp,
ul2cmp, ul3cmp, ul4cmp, ul5cmp, ul6cmp, ul7cmp, ul8cmp, ll8cmp, ll7cmp,
ll6cmp, ll5cmp, ll4cmp, ll3cmp, ll2cmp, ll1cmp, lr1cmp, lr2cmp, lr3cmp,
lr4cmp, lr5cmp, lr6cmp, lr7cmp, lr8cmp,
xraycmp, periocmp, anaescmp, othercmp,
nducmp, ndlcmp, oducmp, odlcmp, customcmp
from currtrtmt order by courseno'''

DEST_QUERY = '''
insert into currtrtmt2 (serialno, examt, examd, accd, cmpd,
xraypl, periopl, anaespl, otherpl, ndupl, ndlpl,
odupl, odlpl, custompl,
ur8pl, ur7pl, ur6pl, ur5pl, ur4pl, ur3pl, ur2pl, ur1pl, ul1pl, ul2pl,
ul3pl, ul4pl, ul5pl, ul6pl, ul7pl, ul8pl, ll8pl, ll7pl, ll6pl, ll5pl, ll4pl,
ll3pl, ll2pl, ll1pl, lr1pl, lr2pl, lr3pl, lr4pl, lr5pl, lr6pl, lr7pl, lr8pl,
ur8cmp, ur7cmp, ur6cmp, ur5cmp, ur4cmp, ur3cmp, ur2cmp, ur1cmp, ul1cmp,
ul2cmp, ul3cmp, ul4cmp, ul5cmp, ul6cmp, ul7cmp, ul8cmp, ll8cmp, ll7cmp,
ll6cmp, ll5cmp, ll4cmp, ll3cmp, ll2cmp, ll1cmp, lr1cmp, lr2cmp, lr3cmp,
lr4cmp, lr5cmp, lr6cmp, lr7cmp, lr8cmp,
xraycmp, periocmp, anaescmp, othercmp,
nducmp, ndlcmp, oducmp, odlcmp, customcmp)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

PATIENT_QUERY = '''
update patients set courseno0=%s where serialno=%s and courseno0=%s
'''

ESTIMATES_QUERY = '''
update newestimates set courseno=%s where serialno=%s and courseno=%s
'''

GARBAGE_QUERY = '''
delete from currtrtmt2
WHERE examt="" AND xraypl="" AND periopl="" AND anaespl="" AND otherpl=""
AND ndupl="" AND ndlpl="" AND odupl="" AND odlpl="" AND custompl=""
AND ur8pl="" AND ur7pl="" AND ur6pl="" AND ur5pl="" AND ur4pl="" AND ur3pl=""
AND ur2pl="" AND ur1pl="" AND ul1pl="" AND ul2pl="" AND ul3pl="" AND ul4pl=""
AND ul5pl="" AND ul6pl="" AND ul7pl="" AND ul8pl="" AND ll8pl="" AND ll7pl=""
AND ll6pl="" AND ll5pl="" AND ll4pl="" AND ll3pl="" AND ll2pl="" AND ll1pl=""
AND lr1pl="" AND lr2pl="" AND lr3pl="" AND lr4pl="" AND lr5pl="" AND lr6pl=""
AND lr7pl="" AND lr8pl="" AND
ur8cmp="" AND ur7cmp="" AND ur6cmp="" AND ur5cmp="" AND ur4cmp="" AND
ur3cmp="" AND ur2cmp="" AND ur1cmp="" AND ul1cmp="" AND ul2cmp="" AND
ul3cmp="" AND ul4cmp="" AND ul5cmp="" AND ul6cmp="" AND ul7cmp="" AND
ul8cmp="" AND ll8cmp="" AND ll7cmp="" AND ll6cmp="" AND ll5cmp="" AND
ll4cmp="" AND ll3cmp="" AND ll2cmp="" AND ll1cmp="" AND lr1cmp="" AND
lr2cmp="" AND lr3cmp="" AND lr4cmp="" AND lr5cmp="" AND lr6cmp="" AND
lr7cmp="" AND lr8cmp="" AND
xraycmp="" AND periocmp="" AND anaescmp="" AND othercmp="" AND nducmp=""
AND ndlcmp="" AND oducmp="" AND odlcmp="" AND customcmp=""
'''

## don't use this one.. seems unnecessary.

CORRECTION_QUERY = '''
update patients join
(select serialno, max(courseno) cno from currtrtmt2 group by serialno) as t
on t.serialno = patients.serialno set courseno0 = cno
where cno > courseno0
'''

class UpdateException(Exception):
    '''
    A custom exception. If this is thrown the db will be rolled back
    '''
    pass

class dbUpdater(QtCore.QThread):
    def __init__(self, parent=None):
        super(dbUpdater, self).__init__(parent)
        self.stopped = False
        self.path = None
        self.completed = False
        self.MESSAGE = "upating database"

    def progressSig(self, val, message=""):
        '''
        emits a signal showing how we are proceeding.
        val is a number between 0 and 100
        '''
        if message != "":
            self.MESSAGE = message
        self.emit(QtCore.SIGNAL("progress"), val, self.MESSAGE)

    def execute_statements(self, sql_strings):
        '''
        execute the above commands
        NOTE - this function may fail depending on the mysql permissions
        in place
        '''
        db = connect.connect()
        db.autocommit(False)
        cursor = db.cursor()
        sucess = False
        try:
            i, commandNo = 0, len(sql_strings)
            for sql_string in sql_strings:
                try:
                    cursor.execute(sql_string)
                except connect.GeneralError, e:
                    print "FAILURE in executing sql statement",  e
                    print "erroneous statement was ",sql_string
                    if 1060 in e.args:
                        print "continuing, as column already exists issue"
                self.progressSig(2+70*i/commandNo,sql_string[:40]+"...")
            sucess = True
        except Exception, e:
            print "FAILURE in executing sql statements",  e
            db.rollback()
        if sucess:
            db.commit()
            db.autocommit(True)
        else:
            raise UpdateException("couldn't execute all statements!")

    def completeSig(self, arg):
        self.emit(QtCore.SIGNAL("completed"), self.completed, arg)

    def run(self):
        print "running script to convert from schema 2.0 to 2.1"
        try:
            #- execute the SQL commands
            self.progressSig(5, _("creating currtrtmt2 table"))
            self.execute_statements(SQLSTRINGS)
            self.progressSig(10, _('transferring data'))

            self.transfer_data()

            self.progressSig(95, _("deleting void courses"))
            self.execute_statements([GARBAGE_QUERY, CORRECTION_QUERY])

            self.progressSig(97, _('updating settings'))
            print "update database settings..."

            schema_version.update(("2.1",), "2_0 to 2_1 script")

            self.progressSig(100, _("updating stored schema version"))
            self.completed = True
            self.completeSig(_("ALL DONE - sucessfully moved db to")
            + " 2.1")

        except UpdateException, e:
            localsettings.CLIENT_SCHEMA_VERSION = "2.0"
            self.completeSig(_("rolled back to") + " 2.0")

        except Exception, e:
            print "Exception caught",e
            self.completeSig(str(e))

        return self.completed

    def transfer_data(self):
        '''
        function specific to this update.
        '''
        db = connect.connect()
        db.autocommit(False)
        try:
            cursor = db.cursor()
            cursor.execute(SOURCE_QUERY)
            rows = cursor.fetchall()
            cursor.close()
            cursor = db.cursor()
            step = 1 / len(rows)
            for i, row in enumerate(rows):
                courseno = row[0]
                serialno = row[1]
                cursor.execute(DEST_QUERY, row[1:])
                new_cno = db.insert_id()
                cursor.execute(PATIENT_QUERY, (new_cno, serialno, courseno))
                cursor.execute(ESTIMATES_QUERY, (new_cno, serialno, courseno))
                if i % 100 == 0:
                    self.progressSig(80 * i/len(rows) + 10,
                    _("transfering data"))
            cursor.close()
            db.commit()
            db.close()
        except Exception as exc:
            logging.exception("error transfering data")
            db.rollback()
            raise UpdateException(exc)

if __name__ == "__main__":
    dbu = dbUpdater()
    if dbu.run():
        print "ALL DONE, conversion sucessful"
    else:
        print "conversion failed"
