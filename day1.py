def main():
    with open('input/day1.txt') as file:
        expense_report = file.readlines()

    expense_report = list(map(lambda line : line.strip(), expense_report))

    ANOMALY = 2020

    print(find_solution(expense_report, ANOMALY))

def find_solution(expense_report, ANOMALY):
    for x_index in range(len(expense_report)):
        for y_index in range(x_index+1, len(expense_report)):
            x = int(expense_report[x_index])
            y = int(expense_report[y_index])

            print(x+y)
            if x + y == ANOMALY:
                print(f'x: {x}')
                print(f'y: {y}')
                # print(f'solution: {x*y}')
                return x*y

main()