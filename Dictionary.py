world = {"IND":
        {"MAH":["c1", "c2", "c3"],
        "MP":["c4","c5","c6"],
        "UP":["c7","c8","c9"]

        },
        "USA":
        {"st1":["c1","c2","c3"],
        "st2":["c4","c5","c6"],
        "st3":["c7","c8","c9"]

        }
    }
for countryName, state in world.items():
    print(countryName)
    print(state)
    print ("############")
    for st, players in state.items():
        print(st+"\'s player is "+players[0])
        print("################")
        print(st+"\'s player are ")
        for pt in players:
            print(pt)
#        print(players[0])
