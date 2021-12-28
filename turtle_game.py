import turtle
import random

player_one = turtle.Turtle()
player_one.color = "green"
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color = "blue"
player_two.penup()
player_two.goto(-200,-100)

player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)

player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)
dice = [1,2,3,4,5,6]
for i in range(20):
    if player_one.pos() >= (300,100):
        print("P1 WINS!!!")
        break
    elif player_two.pos() >= (300,-100):
        print("P2 wins!!!")
        break
    else:
        p1_turn = input("P1:hit 'enter' to roll")
        p1_dice = random.choice(dice)
        print(f"P1 rolls {p1_dice}")
        print(f"P1 moves: {p1_dice * 20}")
        player_one.fd(p1_dice *20)
        p2_turn = input("P2:hit 'enter' to roll")
        p2_dice = random.choice(dice)
        print(f"P2 rolls {p2_dice}")
        print(f"P2 moves: {p2_dice * 20}")
        player_two.fd(p2_dice *20)