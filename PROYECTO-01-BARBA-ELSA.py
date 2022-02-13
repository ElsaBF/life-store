# Import the users list and the lists from lifestore_file
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
                
            else:
                print("Access denied")
                msg = "Incorrect password"
                break
    print(msg)
    # The user can access to the next function only if the login is correct
    if msg == "The user " + user + " successfully logged in":
        main()
    
def init_values():
    # Taking the id_product column from lifestore_sales list
    sales_list = []
    for s in lifestore_sales:
        sale = s[1]
        sales_list.append(sale)

    # Taking the id_product column from lifestore_searches list
    searches_list = []
    for s in lifestore_searches:
        search = s[1]
        searches_list.append(search)
    
    # Creating a dictionary {id_product: [name_product, product_price]}
    products_list = {}
    for e in lifestore_products:
        id_product = e[0]
        name_product = e[1]
        product_price = e[2]
        products_list[id_product] = [name_product, product_price]
    

    # Creating nested dictionaries for the categories {'category': {id_product: 0}}
    results_per_item = {}
    category_dict = {}
    for p in lifestore_products:
        id_product = p[0]
        category = p[3]
        results_per_item[id_product] = 0
        if category not in category_dict:
            category_dict[category] = {}
            category_dict[category][id_product] = 0
        else:
            category_dict[category][id_product] = 0

    return sales_list, searches_list, products_list, results_per_item, category_dict
    
#------ In this function you decide wich data display
def main():
    # Initializing the values of the init_values function
    sales_list, searches_list, products_list, results_per_item, category_dict = init_values()
    
    # Uncoment the name of the function that you want to run
    
    sales(sales_list)
    #searches(searches_list)
    #sales_2(searches_list,  products_list, results_per_item, category_dict)
    #searches_2(searches_list, products_list, results_per_item, category_dict)
    #score(products_list)
    #statistics(sales_list, products_list)
    


#------ Define a function for the most sold products ------
def sales(sales_list):
    # Creating a dictionary with the id_products and the number of sales {id_product: times sold}
    sales_dic = {}
    for i in sales_list:
        if i in sales_dic:
            sales_dic[i] = sales_dic[i] + 1
        else:
            sales_dic[i] = 1

    # Sorting the dictionary sales from smallest to largest
    sales_dic_sorted = dict(sorted(sales_dic.items(), key= lambda x:x[1]))
    
    # Obtaining only the five most selled products
    most_selled = []
    i = 0
    for element in reversed(sales_dic_sorted):
        if i == 5:
            break
        else:
            most_selled.append(element)
            i += 1
    
    # Matching the id_product with the name of the product 
    final_most_selled = []
    for m in most_selled:
        for p in lifestore_products:
            if m == p[0]:
                final_most_selled.append(p[1])
    
    print("The five most selled products are: ")
    print(*final_most_selled, sep='\n')

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

#------ Define another function for sales ------
def sales_2(sales_list, products_list, results_per_item, category_dict):
    # Saving the quantity of sales in the results_per_item dictionary
    for s in sales_list:
        results_per_item[s] = results_per_item[s] + 1
    
    # Filling the category_dict with the data in results_per_item
    for e in category_dict.items():
        category_label = e[0]
        category_dict_int = e[1]
        for v in category_dict_int.items():
            key = v[0]
            category_dict_int[key] = results_per_item[key]    
        # Sorting from mayor to minor the intern dictionary
        category_dict_int = dict(sorted(category_dict_int.items(), key= lambda x:x[1]))
        
        # Displaying the data 
        i = 0
        print("Categoria: " + category_label)
        for v in category_dict_int.items():
            if i == 5:
                break
            id_product = v[0]
            r_per_item = v[1]
            print(f"'{products_list[id_product][0][:20]}...' has been bought {r_per_item} times")
            i += 1

#------ Define a function for the lower searches
# This funtion is similar to sales_2 but displays de lower searches per category
def searches_2(searches_list, products_list, results_per_item, category_dict):
    for s in searches_list:
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

        # Displaying the results
        i = 0
        print("Categoria: " + category_label)
        for v in category_dict_int.items():
            if i == 10:
                break
            id_product = v[0]
            r_per_item = v[1]
            print(f"'{products_list[id_product][0][:20]}...' has been searched {r_per_item} times")
            i += 1
            
###------ Defining a funtion to ranking products ------
def score(products_list):
    # Creating a dictionary {id_product: [scores]}
    avg_item_score = {}
    for e in lifestore_sales:
        id_product = e[1]
        score = e[2]
        isRefound = e[-1]
        if id_product not in avg_item_score:
            avg_item_score[id_product] = [score]
        else:
            avg_item_score[id_product].append(score) 
    
    # Getting a list [id_product, average_score]
    result = []
    for e in avg_item_score.items():
        id_product = e[0]
        internal_value = e[1]
        avg = sum(internal_value) / len(internal_value)
        result.append([id_product, avg])
    result = sorted(result, key=lambda x: x[1])
    print(result)
    
    # Displaying the results
    print("----- Best ranked -----")
    for i in range(0, 5):
        id_product = result[-i-1][0]
        score = result[-i-1][1]
        print(f"'{products_list[id_product][0][:20]}...' has a score of {score}")
    
    print("----- Worst ranked -----")
    for i in range(0, 5):
        id_product = result[i][0]
        score = result[i][1]
        print(f"'{products_list[id_product][0][:20]}...' has a score of {score}")
    
#------ Defining a fungtion for the sales and incomes statistics ------
def statistics(sales_list, products_list):
    # Total incomes per year
    sales_dic = {}
    for e in sales_list:
        if e in sales_dic:
            sales_dic[e] = sales_dic[e] + products_list[e][1]
        else:
            sales_dic[e] = products_list[e][1]

    incomes_per_year = sum(list(sales_dic.values()))
    
    # Total sales per year
    print("The total incomes for the 2020' sales are: ", incomes_per_year)
    print("The total number of sales for the 2020 are: ", len(sales_list))
    
    # Sales and incomes per month
    sales_per_month     = [0,0,0,0,0,0,0,0,0,0,0,0]
    incomes_per_month   = [0,0,0,0,0,0,0,0,0,0,0,0]
    for e in lifestore_sales:
        id_product = e[1]
        month = int(e[3][3:-5]) - 1 #dd/mm/yyyy
        year = int(e[3][6:]) #[dd/mm/]-> yyyy
        if year != 2020:
            continue        # Skip all the following lines 
        sales_per_month[month] += 1
        incomes_per_month[month] += products_list[id_product][1]
    
    i = 1
    print("----- Sales per month -----")
    for e in sales_per_month:
            print(f"In the month {i} there was a total of {e} sales")
            i = i + 1
    
    j = 1
    print("----- Incomes per month -----")
    for e in incomes_per_month:
        print(f"In the month {j} there was a total income of {e}")
        j = j + 1
    
if __name__ == "__main__":
    login()