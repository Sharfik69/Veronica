import sqlite3

def but():
    global conn
    conn = sqlite3.connect("test_data_base.db")
    global cursor
    cursor = conn.cursor()
    list_of_list = []
    list_of_list1 = []
    for i in cursor.execute("""select table_number from new_table_orders where state = 1 order by table_number"""):
        change = str(i[0])
        list_of_list1.append(change)
        if len(list_of_list1) == 3:
            list_of_list.append(list_of_list1)
            list_of_list1=[]        
    if len(list_of_list1) > 0:
        list_of_list.append(list_of_list1)
    list_of_list.append(['Назад'])
    return list_of_list
   
