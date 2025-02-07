def safe_calculator(func):
    def wrapper(expression):
        try:
            if any(c not in "0123456789+-*/(). " for c in expression):
                raise ValueError("Незрозумилі символи")

            result = func(expression)
            return result
        except ZeroDivisionError:
            return "Ділення на нуль неможливе"
        except SyntaxError:
            return "Синтаксична помилка у виразі!"
        except ValueError as e:
            return f"Помилка: {e}"

    return wrapper


@safe_calculator
def calculate(expression):
    return eval(expression)


print(calculate("10 + 5"))
print(calculate("3 / 3"))
print(calculate("10 + b"))
print(calculate("10 + 1.45"))
