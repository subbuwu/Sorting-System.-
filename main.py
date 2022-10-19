import random as ra 

  

import mysql.connector as mc 

  

while True: 

    print('**************************************************************************************************************') 

    print('                                       Welcome To The Examinee Place Alotter') 

    print('**************************************************************************************************************') 

    print('Select  "1" to know whats this program about') 

    print('Select "2" to sort the students') 

    print('Select "3" to Exit') 

    ch=int(input('Enter your choice')) 

    if ch==1: 

        print('The motto of this project is to sort the students of various categories writing an exam obtained from a given\ data considering the classroom as a rectangular array so that student of similar categories doesnt sit together') 

    if ch==2: 

        print('Provide your sql data to fetch the students data from') 

        print('') 

        print('Note:The given sql data should be in the format of',sep=':') 

        print('[roll number,student name,student exam category]') 

        i_user = input('enter your username') 

        i_password=input('enter your password') 

        i_database = input('enter your database') 

        table_name = input('enter the table name') 

        co = mc.connect(host='localhost', user=i_user,password=i_password, database=i_database) 

        cu = co.cursor() 

        cu.execute(f"select * from {table_name}") 

        sql_lst = cu.fetchall() 

        while True: 

            r = int(input("enter the number of rows")) 

            c = int(input('enter the number of coloumns')) 

            if c > 0 and r > 0: 

                break 

            else: 

                print("Try again the entered dimensions are not valied") 

  

        def create_table(m, n):  # m= no of rowss, n=no of coloumns 

            l = [] 

            for i in range(m):  # 3(0,1,2) 

                z = [] 

                for j in range(n):  # 2 (0,1) l=[[0,0],[0,0],[0,0]] 

                    z.append(0) 

                l.append(z) 

            return l 

  

        def print_board(board, l=1): 

            print('[',) 

            for i in range(len(board)): 

                for j in range(len(board[0])): 

                    #print([board[i][j], len([board[i][j]]), l]) 

                    if len(board[i][j]) < l: 

                        a = board[i][j]+' '*(l-len(board[i][j])) 

                    elif len(board[i][j]) == l: 

                        a = board[i][j] 

                    print(a, end=' | ') 

                print('') 

  

        def print_coordinateboard(board): 

            for i in range(len(board)): 

                for j in range(len(board[0])): 

                    print((i, j), end='|') 

                print('') 

  

        def find_empty(board, l=None): 

            for i in range(len(board)): 

                for j in range(len(board[0])): 

                    if board[i][j] == 0 and l == None: 

                        return i, j 

  

        def segregation(a): 

            category = [] 

            number_category = [] 

            for j in a: 

                if j[2] not in category: 

                    category.append(j[2]) 

                    number_category.append(category.index(j[2])+1) 

                 

  

            namelist = [] 

            for j in category: 

                l1 = [] 

                for i in a: 

                    if i[2] == j: 

                        l1.append(i[1]) 

                namelist.append(l1) 

            return namelist, number_category, category 

  

        def dist_list(a): 

            l=[] 

            for i in a: 

                if i not in l: 

                    l.append(i) 

            return l            

  

  

        def check(num, row, col, b): 

            if True: 

                if col+1 != len(b[0]) and col-1 != -1: 

                    if b[row][col+1] == num or b[row][col-1] == num: 

                        return False 

                elif col+1 == len(b[0]): 

                    if b[row][col-1] == num: 

                        return False 

                elif col-1 == -1: 

                    if b[row][col+1] == num: 

                        return False 

            if True: 

                if row+1 != len(b) and row-1 != -1: 

                    if b[row-1][col] == num or b[row+1][col] == num: 

                        return False 

                elif row+1 == len(b): 

                    if b[row-1][col] == num: 

                        return False 

                elif row-1 == -1: 

                    if b[row+1][col] == num: 

                        return False 

            return True 

  

        def limit(m,n): 

            if m%2!=0: 

                a=(m/2+0.5) 

            if m%2==0: 

                a=(m/2) 

            if n%2!=0: 

                b=(n/2+0.5) 

            if n%2==0: 

                b=(n/2) 

            #finding max value 

            if r%2==0 and c%2==0: 

                maximum=a*b+a*b 

            if r%2==0 and c%2!=0: 

                maximum=a*b+a*(b-1) 

            if r%2!=0 and c%2==0: 

                maximum=a*b+(a-1)*b 

            if r%2!=0 and c%2!=0: 

                maximum=a*b+(a-1)*(b-1) 

            return int(maximum) 

        lim=limit(r,c)        

  

        def elemental_list():  # [3,2,1] ---->[1,1,1,2,2,3] 

            el = [] 

            dict = {} 

            for i in range(len(fetch_lst)): 

                dict[b[i]] = fetch_lst[i] 

            a = sorted(dict.items(), key=lambda x: x[1], reverse=True) 

            for i in a: 

                el = el+[i[0]]*i[1] 

            #print(el) 

            #print(dict) 

            return el 

  

        tlist = [] 

        initial_cu = [0, 0] 

        BOARD = create_table(r, c) 

        a, b, ca = segregation(sql_lst) 

        lim = limit(r, c) 

  

        def fetchlist(): 

            fetch_lst=[] 

            while True: 

                print('Hey there enter the number of records from each category needed to be fetched,\ the maximum number of students that can be fetched for a particular category in' ,len(b),'categories for the given table ', r,'*',c,'is', lim) 

                print('') 

                for i in ca: 

                    while True: 

                        print('enter the number of students needed to be fetched for ',i.upper(),'category ') 

                        print('Note:The remaining number of entries are',r*c-sum(fetch_lst),'Max limit=',lim) 

                        print('') 

                        inp=int(input('enter')) 

                        cnt=0 

                        while True: 

                            if inp>lim: 

                                print('enter again as number student exceeded the max limit ') 

                                break 

                            if  sum(fetch_lst)+inp>r*c: 

                                print('enter last value again as enterd value is greater than seat limit') 

                                break 

                            if inp>len(a[ca.index(i)]): 

                                print('Enter again as number of student in this category exceeded the record limit' ) 

                            else: 

                                fetch_lst.append(inp) 

                                cnt=1 

                                break 

                        if cnt==1: 

                            break 

                break 

            return fetch_lst        

  

        def solve(board):  # (BOARD) 

            #find=find_empty(board) 

            #print_board(board) 

            #print('Elelist',ele_list) 

            #print('TLSIT',tlist) 

            if not ele_list: 

                #print('first ret') 

                return True  # To validate the if condition 

            else: 

                if len(ele_list)+len(tlist) == r*c: 

                    R, C = find_empty(board) 

                    for i in dist_list(ele_list):  # [1,2,3,4,5] 

                        if check(i, R, C, board): 

                            board[R][C] = i 

                            a = ele_list.pop(ele_list.index(i)) 

                            tlist.append(a) 

  

                            if solve(board): 

                                #print('2nd ret') 

                                return board 

                            else: 

                                board[R][C] = 0 

                                ele_list.append(tlist.pop()) 

                                #print('ELELIST',ele_list) 

                else: 

                    if find_empty(board) == None and len(ele_list) >= 1: 

                        return False 

                    else: 

                        R, C = find_empty(board) 

                        #print(R,C) 

                        for i in dist_list(ele_list):  # [1,2,3,4,5] 

                            # and ((R+1==r and C+1==c and len(ele_list)==1) or (R+1!=r or C+1!=c)): 

                            if check(i, R, C, board): 

                                #print('h1') 

                                board[R][C] = i 

                                a = ele_list.pop(ele_list.index(i)) 

                                tlist.append(a) 

  

                                if solve(board): 

                                    #print('2nd ret') 

                                    return board 

                                else:  # backtracking 

                                    board[R][C] = 0 

                                    ele_list.append(tlist.pop()) 

                                    #print('ELELIST',ele_list) 

  

                        for i in dist_list(ele_list): 

                            if C+1 == c: 

                                R1 = R+1 

                                C1 = 0 

                            if C+1 != c: 

                                R1 = R 

                                C1 = C+1 

                            if (R+1 != r or C+1 != c) and check(i, R1, C1, board) and len(dist_list(ele_list)) == 1: 

                                #print('hi2',i) 

                                board[R1][C1] = i 

                                a = ele_list.pop(ele_list.index(i)) 

                                tlist.append(a) 

                                board[R][C] = 'EMPTY' 

                                if solve(board): 

                                    #print('2nd ret') 

                                    return board 

                                else:  # backtracking 

                                    board[R][C] = 0 

                                    board[R1][C1] = 0 

                                    ele_list.append(tlist.pop()) 

                                    #print('ELELIST',ele_list) 

            return False 

  

        fetch_lst =fetchlist() 

        ele_list = elemental_list() 

        len_ca = len(ca) 

        #print_board(BOARD) 

        solved_board = solve(BOARD) 

        print('This is just the coordinates of each table for referential purpose') 

        print_coordinateboard(solved_board) 

         

        while True: 

            ans=int(input('1)do you want to autofill students or 2)customfill,choice=1or2:')) 

            if ans==1 or ans==2: 

                break 

            else: 

                print('enterd choice doesnt excist try again') 

         

        t_table = [] 

        sql_op_lst=[] 

        added_names=[] 

        max = 0 

        for i in range(len(solved_board)): 

            l = [] 

            for j in range(len(solved_board[0])): 

                if solved_board[i][j] != 'EMPTY' and solved_board[i][j] != 0: 

                    if ans==1: 

                        element = ra.choice(a[solved_board[i][j]-1]) 

                        added_names.append(a[solved_board[i][j]-1].pop(a[solved_board[i][j]-1].index(element))) 

                    if ans==2: 

                        while True: 

                            print('enter the student to be seated in coordinate',i+1,',',j+1) 

                            print('') 

                            print('available students are in the given coordinates are' ) 

                            print('') 

                            print(a[solved_board[i][j]-1]) 

                            print('NOTE:please be careful to not enter duplicate student entry') 

                            print('') 

                            element=input('enter') 

                            if element not in a[solved_board[i][j]-1] : 

                                print('enter again as enterd student name does not excist or cant be seated in the given place') 

                            else: 

                                added_names.append(a[solved_board[i][j]-1].pop(a[solved_board[i][j]-1].index(element))) 

                                break                

                    if len(element) > max: 

                        max = len(element) 

                    for k in sql_lst: 

                        if k[1]==element: 

                            sno=k[0] 

                    sql_op_lst.append([sno,element, ca[solved_board[i][j]-1], i+1, j+1]) 

                else: 

                    element = 'EMPTY' 

                    sql_op_lst.append(['EMPTY',element, 'EMPTY', i+1, j+1]) 

  

                l.append(element) 

            t_table.append(l) 

        print('Here comes the graphical representation of sorted classroom') 

        print_board(t_table, max) 

        ''' 

        cu.execute("create table finaltable (admissionno varchar(20),studentname varchar(20),category varchar(20),rownumber int,coloumnnumber int,primary key(rownumber,coloumnnumber));") 

        ''' 

        for i in sql_op_lst: 

            cu.execute(f"insert into finaltable values('{i[0]}','{i[1]}','{i[2]}',{i[3]},{i[4]})") 

            co.commit() 

        print('Successfully updated the final record in your sql table') 

    if ch==3: 

        break 

  

         

     

#print('') 

  

#swapping 

  

  

''' 

nl1=[] 

nl2=[] 

while True: 

    for i in solved_board: 

        for j in i: 

            nl1.append(j) 

        a=nl1.sort() 

    for k in b: 

        nl2.append(nl1.count(k)) 

    if nl2==fetch_lst: 

        print('test passed') 

        break 

    else: 

        print('test failed',nl2) 

        break 

print(fetch_lst) 

print(ele_list) 

''' 

''' 

if  len(fetch_lst)==len(ca)-1: 

                        print(' remaining item',r*c-sum(fetch_lst),'is considerd for category',i) 

                        fetch_lst.append(r*c-sum(fetch_lst)) 

                        break 

''' 
