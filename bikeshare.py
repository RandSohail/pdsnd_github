import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    valid_citys = ['chicago', 'new york', 'washington']
    while True:
        city = input('Choose one city from those: Chicago, New York, Washington\n').lower()
        if city in valid_citys:
            break
        else:
            print('Invalid input only one of these: Chicago, New York, Washington')
    # get user input for month (all, january, february, ... , june)
    valid_months=[1, 2, 3, 4, 5, 6, 7]
    while True:
        try:
            month = int(input('Choose a month to filter the data: January, February, March, April, May, June, All (use number to present each month 1-6, 7 -> All )\n'))
            if month in valid_months:
                break
            else:
                print('Invalid input only one of these: 1, 2, 3, 4, 5, 6, 7 -> All')
        except ValueError:
            print("Invalid input. Please enter a valid value.")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "All"]
    while True:
        day = input('Choose a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All \n').title()
        if day in valid_days_of_week:
            break
        else:
            print('Invalid input only one of these: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All')

    print('-'*40)
    # , month, day
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

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from 'Start Time' to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by monthapplicable
    if month != 7:
        # months = ['january', 'february', 'march', 'april', 'may', 'june']
        # month_index = months.index(month) + 1
        df = df[df['month'] == month]

    # # Filter by day of week if applicable
    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months_dictionary = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June"
    }
    # display the most common month
    print('Common month =>', months_dictionary[df['month'].mode()[0]])

    # display the most common day of week
    print('Common day of week =>', df['day_of_week'].mode()[0])

    # display the most common start hour
    print('Common start hour =>', df['Start Time'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Commonly use start station => ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Commonly use end station => ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    # .size().idxmax()
    print('Commonly frequent combination of start station and end station => ', df.groupby(['Start Station', 'End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time => ', df['Trip Duration'].sum())

    # display mean travel time
    print('Mean travel time => ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Total Number of users', df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('Gender Counts:\n', gender_counts)
    else:
        print('Gender information not available.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('Earliest Birth Year:', earliest_birth_year)
        print('Most Recent Birth Year:', most_recent_birth_year)
        print('Most Common Birth Year:', most_common_birth_year)
    else:
        print('Birth year information not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no:\n').lower()
        start_loc = 0
        pd.set_option('display.max_columns', None)
        while view_data == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue? Enter yes or no: ").lower()
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
