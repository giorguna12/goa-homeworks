#2) შექმენით 3 ცვლადი, num1, num2, num3. ამ სამ ცვლადზე მოახდინეთ ყველა მათემატიკური ოპერაცია რაც ვიცით
#3) შექმენით მოხმარებლის Account. შემოატანინეთ სახელი, გვარი, ასაკი და პაროლი. ეს ყველაფერი გამოიტანეთ ეკრანზე.
#4) გააკეთეთ იგივე რაც მესამეში, f stringის გამოყენებით
#( ყველა დავალებაში გამოიყენეთ კომენტარები და best practiceბი)

num1 = 5

num2 = 15

num3 = 10

print(num1 + num2 + num3 )

print(num2 - num1 - num3) 

print(num1 * num2 * num3)

print(num2 / num1 / num3) 


#დავალება( 3 )

user_input = input("თქვენი სახელი: ")

surname = input("თქვენი გვარი: ")

age = int(input("თქვენიასაკი: "))

pasword = input("თქვენი პაროლი: ")

print(user_input,surname,age,pasword)

#დავალება(4)

print(f"{user_input} {surname} {age} {pasword}")




