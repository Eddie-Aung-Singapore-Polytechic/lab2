def main():
    print("DevOps for AIoT (ET0735) ~ Lab 2 ~ Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average(num_list)
    print("Average of the values:", average)
    min_max = find_min_max(num_list)
    print("Minimum number:",min_max[0],"\nMaximum Number:",min_max[1])
    median = calc_median_temperature(num_list)
    print("And the median is:", median)
    
    return 0

def display_main_menu():
      print("Enter some numbers separated by commas (e.g. 5, 67, 32")
      
      return 0

def get_user_input():
      input_text = input("Enter: ")
      numbers = input_text.split(",") #Splits the input text into a list of strings
      numbers_float = []
      for i in numbers:
        numbers_float.append(float(i))
      
      return numbers_float

def calc_average(de_list):
      sum_of_values = 0
      for i in de_list:
           sum_of_values += i
    
      return sum_of_values
    
def find_min_max(de_other_list):
      biggest_num = 0
      smallest_num = 0
      for i in de_other_list:
            if biggest_num < i :
                  biggest_num = i 
            if smallest_num > i :
                  smallest_num = i
      
      return smallest_num,biggest_num

def sort_temperature(temp_list):
      temp_list.sort()
      return temp_list

# By seeing whether it is even or odd and then applying the median formula to the sorted list 
def calc_median_temperature(list_to_calculate):
      sorted_list = []
      sorted_list = sort_temperature(list_to_calculate)
      length_of_list = len(sorted_list)
      if (length_of_list % 2) == 0:
            median = sorted_list[int((length_of_list+1)/2)]          
      else:
            first_middle_value = sorted_list[int((length_of_list+1)/2)]
            second_middle_value = sorted_list[int(length_of_list/2)] 
            median = (first_middle_value + second_middle_value) /2   
    
      return median

if __name__ == "__main__":
        main()
