import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 625983402 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    max = x.max()  
    return (max - ((max - 0.038) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))),
            max + ((max - 0.038) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))))
