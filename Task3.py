# Task3
# Example: ("QWE",1.1,234),2,(None,7),0,2,(7,7,7),2,(12,),(),3,(5,6),3,100500

main_sequence = []
for elem in eval(input()):
    if type(elem) is tuple:
        main_sequence += elem
    else:
        if elem > len(main_sequence):
            break
        print(main_sequence[:elem])
        main_t = main_sequence[elem:]
