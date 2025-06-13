# Docstrings 

def example_func(param1, param2):
    # python の場合、関数の説明は以下のように、関数の中に書く。
    """Example function with types documented in the docstring. <- function の中身はどんなものなのかの説明
    
    Args: <- 引数がどんなものかの説明
        param1 (int): The first parameter.
        param2 (str): The second parameter.
        
        Returns: <- function が返すもの
            bool: The return value. True for success, False otherwise.
    
    """
    print(param1)
    print(param1)
    return True

print(example_func.__doc__) # 関数内に書いたドキュメントの内容が出力される
help(example_func) # これでも関数内に書いたドキュメントの内容が出力される