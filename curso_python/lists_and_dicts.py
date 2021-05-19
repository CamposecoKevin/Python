def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'Fistname': 'kevin', 'lastname':'Camposeco'}

    super_list =[
         {'Firstname': 'kevin', 'lastname':'Camposeco'},
         {'Firstname': 'Harli', 'lastname':'Montejo'},
         {'Firstname': 'Rubeli', 'lastname':'Taracena'},
         {'Firstname': 'Monica', 'lastname':'Cartagena'},
         {'Firstname': 'Maria', 'lastname':'Montejo'},

    ]

    super_dict ={

         'natural_nums': [1,2,3,4,5],
          'integer_nums': [-1,-2,0,1,2],
          'floating_nums': [1.1,2.2,3.3,4.5]

    }

    #Para imprimir super_dict
    # for key, value in super_dict.items():
    #     print(key, '-',value)

    #para imprimir super_list
    for item in super_list:
        print(item["Firstname"] , "-" , item["lastname"])


if __name__=='__main__':
    run()