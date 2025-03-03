true_operator = {"+", "-", "*", "/"}

running = True
while running:
    while True:
        try:
            x = float(input("数字を入力してください。\n>>> "))
            break

        except ValueError:
            print("数値以外が入力されました。")

    while True:
        operator = input("演算子(+, -, *, /)を入力してください。\n>>> ")
        if operator in true_operator:
            break
        print("+, -, *, /以外が入力されました。")

    while True:
        try:
            y = float(input("数字を入力してください。\n>>> "))
            break

        except ValueError:
            print("数値以外が入力されました。")

    result = {"+": x + y,
              "-": x - y,
              "*": x * y,
              "/": x / y if y != 0 else "0では割れません。"}[operator]

    print(result)

    condition = input("続けますか？(Yes か No で答えてください)\n>>> ")
    if condition.lower() == "yes":
        print("計算を続けます。")

    else:
        print("終了します。")
        running = False
