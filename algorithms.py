# import google.generativeai as genai

# # Настройка API-ключа
# genai.configure(api_key="AIzaSyBAecsSQfAxeQDChXVKMYJ1QFOvH223oTo")  

# # Создание модели
# model = genai.GenerativeModel("gemini-2.5-flash")

# # Генерация текста
# response = model.generate_content("Напиши код который будет выводить 'Hello, World!' в Python.")
# print(response.text)






# def bin_search(arr, item):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#         if guess == item:
#             return 'Item index:', mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return False

# a = [1, 2, 4, 5, 7, 8, 9]
# a_bin = bin_search(a, 7)
# if a_bin == False:
#     print('Array not have item')
# else:
#     print(*a_bin)





# def rec_bin_search(arr, item, low=0, high=None):
#     if high is None:
#         high = len(arr) - 1
    
#     # Базовый случай: элемент не найден
#     if low > high:
#         return False
    
#     mid = (low + high) // 2
#     guess = arr[mid]
    
#     # Базовый случай: элемент найден
#     if guess == item:
#         return 'Item index:', mid
#     # Рекурсивные случаи
#     elif guess > item:
#         return rec_bin_search(arr, item, low, mid - 1)
#     else:
#         return rec_bin_search(arr, item, mid + 1, high)

# a = [1, 2, 4, 5, 7, 8, 9]
# a_bin = rec_bin_search(a, 7)
# if a_bin == False:
#     print('Array not have item')
# else:
#     print(*a_bin)




# def bubbleSort(array):

#     for i in range(len(array)):
#         for j in range(0, len(array) - i - 1):
#             if array[j] > array[j + 1]:

#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp


# data = [-2, 45, 0, 11, -9]

# bubbleSort(data)

# print('Sorted Array in Ascending Order:')
# print(data)
