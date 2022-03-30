print('ip-tools cli')
print('')
print('1. melissa')
print('2. HTML-fetch (WIP)')
print('3. shodan (WIP)')
print('4. intelx (WIP)')
print('5. convert (WIP)')
print('6. ip-lookup')
print('7. ip-lookup')
print('8. ip-lookup')





print('')
selection = input("Enter module:\n>")

if selection == "1":
    exec(open("melissa.py").read())

else:
    print('Invalid input')