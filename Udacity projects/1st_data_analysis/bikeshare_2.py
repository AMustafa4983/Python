import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city=input('enter the city name (chicago , new york city , washington) : ').lower()
            while city not in ['chicago' , 'new york city' , 'washington']:
                print("\n invalid Name\n")
                city=input('enter the city name (chicago , new york city , washington) : ').lower()
            break
        except (ValueError,RuntimeError,KeyboardInterrupt):
            print("\n invalid Name\n")
            

    # get user input for month (all, january, february, ... , june)
    while True :
        try:
            month=input('if you want filter by month enter month name if not enter all : ').lower()
            while month not in ['january','february','march','april','may','june','july','august','september','october','november','december','all']:
            
                print("\n invalid Name\n")
                month=input('if you want filter by month enter month name if not enter all : ').lower()
            break
        except (ValueError,RuntimeError,KeyboardInterrupt):
            print("\n invalid Name\n")
            


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day=input('if you want filter by day enter day name if not enter all : ').lower()
            while day not in ['sunday','monday','thursday','wednesday','tuesday','friday','saturday','all']:
                print("\n invalid Name\n")
                day=input('if you want filter by day enter day name if not enter all : ').lower()
            break
        except (ValueError,RuntimeError,KeyboardInterrupt):
            print("\n invalid Name\n")
            

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['weekday_name'] = df['Start Time'].dt.day_name()
    df['Hours'] = df['Start Time'].dt.hour

    months_names=['January','February','March','April','May','June','July','August','September','October','November','December',]
    
    if month != "all" :
        month = month.title()
        month = months_names.index(month)+1
        df = df[df['month'] == month]


    if day != "all" :
        df = df[df['weekday_name'] == day.title()]
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    Common_Month = "Most common Month : "
    print(Common_Month,df['month'].mode()[0])
    # display the most common month
    Common_Day= "Most common Day of Week : "
    print(Common_Day,df['weekday_name'].mode()[0])
    # display the most common day of week
    Common_Hour = "Most common Start Hour : "
    print(Common_Hour,df['Hours'].mode()[0])
    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("Most Commonly Start Station is ",df['Start Station'].mode()[0])
    # display most commonly used start station

    print("Most Commonly Start Station is ",df['End Station'].mode()[0])
    # display most commonly used end station
    print("Most Frequent Combination of Start and End Station trip is ",(df['Start Station'] + ' , ' + df['End Station']).mode()[0])
   # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("Total Travel Time is ",df['Trip Duration'].sum())
    # display total travel time

    
    print("Mean Travel Time is ",df['Trip Duration'].mean())
    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("Counts of User Types is \n",df['User Type'].value_counts())
    # Display counts of user types
    if city != 'washington':

        print("Counts of Gender is \n",df['Gender'].value_counts())
    # Display counts of gender
        print("Earliest Birth Year is ",df['Birth Year'].min())
        print("Most Recent Birth Year is ",df['Birth Year'].max())
        print("Most common Birth Year is ",df['Birth Year'].mode()[0])
    # Display earliest, most recent, and most common year of birth
    else:
        print("\nGender and Birth Year NotFound\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def describe_Data(df):
    while True :
        try:
            request = input('Do you want to see 5 lines of raw data ? Enter (Yes/No) : ').lower()
            while request not in ['yes','no']:
                print("\n Invalid input \n")
                request = input('Do you want to see 5 lines of raw data ? Enter (Yes/No) : ').lower()
            break
        except ValueError:
            print("\n invalid input \n")
            
    
    if request == 'yes':
        print(df.iloc[0:5])        
        while True:
            try:
                request_more = input('Do you want to see more lines of raw data ? Enter (Yes/No) : ').lower()
                while request_more not in ['yes','no']:
                    print("\n Invalid input \n")
                    request_more = input('Do you want to see more lines of raw data ? Enter (Yes/No) : ').lower()
                break
            except ValueError:
                print("\n Invalid input \n")

        if request_more == 'yes':
            while True :
                try:
                    request_raw_num = int(input('How much lines do you need ? Enter integer number : '))
                    break
                except ValueError:
                    print("\n Invalid input \n")
            print(df.iloc[0:request_raw_num])




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        describe_Data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
