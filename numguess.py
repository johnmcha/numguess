from random import randint

# create random number integer
answer = randint (1, 100)
print(answer)
# get user's name, guess

user_name = input('hello what is your name?')
guess = input(f'hi,{user_name}. guess the number (1-100): ')

# print to check
print(user_name, guess)

# check and print correct or not

if guess == answer:
    print('congratulation')
else:
    print(f'you failed to guess correct answer, {answer}')
