""" 

Задача 1.  Дано двовимірний масив. 
У кожному його стовпці знайти: 
максимальний елемент (функція); 
мінімальний елемент (функція) 
і переставити їх місцями.

"""

def get_max_id(col_data):
    max_idx=0
    for i in range(1, len(col_data)):
        if col_data[i]>col_data[max_idx]:
            max_idx=i
    return max_idx

def get_min_id(col_data):
    min_idx=0
    for i in range(1, len(col_data)):
        if col_data[i]<col_data[min_idx]:
            min_idx=i
    return min_idx

def main():
    
    rows=2
    cols=2
    matrix=[]
    
    for i in range(rows):
        
        row = []

        for j in range(cols):
            value=float(input(f"Введіть елемент [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)

    print("Введена вами матриця:")

    for row in matrix:
        print(row)

    for j in range(cols):
        col_el = []
        for i in range(rows):
            col_el.append(matrix[i][j])

        max_id = get_max_id(col_el)
        min_id = get_min_id(col_el)
        
        print(f"Стовпець {j+1}: Max = {col_el[max_id]}, Min = {col_el[min_id]}")
        matrix[max_id][j], matrix[min_id][j] = matrix[min_id][j], matrix[max_id][j]

    print("Матриця після перестанови")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()


