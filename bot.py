#imports
import discord
from dotenv import load_dotenv
from discord.ext import commands
import os


#loading in the token
load_dotenv()


TOKEN = os.getenv("TOKEN")


#coding our bot
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix=".", intents=intents)








#all the math stuff


def add(a, b, c, d, e, f):
    return a + b + c + d + e +f


def subtract(a, b, c, d, e, f):
    return a - b - c - d - e -f


def multiply(a, b, c, d, e, f):
    return a * b * c * d * e * f


def divide(a, b, c, d, e, f):
    return a / b / c / d / e / f

def pow(a, b):
    return a**b #this is the exponants, so it would be a to the power of b and would only work for one number 


#basic opporations
@bot.command()
async def calculate(ctx, num1, operation, num2, num3, num4, num5, num6): 
    a = int(num1)  
    b = int (num2)
    c = int (num3)
    d = int (num4)
    e = int (num5)
    f = int (num6)


    if operation == "+":
        output = add(a, b, c, d, e, f)
    elif operation == "-":
        output = subtract(a, b, c, d, e, f)
    elif operation == "*":
        output = multiply(a, b, c, d, e, f)
    elif operation == "/":
        output = divide(a, b, c, d, e, f)
    else:
        output = "nope"
    await ctx.send(output)
def calculate_expression(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    
    for token in expression.split():
        if token.isnumeric():
            output.append(token)
        elif token in operators:
            while (stack and stack[-1] in operators and
                    operators[token] <= operators[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove the left parenthesis
    
    while stack:
        output.append(stack.pop())

    result_stack = []
    for token in output:
        if token.isnumeric():
            result_stack.append(token)
        elif token in operators:
            a = result_stack.pop()
            b = result_stack.pop()
            c = result_stack.pop()
            d = result_stack.pop()
            e = result_stack.pop()
            f = result_stack.pop()



            if token == '+':
                result_stack.append(str(int(a) + int(b) + int(c) + int(d) + int(e) +int(f)))
            elif token == '-':
                result_stack.append(str(int(a) - int(b) - int(c) - int(d) - int(e) - int(f)))
            elif token == '*':
                result_stack.append(str(int(a) * int(b) * int(c) * int(d) * int(e) * int(f)))
            elif token == '/':
                result_stack.append(str(int(a) / int(b) / int(c) / int(d) /int(e) /int(f)))
            elif token == '^':
                result_stack.append(str(int(a) ** int(b)))
    
    return result_stack[0]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def calculate(ctx, *, expression):
    try:
        result = calculate_expression(expression)
        await ctx.send(f'Result: {result}')
    except Exception as e:
        await ctx.send(f'Error: {str(e)}')





#have to put spaces between everything 


bot.run(TOKEN)
