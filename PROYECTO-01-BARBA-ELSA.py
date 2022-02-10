# Import the users list and the lists from lifestore_file
from re import search
from users import users_list
from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products

#------ Define a function for the login ------
def login():
    # Displayng a welcome message
    welcome_message = "Welcome, please enter your username and your password."
    print(welcome_message)
    # Request username and password
    user = input("Escriba el nombre de usuario: ")
    password = input("Escriba la contraseña: ")
    # This message is displayed if the user is unregistered
    msg = "Unregistered user"

    for u in users_list:
        # Verifying if the user exist in the list
        if user == u[1]:
            # Verifying if the password exist and match with the user
            if password == u[2]:
                print("Access granted")
                msg = "The user " + user + " successfully logged in"
                # The user can access to the next function only if le login is correct
                sales()
            else:
                print("Access denied")
                msg = "Incorrect password"
                break
    print(msg)

def init_values():
    # Taking the id_product column from lifestore_sales list
    sales_list = []
    for s in lifestore_sales:
        sale = s[1]
        sales_list.append(sale)

    searches_list = []
    for s in lifestore_searches:
        search = s[1]
        searches_list.append(search)
    
    products_list = {}
    for e in lifestore_products:
        id_product = e[0]
        name_product = e[1]
        products_list[id_product] = name_product

    return sales_list, searches_list, products_list
    

def main():
    sales_list, searches_list, products_list = init_values()
    sales_2(sales_list, products_list)


#------ Define a function for the sales ------
def sales():
    # Taking the id_product column from lifestore_sales list
    sales_list = []
    for s in lifestore_sales:
        sale = s[1]
        sales_list.append(sale)

    # Creating a dictionary with the id_products and the number of sales
    sales_dic = {}
    for i in sales_list:
        if i in sales_dic:
            sales_dic[i] = sales_dic[i] + 1
        else:
            sales_dic[i] = 1

    # Sorting the dictionary sales from smallest to largest
    sales_dic_sorted = dict(sorted(sales_dic.items(), key= lambda x:x[1]))
    
    # Obtaining the five most selled products
    most_selled = []
    i = 0
    for element in reversed(sales_dic_sorted):
        if i == 5:
            break
        else:
            most_selled.append(element)
            i += 1
    

    final_most_selled = []
    for m in most_selled:
        for p in lifestore_products:
            if m == p[0]:
                final_most_selled.append(p[1])
    
    print("The five most selled products are: ")
    print(*final_most_selled, sep='\n')
    searches()

#------ Define a function for the searches ------
### This section is pretty much like the sales function but using the lifestore_searches list
def searches(searches_list):
    searches_dic = {}
    for i in searches_list:
        if i in searches_dic:
            searches_dic[i] = searches_dic[i] + 1
        else:
            searches_dic[i] = 1
 
    searches_dic_sorted = dict(sorted(searches_dic.items(), key= lambda x:x[1]))
    
    most_searched = []
    i = 0
    for element in reversed(searches_dic_sorted):
        if i == 10:
            break
        else:
            most_searched.append(element)
            i += 1

    final_most_searched = []
    for m in most_searched:
        for p in lifestore_products:
            if m == p[0]:
                final_most_searched.append(p[1])
    
    print("The ten most searched products are: ")
    print(*final_most_searched, sep='\n')

#------ Define another function for sales
def sales_2(sales_list, products_list):
    results_per_item = {}
    category_dict = {}

    # Creating nested dictionaries for the categories
    for p in lifestore_products:
        id_product = p[0]
        category = p[3]
        results_per_item[id_product] = 0
        if category not in category_dict:
            category_dict[category] = {}
            category_dict[category][id_product] = 0
        else:
            category_dict[category][id_product] = 0
    
    for s in sales_list:
        results_per_item[s] = results_per_item[s] + 1
    
    # Connecting the number of sales dictionary with the category dictionary
    #result = {}
    for e in category_dict.items():
        category_label = e[0]
        category_dict_int = e[1]
        for v in category_dict_int.items():
            key = v[0]
            category_dict_int[key] = results_per_item[key]
        # Sorting from mayor to minor the intern dictionary
        category_dict_int = dict(sorted(category_dict_int.items(), key= lambda x:x[1]))
        # Set new values for final dictionary that contains the sorted data
        #result[category_label] = category_dict_int

        ####
        i = 0
        print("Categoria: " + category_label)
        for v in category_dict_int.items():
            if i == 5:
                break
            id_product = v[0]
            r_per_item = v[1]
            print(f"'{products_list[id_product][:20]}...' has been bought {r_per_item} times")
            i += 1
    #print(result)

if __name__ == "__main__":
    main()