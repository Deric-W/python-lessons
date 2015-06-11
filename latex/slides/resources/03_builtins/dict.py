d = { 'm': 4, 3: 'val2', object: 'auch typen können schlüssel sein' }

d[3]  # ==> "val2"
d['q']  # ==> KeyError: 'q'
d.get('q')  # ==> None
d.get('q', 5)  # ==> 5

d[0] = 7
d  # ==> {3: 'val2', 'm': 4, 'q': 5, <class 'object'>: 'auch typen können schlüssel sein'}

d.setdefault('m')  # ==> 4
d.setdefault('q', 5)  # ==> 5
d  # ==> { 'm': 4, 3: 'val2', object: 'auch typen können schlüssel sein', 0:7, 'q': 5 }
len(d)  # ==> 5
d.keys()  # ==> dict_keys([3, 0, 'm', 'q', <class 'object'>])
d.values()  # ==> dict_values(['val2', 7, 4, 5, 'auch typen können schlüssel sein'])
d.items()  # ==> dict_items([(3, 'val2'), (0, 7), ('m', 4), ('q', 5), (<class 'object'>, 'auch typen können schlüssel sein')])

'm' in d  # ==> True
object in d  # ==> True
tuple in d  # ==> False