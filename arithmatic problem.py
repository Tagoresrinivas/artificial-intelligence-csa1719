from itertools import permutations

def solve_puzzle():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)
    
    for perm in permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        
        # Skip solutions where 'S' or 'M' is 0, as per the problem statement
        if sol['S'] == 0 or sol['M'] == 0:
            continue
        
        send = sol['S'] * 1000 + sol['E'] * 100 + sol['N'] * 10 + sol['D']
        more = sol['M'] * 1000 + sol['O'] * 100 + sol['R'] * 10 + sol['E']
        money = sol['M'] * 10000 + sol['O'] * 1000 + sol['N'] * 100 + sol['E'] * 10 + sol['Y']
        
        if send + more == money:
            return sol, send, more, money
    
    return None, None, None, None

solution, send, more, money = solve_puzzle()
if solution:
    print(f"Solution: {solution}")
    print(f"{send} + {more} = {money}")
else:
    print("No solution found.")
