print('ip-tools cli')
print('')
print('1. melissa')
print('2. shodan (WIP)')
print('3. intelx (WIP)')
print('4. html-fetch (WIP)')
print('5. convert (WIP)')





print('')
selection = input("Enter module:\n>")

if selection == "1":
    exec(open("melissa.py").read())
if selection == "2":
    exec(open("shodan.py").read())
if selection == "3":
    exec(open("shodan.py").read())

else:
    print('Invalid input')