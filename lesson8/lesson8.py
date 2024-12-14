from streamlit import exception

text = "this is not a number"

try:
    text_to_int = int(text)

except Exception as e:
    print("an error accured while parsing the data", e)


    try:
        result = 10/ 2

    except ZeroDivisionError:
        print("this division is accured to deviding by 2")

    else:
        print("fegegregrreg", result )


try:
    result = 10/ 2

except ZeroDivisionError:
    print("an error accured while parsing the data")

finally:
    print("finally this finally")
















































