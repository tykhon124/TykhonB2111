print("Kod do kapsulu")
for i in range(5):
    print(i+1)


try:
    print("Normal")
    print("Next print - error")
    print(error)
    print("After error")
except:
    print(f"Ви намагались поділити {ch1} на {ch2} і отримати помилку!")
    if ch2 == 0:
        print("На 0 ділити не можна")
else:
    print("Розрахунки закінченно!")