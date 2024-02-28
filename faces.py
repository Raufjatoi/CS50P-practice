face = input('Enter felling and emoticons like :) and :( : ')
if ':)' in face :
    print(face.replace(':)', '🙂'))
elif ':(' in face :
    print(face.replace(':(','🙁'))
else:
    print(face)