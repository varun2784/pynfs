#!/usr/bin/env python

import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], 'lib'))
import rpc
from nfs4.nfs4lib import NFS4Client
from nfs4.nfs4_const import *

AuthSys = rpc.SecAuthSys(0, '', 100,100,[])

AuthGss = rpc.SecAuthGss()

cs = NFS4Client('authsysclient', sec_list=[AuthSys],host='pip1');
cg = NFS4Client('authgssclient', sec_list=[AuthGss],host='pip1');

#res = cg.compound([cs.putrootfh_op(), cg.lookup_op('exports'),
#                               cg.lookup_op('xfs'), cg.getfh_op()]);

#fh = cg.do_getfh(['exports', 'xfs']);
#res = cs.compound([cs.putrootfh_op(), cs.lookup_op('xfs'), cs.getfh_op()]);
try:
    fh = cs.do_getfh(['xfs']);
except:
    print('got some kinda error, yah yah yah');
fh = cg.do_getfh(['xfs']);


cs.compound([cs.putfh_op(fh), cs.getattr_op(FATTR4_FILEID|FATTR4_FSID)])

#cs.compound([cs.putfh_op(fh), cs.lookup_op('thingy')])

