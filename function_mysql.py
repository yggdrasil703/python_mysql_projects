import mysql.connector as mysql

try:
    connection=mysql.connect(host="localhost",port="3306", user="root", password="admin#123", database="data_base")

#except mysql.Error as err:
    #print("mysql error:"+ str(err))

except Exception as ex:
    print("error: "+ str(ex))

cursor_ = connection.cursor()





###############################################################################################
###############################################################################################
###############################################################################################







def check_info():
    cursor_.execute("SELECT user_id,first_name,last_name,age FROM data_base.customer_table;")

    # for row in cursor_:
    # print(row)
    rows = cursor_.fetchall()
    for row in rows:
        print(row)

    connection.close()











###############################################################################################
###############################################################################################
###############################################################################################

def add_info():
    user_id = str(input("input the dedicated id \n"))
    user_first_name = input("input your first name \n")
    user_last_name = input("input your last name \n")
    user_age = str(input("input your age \n"))

    insert_info = (
        "INSERT INTO data_base.customer_table (`user_id`,`first_name`, `last_name`, `age`)"
        "VALUES (%s, %s, %s, %s)"
    )

    try:
        data = (str(user_id), str(user_first_name), str(user_last_name), str(user_age))
        cursor_.execute(insert_info, data)

        connection.commit()
        print("successfully commited")

    except:
        print("my code failed")
        connection.rollback()

    finally:
        print("______________")
        print("Data inserted")
        print("______________")









###############################################################################################
###############################################################################################
###############################################################################################







def delete_info():
    user_delete = str(input("input who do you want to delete, state their id \n"))
    print("user_delete", user_delete)

    print("deleting...")
    delete_info = "DELETE FROM data_base.customer_table WHERE user_id=" + user_delete
    print("deleteinfo", delete_info)
    try:

        cursor_.execute(delete_info)
        connection.commit()
        print("removal succesfull")

        print(cursor_.fetchall())

    except:
        print("my code failed")
        connection.rollback()

    finally:
        connection.close()





###############################################################################################
###############################################################################################
###############################################################################################







def update_info():
    user_update_choice = input("what do you want to update? \n").upper()
    print("Test1")

    if user_update_choice == "FN":
        print("test2")
        user_fn_update = input("input your new first name \n")
        user_fn_update2 = input("input your id \n")
        try:
            first_name_update = """UPDATE data_base.customer_table SET first_name =%s  WHERE user_id=%s"""

            print(first_name_update)

            tuple_1 = (user_fn_update, user_fn_update2)

            cursor_.execute(first_name_update, tuple_1)

            connection.commit()
            print("update succesfull")

        except:
            print("my code failed")
            connection.rollback()

        finally:
            connection.close()







###############################################################################################
###############################################################################################
###############################################################################################






if connection.is_connected() == True:
    print("connected")

    user_choice=input("do you want to add(a) or check(c) or delete(d) or update(u) your info? \n").lower()

    if user_choice=="c":
        check_info()


    elif user_choice=="a":
        add_info()

    elif user_choice=="d":
        delete_info()


    elif user_choice=="u":
        update_info()











