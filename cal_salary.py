
def annual_tax_map(annual_salary_amount):
    if annual_salary_amount < 36000:
        return 0.03, 0
    elif annual_salary_amount < 144000:
        return 0.10, 2520
    elif annual_salary_amount < 300000:
        return 0.20, 16920
    elif annual_salary_amount < 420000:
        return 0.25, 31920
    elif annual_salary_amount < 660000:
        return 0.30, 52920
    elif annual_salary_amount < 960000:
        return 0.35, 85920
    else:
        return 0.45, 181920

def reward_tax_map(reward):
    monthly_reward = reward / 12.
    if monthly_reward < 3000:
        return 0.03, 0
    elif monthly_reward < 12000:
        return 0.10, 210
    elif monthly_reward < 25000:
        return 0.20, 1410
    elif monthly_reward < 35000:
        return 0.25, 2660
    elif monthly_reward < 55000:
        return 0.30, 4410
    elif monthly_reward < 80000:
        return 0.35, 7160
    else:
        return 0.45, 15160


def after_tax_package_individual(salary, reward, special_discount, insurance=0, free=60000, month=12):
    annual_salary = salary * month
    tax_annual_salary = annual_salary - insurance - free - special_discount
    tax_rate, tax_extra_num = annual_tax_map(tax_annual_salary)
    annual_salary_tax = tax_annual_salary * tax_rate - tax_extra_num
    after_tax_annual_salary = annual_salary - insurance - annual_salary_tax

    reward_tax_rate, reward_tax_extra_num = reward_tax_map(reward)
    reward_tax = reward * reward_tax_rate - reward_tax_extra_num
    after_tax_reward = reward - reward_tax
    return after_tax_annual_salary + after_tax_reward


def after_tax_package_combined(salary, reward, special_discount, insurance=0, free=60000, month=12):
    annual_salary = salary * month + reward
    tax_annual_salary = annual_salary - insurance - free - special_discount
    tax_rate, tax_extra_num = annual_tax_map(tax_annual_salary)
    annual_salary_tax = tax_annual_salary * tax_rate - tax_extra_num
    after_tax_annual_salary = annual_salary - insurance - annual_salary_tax
    return after_tax_annual_salary


if __name__ == '__main__':
    after_tax_money = after_tax_package_individual(
        salary=50000,
        reward=150000,
        insurance=7628.6*12,
        special_discount=0,
    )
    print(f'年终奖单独计税到手{after_tax_money:.0f}元')

    after_tax_money = after_tax_package_combined(
        salary=50000,
        reward=150000,
        insurance=7628.6*12,
        special_discount=0,
    )
    print(f'年终奖合并计税到手{after_tax_money:.0f}元')
