print ("...Welcome to Maths-Quiz...")


while True:
    num_b = list(range(1 ,11))
    num_e = list(range(11 ,101))
    point = 0

    import random
    level = input("Enter your current level {Beginner(B) , Expert(E) , Grandmaster(G)} ").upper()

# For Beginner Level
    s_num_1 = random.choice(num_b)
    s_num_2 = random.choice(num_b)
    s_num_3 = random.choice(num_b)
    s_num_4 = random.choice(num_b)
    s_num_5 = random.choice(num_b)
    s_num_6 = random.choice(num_b)

# For Expert Level  
    s_num_7 = random.choice(num_e)
    s_num_8 = random.choice(num_e)
    s_num_9 = random.choice(num_e)
    s_num_10 = random.choice(num_e)
    s_num_11 = random.choice(num_e)
    s_num_12 = random.choice(num_e)

    count = 0
    limit = 3   


    if level == "B":
        opretion = input("Enter math opretion which you want to practice {+ (addition) , - (minus) , * (multiplication) , / (division)} ")
        print("Ready for your math quiz!!!")
        if opretion == "*":
         while count < limit :
          if level == "B" and count == 0 :
           ans = int(input(f"{s_num_1} X {s_num_2} = "))
           if ans == s_num_1*s_num_2 :
            count += 1
            point += 10
            print ("10 points")

           else :
            print("❌You Failed!!!")

         
          elif level == "B" and count == 1 :
            ans = int(input(f"{s_num_3} X {s_num_4} = "))
            if ans == s_num_3*s_num_4 :
                count += 1
                point += 10
                print("10 points")

            else :
             print("❌You Failed!!!")
        
          elif level == "B" and count == 2 :
            ans = int(input(f"{s_num_5} X {s_num_6} = "))
            if ans == s_num_5*s_num_6 :
                print("20 points")
                print("✅You win the math quiz!!!")
                point += 20
                print("Your total points is :",point)
                break

            else :
             print("❌You Failed!!!")

        elif opretion == "+":
         while count < limit :
            if level == "B" and count == 0:
                ans = int(input(f"{s_num_1} + {s_num_2} = "))
                if ans == s_num_1+s_num_2 :
                  count += 1
                  point += 10
                  print("10 points")

                else :
                 print("❌You Failed!!!")

            elif level == "B" and count == 1:
              ans = int(input(f"{s_num_3} + {s_num_4} = "))
              if ans == s_num_3+s_num_4 :
               count += 1
               point += 10
               print("10 points")

              else :
                print("❌You Failed!!!")
        
            elif level == "B" and count == 2:
                ans = int(input(f"{s_num_5} + {s_num_6} = "))
                if ans == s_num_5+s_num_6 :
                    print("20 points")
                    print("✅You win the math quiz!!!")
                    point += 20
                    print("Your total points is :",point)
                    break

                else :
                 print("❌You Failed!!!")

        elif opretion == "-":
         while count < limit :
            if level == "B" and count == 0:
             ans = int(input(f"{s_num_1} - {s_num_2} = "))
             if ans == s_num_1-s_num_2 :
                 count += 1
                 point += 10
                 print("10 points")

             else :
                print("❌You Failed!!!")

            elif level == "B" and count == 1:
             ans = int(input(f"{s_num_3} - {s_num_4} = "))
             if ans == s_num_3-s_num_4 :
                count += 1
                point += 10
                print("10 points")

             else :
                print("❌You Failed!!!")

            elif level == "B" and count == 2:
             ans = int(input(f"{s_num_5} - {s_num_6} = "))
             if ans == s_num_5-s_num_6 :
                print("20 points")
                print("✅You win the math quiz!!!")
                point += 20
                print("Your total points is :",point)
                break

            else :
                print("❌You Failed!!!")

        elif opretion == "/":
         while count < limit :
            if level == "B" and count == 0:
              ans = float(input(f"{s_num_1} ÷ {s_num_2} = "))
              if ans == s_num_1/s_num_2 :
               count += 1
               point += 10
               print("10 points")

              else :
                 print("❌You Failed!!!")

            elif level == "B" and count == 1:
                ans = float(input(f"{s_num_3} ÷ {s_num_4} = "))
                if ans == s_num_3/s_num_4 :
                  count += 1
                  point += 10
                  print("10 points")

                else :
                 print("❌You Failed!!!")
        
            elif level == "B" and count == 2:
                ans = float(input(f"{s_num_5} ÷ {s_num_6} = "))
                if ans == s_num_5/s_num_6 :
                    print("20 points")
                    print("✅You win the math quiz!!!")
                    point += 20
                    print("Your total points is :",point)
                    break

                else :
                 print("❌You Failed!!!")

    elif level == "E":
        opretion = input("Enter math opretion which you want to practice {+ (addition) , - (minus) , * (multiplication) , / (division)} ")
        print("As a expert this is very is easy for you !!!")
        if opretion == "*":
         while count < limit :
            if level == "E" and count == 0 :
             ans = int(input(f"{s_num_7} X {s_num_8} = "))
             if ans == s_num_7*s_num_8 :
                 count += 1
                 point += 20
                 print("20 points")


             else :
              print("❌You Failed!!!")

            elif level == "E" and count == 1 :
             ans = int(input(f"{s_num_9} X {s_num_10} = "))
             if ans == s_num_9*s_num_10 :
              count += 1
              point += 20
              print("20 points")


             else :
                print("❌You Failed!!!")
        
            elif level == "E" and count == 2 :
             ans = int(input(f"{s_num_11} X {s_num_12} = "))
             if ans == s_num_11*s_num_12 :
                print("50 points")
                print("✅You win the math quiz!!!")
                point += 50
                print("Your total points is :",point)
                break

             else :
              print("❌You Failed!!!")

        elif opretion == "+":
            while count < limit :
                if level == "E" and count == 0:
                 ans = int(input(f"{s_num_7} + {s_num_8} = "))
                 if ans == s_num_7+s_num_8 :
                     count += 1
                     point += 20
                     print("20 points")

                 else :
                  print("❌You Failed!!!")

                elif level == "E" and count == 1:
                 ans = int(input(f"{s_num_9} + {s_num_10} = "))
                 if ans == s_num_9+s_num_10 :
                    count += 1
                    point += 20
                    print("20 points")

                 else :
                        print("❌You Failed!!!")
        
                elif level == "E" and count == 2:
                    ans = int(input(f"{s_num_11} + {s_num_12} = "))
                    if ans == s_num_11+s_num_12 :
                     print("50 points")
                     print("✅You win the math quiz!!!")
                     point += 50
                     print("Your total points is :",point)
                     break

                    else :
                        print("❌You Failed!!!")

        elif opretion == "-":
         while count < limit :
          if level == "B" and count == 0:
            ans = int(input(f"{s_num_7} - {s_num_8} = "))
            if ans == s_num_7-s_num_8 :
             count += 1
             point += 20
             print("20 points")

            else :
             print("❌You Failed!!!")

          elif level == "E" and count == 1:
            ans = int(input(f"{s_num_9} - {s_num_10} = "))
            if ans == s_num_9-s_num_10 :
             count += 1
             point += 20
             print("20 points")

            else :
                print("❌You Failed!!!")
        
          elif level == "E" and count == 2:
            ans = int(input(f"{s_num_9} - {s_num_10} = "))
            if ans == s_num_9-s_num_10 :
             print("50 points")
             print("✅You win the math quiz!!!")
             point += 50
             print("Your total points is :",point)
             break

            else :
             print("❌You Failed!!!")

        elif opretion == "/":
         while count < limit :
          if level == "E" and count == 0:
           ans = float(input(f"{s_num_7} ÷ {s_num_8} = "))
           if ans == s_num_7/s_num_8 :
            count += 1
            point += 20
            print("20 points")

           else :
            print("❌You Failed!!!")

          elif level == "E" and count == 1:
           ans = float(input(f"{s_num_9} ÷ {s_num_10} = "))
           if ans == s_num_9/s_num_10 :
             count += 1
             point += 20
             print("20 points")

           else :
             print("❌You Failed!!!")
        
          elif level == "E" and count == 2:
           ans = float(input(f"{s_num_11} ÷ {s_num_12} = "))
           if ans == s_num_11/s_num_12 :
             print("50 points")
             print("✅You win the math quiz!!!")
             point += 50
             print("Your total points is :",point)
             break

           else :
                print("❌You Failed!!!")

    elif level == "G":
        print("Let's begin the Grandmaster level math quiz!")
        while count < limit :
         if count == 0:
          ans = int(input(f"[({s_num_7} + {s_num_8}) X {s_num_1}] - {s_num_2} = "))
          if ans == ((s_num_7 + s_num_8) * s_num_1) - s_num_2 :
                count += 1
                point += 50
                print("50 points")
    
          else :
                print("❌You Failed!!!")

         elif count == 1:
            ans = int(input(f"[({s_num_9} + {s_num_10}) X {s_num_3}] - {s_num_4} = "))
            if ans == ((s_num_9 + s_num_10) * s_num_3) - s_num_4 :
                    count += 1
                    point += 50
                    print("50 points")
        
            else :
                    print("❌You Failed!!!")

         elif count == 2:
            ans = int(input(f"[({s_num_11} + {s_num_12}) X {s_num_5}] - {s_num_6} = "))
            if ans == ((s_num_11 + s_num_12) * s_num_5) - s_num_6 :
                    print("100 points")
                    print("✅You win the granmaster math quiz!!!")
                    point += 100
                    print("Your total points is :",point)
                    break
        
            else :
                    print("❌You Failed!!!")

    choice = input("Do you want play again yes/no :- ").lower()
    if choice != "yes" :
         break
