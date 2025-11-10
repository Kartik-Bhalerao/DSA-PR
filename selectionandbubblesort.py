def selection_sort(customer_id): 

    n = len(customer_id)-1 

    for i in range(n): 

        min_index = i 

        for j in range(i+1,n+1): 

            if customer_id[j]<customer_id[min_index]: 

                min_index = j 

        customer_id[i], customer_id[min_index] = customer_id[min_index], customer_id[i] 

    print("Sorted customer IDs:", customer_id) 

customer_id = [9,8,7,6,5,4,3,2,1] 

selection_sort(customer_id) 

 

BUBBLESORT=() 

 

def bubble_sort(salaries): 

    n =len(salaries) 

    for i in range(n): 

        for j in range(n-1-i): 

            if salaries[j]>salaries[j+1]: 

                salaries[j],salaries[j+1]=salaries[j+1],salaries[j] 

    print("Sorted salaries:",salaries) 

salaries=[55000,41000,66000,3000] 

bubble_sort(salaries) 

 
 

 
