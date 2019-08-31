import time
import pandas as pd
import numpy as np
import statistics
from statistics import mode

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """Asks user to specify a city, month, and day to analyze."""
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('what city would you like to look at: chicago, new york city, or washington?').lower()
    """city=chicago"""
    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
        "invalid input! Please type another city: ").lower()

    print('great! we will look at {}.'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('what month would you like to look at: all, january, february, march, april, may, or june?')
    month = month.lower()
    while month not in ['all','january','february','march','april','may','june']:
        month = input(
        "invalid input! Please type another month: ").lower()

    print('great! we will look at {}.'.format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('what day of week would you like to look at: all, mon, tues, wed, thurs, fri, sat, or sun?')
    day = day.lower()
    while day not in ['all', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']:
        day = input(
        "invalid input! Please type another day: ").lower()
    print('great! we will look at {}.'.format(day))

    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month']=pd.to_datetime(df['Start Time']).dt.month
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    month_lib={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6}
    day_lib={'mon':0,'tues':1,'wed':2,'thurs':3,'fri':4,'sat':5,'sun':6}
    #monthdf is our filtered by month dataframe

    if month=='all':
        monthdf=df
    else:
        monthnum=month_lib[month]
        monthdf=df['month']==monthnum
        monthdf=df[monthdf]

    if day=='all':
        daymonthdf=monthdf
    else:
        daynum=day_lib[day]
        daymonthdf=monthdf['day_of_week']==daynum
        daymonthdf=monthdf[daymonthdf]
        #remove false rows


    return daymonthdf

def time_stats(df):

    month_lib={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6}
    day_lib={'mon':0,'tues':1,'wed':2,'thurs':3,'fri':4,'sat':5,'sun':6}
    #most common month
    months=df['month']
    mon_pop=mode(months)
    for key, value in month_lib.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
        if value == mon_pop:
            mon_pop_name=key
    print('The most popular month is: ', format(mon_pop_name))

    #most common dow
    days=df['day_of_week']
    day_pop=mode(days)
    for key, value in day_lib.items():
        if value == day_pop:
            day_pop_name=key
    print('The most popular day of the week is: ', format(day_pop_name))

    #most common hour
    hours=df['hour']
    hour_pop=mode(hours)
    print('The most popular hour is: ', format(hour_pop))

def station_stats(df):
    start_stations=df['Start Station']
    start_station_pop=mode(start_stations)
    print('The most popular start station is: ', format(start_station_pop))

    end_stations=df['End Station']
    end_station_pop=mode(end_stations)
    print('The most popular end station is: ', format(end_station_pop))

    start_end=(df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip is: ', format(start_end))

def trip_duration_stats(df):

    total_travel = df['Trip Duration'].sum()
    print('Total travel time =', format(total_travel), 'seconds.')
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time =', format(mean_travel), 'seconds.')

def display_raw_data(df, line_by_line):
    display=input('would you like to see 5 lines of raw user data?').lower()
    if display =='yes':
        print(df.iloc[line_by_line:line_by_line+5])
        line_by_line += 5
        return display_raw_data(df, line_by_line)
    if display =='no':
        return
    else:
        print('error. type yes or no.')
        return display_raw_data(df, line_by_line)
def user_stats(df):
    user_type_count = df['User Type'].value_counts()
    print('User type count is: ', format(user_type_count))

    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print('gender count is: ', format(gender_count))
    else:
        print('washington did not collect gender info')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        min_birth_year = df['Birth Year'].min()
        print('Earliest =', format(min_birth_year))

        max_birth_year = df['Birth Year'].max()
        print('Youngest =', format(max_birth_year))

        common_birth_year = df['Birth Year'].mode()[0]
        print('most common year of birth is' , format(common_birth_year))
    else:
        print('washington did not collect info on birth year')
def main():
    while True:
        global city, month, day
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df,0)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    #https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
    #https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
    #https://stackoverflow.com/questions/55719762/how-to-calculate-mode-over-two-columns-in-a-python-dataframe
    #http://www.java2s.com/Tutorial/JavaScript/0060__Statement/Setloopstepto5inforloop.htm
