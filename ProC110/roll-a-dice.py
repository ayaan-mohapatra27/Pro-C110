import random as r
response = "y"

while response == "y":
    num=r.randint(1,6)
    if(num==1):
        print("[     ]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[     ]")
        response=input("Would You Like To Continue? If so, Press 'y', Otherwise, Press 'n': ")
    if(num==2):
        print("[0    ]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[    0]")
        response=input("Would You Like To Continue? If so, Press 'y', Otherwise, Press 'n': ")
    if(num==3):
        print("[    0]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[0    ]")
        response=input("Would You Like To Continue? If so, Press 'y', Otherwise, Press 'n': ")
    if(num==4):
        print("[0   0]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[0   0]")
        response=input("Would You Like To Continue? If so, Press 'y', Otherwise, Press 'n': ")
    if(num==5):
        print("[0   0]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[0   0]")
        response=input("Would You Like To Continue? If so, Press 'y', Otherwise, Press 'n': ")
    if(num==6):
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        response=input("Would You Like To Continue? If so, Press 'y', Otherwise, Press 'n': ")