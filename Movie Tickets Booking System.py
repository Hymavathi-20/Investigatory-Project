import random

# function to select a movie
def movies():
  print('SELECT THE MOVIE TO WATCH:')
  print('1: MOVIE 1')
  print('2: MOVIE 2')
  print('3: MOVIE 3\n')
  movie=int(input('Enter the movie number:'))
  movies={1:'MOVIE 1',2:'MOVIE 2',3:'MOVIE 3'}
  data.append(movies[movie])
  print(f'You have selected {movies[movie]}\n')
  date()

# function to select a date to watch movie
def date():
  print('SELECT A DATE TO WATCH:')
  date=input('Enter the date (dd/mm/yy) :')
  print(f'You have selected {date} for your movie\n')
  data.append(date)
  theater()

# function to select a theater to watch in
def theater():
  print('SELECT A THEATER:')
  print('1: PVR')
  print('2: TRENDSET')
  print('3: PVP\n')
  theater=int(input('Enter the theater number:'))
  theaters={1:'PVR',2:'TRENDSET',3:'PVP'}
  data.append(theaters[theater])
  print(f'You have selected {theaters[theater]} theater\n')
  timing()

# function to select timing for the movie show
def timing():
  print('SELECT THE SHOW TIMING')
  print('1: 11:00am-02:00pm  MORNING SHOW')
  print('2: 02:30pm-06:00pm  MATINEE SHOW')
  print('3: 06:30pm-09:00pm  FIRST SHOW')
  print('4: 09:30pm-12:00pm  SECOND SHOW\n')
  timing=int(input('Enter show timing:'))
  timings={1:'11:00am-02:00pm',2:'02:30pm-06:00pm',3:'06:30pm-09:00pm',4:'09:30pm-12:00pm'}
  data.append(timings[timing])
  print(f'You have selected {timings[timing]} timing\n')
  seats()

# function to enter the number of movie tickets and seat type
def seats():
  count=int(input('Enter number of tickets to be booked:'))
  data.append(count)
  print('\nSELECT SEAT TYPE:')
  print('1: 250/-  VIP')
  print('2: 200/-  BALCONY')
  print('3: 150/-  CLASSIC')
  seat=int(input('Enter type of seat:'))
  seats={1:'VIP',2:'BALCONY',3:'CLASSIC'}
  costs={1:250,2:200,3:150}
  data.append(costs[seat])
  data.append(seats[seat]) #6
  seat_no(count)

# function to generate seat numbers
def seat_no(n):
  if data[5]==150:
    x=random.randint(1,40)
  elif data[5]==200:
    x=random.randint(41,80)
  elif data[5]==250:
    x=random.randint(81,100)
  data.append(f'{x}-{x+n}')
  print(f'\nYour seat nos are {x}-{x+n}')
  price()


# function to display total price for tickets
def price():
  total=data[5] * data[4]
  data.append(total)
  print(f'Total fare is {total}/-')



data=[] # empty list to append all the entered data about ticket booking

# MAIN PROGRAM
def book():
  print('_'*100,'\n')
  print(' '*35,'WELCOME TO SHOWBOOKS!!')
  print('\n',' '*28,'WATCH TELUGU MOVIES IN VIJAYWADA NOW!')
  print('_'*100,'\n')
  movies()
  print('_'*100,'\n')
  print('TICKET DETAILS:\n')
  print(f'MOVIE: {data[0]}')
  print(f'DATE: {data[1]}')
  print(f'THEATER: {data[2]}')
  print(f'TIMINGS: {data[3]}')
  print(f'TICKETS: {data[4]}')
  print(f'SEAT TYPE: {data[6]}')
  print(f'SEAT NO. : {data[7]}')
  print(f'TOTAL AMOUNT: {data[8]}')
  print('\nHave a great movie experience!!\n')
  print('_'*100,'\n')

book()
