# -*- coding: utf-8 -*-

import iota
from pprint import pprint

def send_transfer(url, add1, add2, key_index):
    add1 = iota.Address(add1, key_index=key_index, security_level=2)
    add2 = iota.Address(add2)
    unspend = iota.Address(b'COIHHICCHC9JXNBJZXCNNHCRYGEVKKZKJPVJGTEQX9VPWYOJVLEZMBYHJRH9OIRXVFJVTJZHPZMZZYEYB')
    #add1.key_index = 4
    #add1.security_level = 2

    # 1. create transactions
    pt = iota.ProposedTransaction(
        address=add2, 
        tag=iota.Tag(b'HRIBEK999IOTA999TUTORIAL'),
        value=100
    )
    api = iota.Iota(url, seed=b'N9MOJKSFIHTPRIBYDIWEHLRNBLNFSLWPVNYTEGBIRAOZRJSIBXDNCDBVPSEJRFVRSMISGQMSLAGZEVQTR') 
    res = api.send_transfer(
        depth=3,
        transfers=[pt],
        inputs=[add1],
        # if without the change address, iota will generate new address automatically
        # which may waste a lot of time. 
        change_address=unspend,
        min_weight_magnitude=14
    ) 
    
    #pprint(vars(res['bundle'])['transactions']) 
    '''
    txs = vars(res['bundle'])['transactions']
    for tx in txs:
        pprint(vars(tx))
    '''
    return res


def send_text(url):
    add1 = iota.Address(b'TNNAFSHKQHBHRZUBE9ZFPUFKRAZVSUZDXIJEMXOGFRCOAYOBHFIPBKDPOROC9VKJBPRMYUEXGLDUU9II9')
    add2 = iota.Address(b'CAKYWFCCGEIBNHAIRRNZENH9OSMLZBNUNTSXNSZPD9FPFCOBKFPCR9JQQSJDTFZQFKV9CSPRDUOKJMEAX')

    # 1. create transactions
    pt = iota.ProposedTransaction(
        address=add1, 
        message=iota.TryteString.from_unicode('hello, Now'),
        tag=iota.Tag(b'HRIBEK999IOTA999TUTORIAL'),
        value=0
    )
    pt2 = iota.ProposedTransaction(
        address=add2, 
        message=iota.TryteString.from_unicode('hello2, Now'),
        tag=iota.Tag(b'HRIBEK999IOTA999TUTORIAL'),
        value=0
    )
    api = iota.Iota(url, seed=b'N9MOJKSFIHTPRIBYDIWEHLRNBLNFSLWPVNYTEGBIRAOZRJSIBXDNCDBVPSEJRFVRSMISGQMSLAGZEVQTR') 
    res = api.send_transfer(
        depth=3,
        transfers=[pt, pt2, pt, pt2],
        #inputs=[add1],
        #change_address=unspend,
        min_weight_magnitude=9
    ) 


def get_tips():
    api = iota.Iota("http://localhost:14700") 
    tips = api.get_transactions_to_approve(depth=15)
    return tips


if __name__ == '__main__':
   # res = send_transfer()
   send_text()
   #get_bundles()
   #my_send_transfer()


