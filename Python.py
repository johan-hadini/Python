
‏import itertools
‏import string

‏def crack_password(password):
‏    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
‏    attempts = 0
‏    for length in range(1, len(password)+1):
‏        for guess in itertools.product(chars, repeat=length):
‏            attempt = ''.join(guess)
‏            attempts += 1
‏            if attempt == password:
‏                return attempt, attempts
‏    return None, attempts

‏password = input("أدخل كلمة المرور: ")
‏result, attempts = crack_password(password)
‏if result:
‏    print(f"تم اكتشاف كلمة المرور بنجاح: {result}")
‏    print(f"عدد المحاولات المستخدمة: {attempts}")
‏else:
‏    print("فشل في اكتشاف كلمة المرور.")
‏    print(f"عدد المحاولات المستخدمة: {attempts}")
