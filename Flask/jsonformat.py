def obj2dict(obj):
    if not hasattr(obj,'__dict__'):
        return obj
    res = {}
    for k,v in obj.__dict__.items():
        if k.startswith('-'):
            continue
        if isinstance(v,list):
            ele = [obj2dict(item) for item in v]
        else:
            ele = obj2dict(v)
        res[k] = ele
    return res