import calendar
from datetime import datetime
from dateutil import relativedelta

def day_by_number(num):
    return ["Пн", "Вт", "Ср", "Чт", "Пт"][num]

hui =  {'January':[1,2,3,4,5,6,7,8],
            'February':[23],
            'March':[8],
            'April':[],
            'May':[1,9],
            'June':[12],
            'July':[],
            'August':[],
            'September':[],
            'Oсtober':[],
            'November':[4],
            'December':[]}
def is_holiday():
    return {'January':[1,2,3,4,5,6,7,8],
            'February':[23],
            'March':[8],
            'April':[],
            'May':[1,9],
            'June':[12],
            'July':[],
            'August':[],
            'September':[],
            'Oсtober':[],
            'November':[4],
            'December':[]}


def create_date_btn():
    current_date = datetime.now()
    curr_day = current_date.day
    curr_month = current_date.month
    curr_year = current_date.year
    next_date = (current_date + relativedelta.relativedelta(months=1))
    next_month = next_date.month
    next_year = next_date.year
    tc = calendar.TextCalendar(firstweekday=0)
    date_lst_curr = tc.monthdayscalendar(curr_year,curr_month)
    date_lst_next = tc.monthdayscalendar(next_year,next_month)
    curr_month_name = current_date.strftime('%B')
    next_month_name = next_date.strftime('%B')
    btn_lst_curr = [f"{day_by_number(j)} {i[j]}" for i in date_lst_curr for j in range(len(i)) if i[j] !=0 and j!=5 and j!=6 and i[j]>=curr_day and i[j] not in is_holiday()[curr_month_name]]
    btn_lst_next = [f"{day_by_number(j)} {i[j]}" for i in date_lst_next for j in range(len(i)) if i[j] !=0 and j!=5 and j!=6 and i[j] not in is_holiday()[next_month_name]]
    LEXICON ={curr_month_name:{f"butd_{i+1}":btn_lst_curr[i] for i in range(len(btn_lst_curr))} ,next_month_name:{f"butd_{i+1}":btn_lst_next[i] for i in range(len(btn_lst_next))}}
   
    return LEXICON

if __name__ == "__main__":
    for month,i in enumerate(hui):
        print(month , i)
    
    
