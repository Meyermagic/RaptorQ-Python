from __future__ import division
#import array
#from ctypes import *
from math import ceil, floor
import tables

class FECPayloadID(object):
    """
    FEC Payload ID
    http://tools.ietf.org/html/rfc6330#section-3.2
    """
    def __init__(self, SBN, ESI):
        self.SBN = SBN
        self.ESI = ESI


#FEC Encoding ID = 6

class FEC_OTI(object):
    """
    Common FEC Object Transmission Information (OTI)
    http://tools.ietf.org/html/rfc6330#section-3.3.2
    """
    def __init__(self, transfer_length, symbol_size):
        self.F = transfer_length
        self.T = symbol_size

class SS_FEC_OTI(object):
    """
    Scheme-Specific FEC Object Transmission Information
    http://tools.ietf.org/html/rfc6330#section-3.3.3
    """
    def __init__(self, source_block_count, sub_block_count, symbol_alignment):
        self.Z = source_block_count
        self.N = sub_block_count
        self.Al = symbol_alignment


#The recommended setting for the input parameter Al is 4.
#Note: Section 5.1.2 defines K'_max to be 56403.
def get_TZN(F, WS, P_, Al, SS, K__max):
    #TODO: RFC6330, Section 4.3 says we need K'_max here, but then doesn't use it.
    T = P_
    Kt = ceil(F/T)
    N_max = floor(T/(SS*Al))
    def KL(n):
        """
        KL(n) is the maximum K' value in Table 2 in Section 5.6 such
        that K' <= WS/(Al*(ceil(T/(Al*n))))
        """
        return tables.t2_le(WS/(Al*(ceil(T/(Al*n)))))
    Z = ceil(Kt/KL(N_max))
    #N is the minimum n=1, ..., N_max such that ceil(Kt/Z) <= KL(n)
    cktz = ceil(Kt/Z)
    for n in range(1, N_max+1):
        #TODO: This, in constant time.
        if cktz <= KL(n):
            return T, Z, n
    assert False