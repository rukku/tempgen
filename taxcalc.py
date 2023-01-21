import streamlit as st
import random

st.title('PhilSA Tax Calculator 2023 💸')

# if st.button("Generate", key=None, help=None):
#     st.write(round(random.uniform(35.5,37.5), 1))


salary_grades = (range(1, 34))

sg_list = {
    1:  13000,
    2:  13819.00,
    3:  14678.00, 
    4:  15586,
    5:  16543,
    6:  17553,
    7:  18620,
    8:  19744,
    9:  21211,
    10: 23176,
    11: 27000,
    12: 29165,	
    13: 31320,
    14: 33843,
    15: 36619,
    16: 39672,
    17: 43030,
    18: 46725,
    19: 51357, 
    20: 57347,
    21: 63997,
    22: 71511,
    23: 80003,
    24: 90078,
    25: 102690,
    26: 116040,
    27: 131124,	
    28: 148171,
    29: 167432,
    30: 189199,	
    31: 278434,
    32: 331954,	
    33: 419144,
}


option = st.selectbox(
    'What is your salary grade??',
    salary_grades)


# Constants

basic_salary = sg_list[option]
total_basic_salary = basic_salary*12

pera = 2000
total_pera = pera*12

clothing_allowance = 6000
midyear_bonus = basic_salary
yearend_bonus = basic_salary
cash_gift = 5000
pei = 5000
sri_2022 =   16285.28 


# deductions
gsis = total_basic_salary * 0.09
pagibig = 1200


#=(IF(AND(B3>1,B3<10000.01),400,IF(AND(B3>10000,B3<80000),(B3*4%),IF(B3>79999.99,3200,0)))/2)*12
def get_phic(bs):
    if 1< bs < 10000.01:
        result = 400
    elif 10000 < bs < 80000:
        result = bs * 0.04
    elif bs > 79999.99:
        result = 3200
    return 12 * result/2

phic = get_phic(basic_salary)

def get_rata(sg):
    if sg == 31:
        return 336000
    elif sg in (27, 28):
        return 216000
    elif sg == 30:
        return 264000
    elif sg in (24, 25):
        return 120000
    else:
        return 0

rata = get_rata(option)
# RATA
# =IF(B2=31,336000,IF(OR(B2=28,B2=27),216000,IF(B2=30,264000,IF(OR(B2=24,B2=25),120000,0))))

total_compensation = total_basic_salary + total_pera + clothing_allowance + midyear_bonus + yearend_bonus + cash_gift + pei + sri_2022 + rata



# Exemptions

# =IF((B8+B9+5000+B12)>90000,90000,(B8+B9+B11+B12))

def get_nontaxable_bonus(myb, yeb, peib, srib):
    if myb + yeb + 5000 + srib > 90000:
        return 90000
    else:
        return myb + yeb + peib + srib


nontaxable_bonus = get_nontaxable_bonus(midyear_bonus, yearend_bonus, pei, sri_2022)


total_nontaxable_income = gsis + pagibig + phic + total_pera + nontaxable_bonus + clothing_allowance + cash_gift + rata
taxable_income = total_compensation - total_nontaxable_income

def get_annual_tax(ti):
    if 250000 < ti < 400001:
        return (ti - 250000) * 0.15
    elif 400000 < ti < 800001:
        return (ti - 400000) * 0.20 + 22500
    elif 800000 < ti < 2000001:
        return (ti - 800000) * 0.25 + 102500
    elif 2000000 < ti < 8000001:
        return (ti - 2000000) * 0.30 + 402500
    elif ti  > 8000000:
        return (ti - 8000000) * 0.35 + 2202500
    else:
        return 0

annual_tax_due = get_annual_tax(taxable_income)
monthly_deduction_from_jan_to_nov = annual_tax_due/11

# st.write( f"Basic Salary: {basic_salary:,.2f} " )
# st.write( f"Total Salary: {total_basic_salary:,.2f} " )
# st.write( f"Total PERA: {total_pera:,.2f} " )
# st.write( f"RATA: {rata:,.2f} " )
# st.write( f"Clothing Allowance: {clothing_allowance:,.2f} " )
# st.write( f"Mid-Year Bonus: {basic_salary:,.2f} " )
# st.write( f"Year-End Bonus: {basic_salary:,.2f} " )
# st.write( f"PEI: {pei:,.2f} " )
# st.write( f"Cash Gift: {cash_gift:,.2f} " )
# st.write( f"SRI 2022: {sri_2022:,.2f} " )
# st.write( f"Total Compensation: {total_compensation:,.2f}")

# st.write(f"GSIS: {gsis:,.2f}")
# st.write(f"Pag-IBIG: {pagibig:,.2f}")
# st.write(f"PHIC: {phic:,.2f} ")
# st.write(f"Non-Taxable Bonus: {nontaxable_bonus:,.2f}")
# st.write(f"Total Non-Taxable Income: {total_nontaxable_income:,.2f}")
# st.write(f"Taxable Income: {taxable_income:,.2f}")
# st.write(f"Annual Tax Due: {annual_tax_due:,.2f}")
# st.write(f"Monthy Deductions from January to November: {monthly_deduction_from_jan_to_nov:,.2f}")


table = f'''




# Tax Computation

|  | Amount |
| --- | ---:|
| Total Salary | {total_basic_salary:,.2f} |
| Total Compensation | {total_compensation:,.2f} |
| Total Non-Taxable Income | {total_nontaxable_income:,.2f} |
| Taxable Income | {taxable_income:,.2f} |
| Annual Tax Due | {annual_tax_due:,.2f} |
|      Monthly Deductions from January to November | {monthly_deduction_from_jan_to_nov:,.2f} |
| Net Compensation | {total_compensation-annual_tax_due:,.2f} |

## Compensation 

| | Amount |
| --- | ---:|
| Basic Salary | {basic_salary:,.2f} |
| Total Salary | {total_basic_salary:,.2f} |
| Total PERA | {total_pera:,.2f} |
| RATA | {rata:,.2f} |
| Clothing Allowance | {clothing_allowance:,.2f} |
| Mid-Year Bonus | {basic_salary:,.2f} |
| Year-End Bonus | {basic_salary:,.2f} |
| PEI | {pei:,.2f} |
| Cash Gift | {cash_gift:,.2f} |
| SRI 2022 | {sri_2022:,.2f} |
| **Total Compensation** | **{total_compensation:,.2f}** |


## Exemptions and Deductions

### Deductions
|  | Amount |
| --- | ---:|
| GSIS | {gsis:,.2f} |
| Pag-IBIG | {pagibig:,.2f} |
| PHIC | {phic:,.2f} |      

### Deductions
|  | Amount |
| --- | ---:|
| PERA | {gsis:,.2f} |
| RATA | {rata:,.2f} |
| Non-Taxable Bonuses | {phic:,.2f} |
| Clothing Allowance | {clothing_allowance:,.2f} |
| Cash Gift | {cash_gift:,.2f} |
| Total Non-Taxable Income | {total_nontaxable_income:,.2f} |

'''

st.markdown(table)

# with st.expander(f"Total Compensation : {total_compensation:,}"):
#     st.markdown(table)

# with st.expander(f"Taxable Income : {taxable_income:,.2f}"):
#     st.markdown(table)

# with st.expander(f"Annual Tax Due: {annual_tax_due:,.2f}"):
#     st.markdown(table)