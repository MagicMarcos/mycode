#!/usr/bin/env python3

def main():
    Deadpool={
            'Real Name':'Wade Winston Wilson',
            'First Appearance':'New Mutants (Vol. 1) #98 (February, 1991)',
            'Creators':[
                'Fabian Nicieza',
                'Rob Liefeld'
                ],
            'Base of Operations':'Nomadic',
            'Paraphernalia':[
                'Knives',
                'Guns'
                ]
            }
    name = Deadpool["Real Name"]
    firstappearance = Deadpool["First Appearance"]
    creators = Deadpool["Creators"]
    base = Deadpool["Base of Operations"]
    weapons = Deadpool["Paraphernalia"]

    print(f"Deadpool aka {name}, first appeared in {firstappearance}. Creators include {creators[0]} and {creators[1]}. He has no base of operations as he is {base}, and he loves using {weapons[0]} and {weapons[1]}.")

main()
