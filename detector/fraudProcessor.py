def is_suspicious(transaction:dict)->bool:
    return transaction['amount']=>900