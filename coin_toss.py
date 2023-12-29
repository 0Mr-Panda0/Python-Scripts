from random import randint

def coin_toss():
    return "HEADS!!" if randint(0,1) == 0 else "TAILS!!"

if __name__ == "__main__":
    result = coin_toss()
    print(f"it's {result}")
