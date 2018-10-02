# -*- coding: utf-8 -*-

import iota
from datetime import datetime
from pprint import pprint

# transfer between trytes and trits
def trytes_encode():
    trytes_bytes = 'YZJEATEQ9JKLZ'
    trytes = iota.TryteString(trytes_bytes)
    pprint(trytes)

    trits = trytes.as_trits()
    print(trits)


# getNodeInfo
def get_node_info():
    node_url = 'http://localhost:14700'
    api = iota.Iota(node_url)
    res = api.get_node_info()
    print(res)


def get_tips():
    api = iota.Iota("http://localhost:14700") 
    tips = api.get_transactions_to_approve(depth=2)
    return tips


def my_send_transfer():
    add1 = iota.Address(b'BUFVPNVBDXLJSJTVBZTKLUOBVZIMXZODRTHOFGNNJOAXJOKUNIDLFMYSTXMUAYDBLHGTGFFSECFCQV9GZ')
    add2 = iota.Address(b'FWYJNMOZ9WSHNJQVZUACHUCTDFSREKJZSJGORAIEMOCKFHJZEBIYMGOIEAJHIFZHQDDEBPFZZC99SZKPY')
    unspend = iota.Address(b'HSQFLPJDQDWLRUFUSCCALKTFIOSAMLKJ9FXVGDMIHVGJZBATK99BOLDGKBTHVN9Z9MFXCYZK9YGHGQPZ9')

    now = datetime.now()
    add1.key_index = 2
    add1.security_level=2

    # 1. create transactions
    pt = iota.ProposedTransaction(
        address=add1, 
        message=iota.TryteString.from_unicode('hello, Now is %s' % (now)),
        tag=iota.Tag(b'HRIBEK999IOTA999TUTORIAL'),
        value=0
    )
    pt2 = iota.ProposedTransaction(
        address=add2, 
        message=iota.TryteString.from_unicode('hello2, Now is %s' % (now)),
        tag=iota.Tag(b'HRIBEK999IOTA999TUTORIAL'),
        value=0
    )
    #pprint(vars(pt))
    #print('\n')
    #pprint(vars(pt2))

    # 2. create bundle
    pb = iota.ProposedBundle(transactions=[pt, pt2])      # receiever tx
    #pb._transactions.append(pt)                       # input tx      
    #pb.send_unspent_inputs_to(unspend)                # unspend tx  

    # finalize: generate bundle hash + normalize bundle hash + copy bundle hash into each tx
    pb.finalize()
    print(pb.hash)

    # the first tx in bundle called tail transaction
    #print(pb.tail_transaction.current_index)     # 0

    for tx in pb:
       pprint(vars(tx))

    # encode bundle into trytes
    trytes = pb.as_tryte_strings()


    # 3. tips selection
    api = iota.Iota("http://localhost:14700") 

    tips = api.get_transactions_to_approve(depth=3)       # return trunk and branch

    '''
    tips = {
        'branchTransaction': iota.Hash(b'IPSRKCCKMWM9VQVJDVHQYGYFXTAFYGZYAZPTUTANMDFLXYBHNKPTNBQRLRZXMFXVDPKPNJPOBFDDA9999'),
        'duration': 1,
        'trunkTransaction': iota.Hash(b'IPSRKCCKMWM9VQVJDVHQYGYFXTAFYGZYAZPTUTANMDFLXYBHNKPTNBQRLRZXMFXVDPKPNJPOBFDDA9999')
    }
    '''
    pprint(tips)

    # 4. Do PoW
    # return the new bundle that each tx in it get the nonce and tx_hash
    att = api.attach_to_tangle(
        trunk_transaction=tips['trunkTransaction'],
        branch_transaction=tips['branchTransaction'],
        trytes=trytes,
        min_weight_magnitude=14
    )
    
    # every tx in final bundle
    #for i in att['trytes']:
    #    pprint(vars(iota.Transaction.from_tryte_string(i)))
    

    # 5. Store & Brordcast  
    res = api.broadcast_and_store(att['trytes'])
    #pprint(res)


if __name__ == '__main__':
   my_send_transfer()
   


