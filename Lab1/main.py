import math
import numpy as np


def cylinder_area(r: float, h: float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r > 0 and h > 0:
        return 2 * math.pi * r * (r + h)
    else:
        return np.NaN


def fib(n: int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    fibonacci_list = np.array([1, 1])
    if isinstance(n, int): #sprawdzenie czy n jest całkowity
        if n <= 0:
            return None
        if n == 1:
            return fibonacci_list[0]
        if n == 2:
            return fibonacci_list
        if n > 2:
            fibonacci_list = [1, 1]
            for i in range(n - 2):
                fibonacci_list = np.append(fibonacci_list, [fibonacci_list[-1] + fibonacci_list[-2]])
        return np.reshape(fibonacci_list, (1, n))


def matrix_calculations(a: float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    Mt = np.transpose(M) #transpozycja macierzy
    Mdet = np.linalg.det(M) #obliczenie wyznacznika, jesli det = 0 to macierz odwrotna nie istnieje
    if Mdet == 0:
        Minv = np.NaN
    else:
        Minv = np.linalg.inv(M)
        touple = (Minv, Mt, Mdet)
    return touple



def custom_matrix(m: int, n: int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if m < 0 or n < 0:
        return None

    if isinstance(m, int) and isinstance(n, int): #sprawdzenie czy m oraz n są liczbami całkowitymi
        matrix = np.zeros(shape=(m, n)) #inicjalizacja macierzy wypełnionej zerami
        for i in range(m):
            for j in range(n):
                if i > j:
                    matrix[i][j] = i
                else:
                    matrix[i][j] = j

        return matrix

    else:
        return None
