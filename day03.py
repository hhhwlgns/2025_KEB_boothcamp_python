import random
drinks = ["위스키", "와인", "소주", "고량주"]
drinks_foods = ["초콜릿", "치즈", "삽겹살", "양꼬치"]

japan_drinks = ["사케", "위스키"]
japan_drinks_foods = ["광어회", "낙곱새"]
drinks.append(japan_drinks[0])
drinks_foods.append(japan_drinks_foods[0])
drinks[0] = japan_drinks[1]
drinks_foods[0] = japan_drinks_foods[1]

menu_list = ''
for i in range (len(drinks)):
    menu_list = menu_list + (f' {i+1}) {drinks[i]} ')
menu_list = menu_list + f' {len(drinks)+1}) 아무거나  {len(drinks)+2}) 종료'

def print_menu(k):
    print(f'{drinks[k]}에 어울리는 안주는 {drinks_foods[k]} 입니다.')
    print(f'')


while True:
    menu = int(input(f'다음 술중에 고르세요.\n {menu_list}'))

    if 0 < menu < len(drinks)+1:
        print_menu(menu-1)

    elif menu == len(drinks)+1:
        rdrink = random.randint(0, len(drinks) - 1)
        print(f'{drinks[rdrink]}에 어울리는 안주는 {drinks_foods[rdrink]} 입니다')

    elif menu == len(drinks)+2:
        print(f'다음에 또 오세요')
        break

    else:
        print(f'다시 입력하세요.')
