# аба́
def find_form(x):
    with open('slovar_new.txt', 'r', encoding = 'utf-8') as sl:
        sl = sl.read().split('\n')
    for st in sl:
        if x in st:
            print()
            if ' — ' in st:
                print(st.split(' — ')[0])
                opr = st.split(' — ')[1]
            else:
                print(st.split(' ')[0])
                opr = ''
                for i in st.split(' ')[0::]:
                    opr += str(i) + " "
            print(opr.split(';')[0])
            if len(opr.split(';'))>1:
                print(opr.split(';')[1])
            if len(opr.split(';'))>2:
                print(opr.split(';')[2])
            if len(opr.split(';'))>3:
                print(opr.split(';')[3])
            if len(opr.split(';')) > 4:
                print(opr.split(';')[4])
            if len(opr.split(';'))>5:
                print(opr.split(';')[5])
            if len(opr.split(';'))>5:
                print(opr.split(';')[5])
                return
find_form(input())