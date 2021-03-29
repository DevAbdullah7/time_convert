user = int(input("To 12 OR To 24: "))
try:
  if user == 12:
    hour = int(input('Hour: '))
    mint = int(input('Minute: '))
    try:
      if 0 <= hour <= 23 and 0 <= mint <= 59:
        print('wait...')
        if 1 <= hour <= 11:
          print('\nTime in 24 hour system: '+str(hour)+':'+str(mint))
          print('Time in 12 hour system: '+str(hour)+':'+str(mint)+' am')
        elif 13 <= hour <= 23:
          print('\nTime in 24 hour system: '+str(hour)+':'+str(mint))
          hour = hour - 12
          print('Time in 12 hour system: '+str(hour)+':'+str(mint)+' pm')
        elif hour == 0:
          print('\nTime in 24 hour system: '+str(hour)+':'+str(mint))
          print('Time in 12 hour system: 12:'+str(mint)+' am')
        elif hour == 12:
          print('\nTime in 24 hour system: '+str(hour)+':'+str(mint))
          print('Time in 12 hour system:  '+str(hour)+':'+str(mint)+' pm')
      else:
        raise Exception('Error: TIME IS WRONG !')
    except Exception as Error:
      print(Error)
  elif user == 24:
    hour = int(input('Hour: '))
    mint = int(input('Minute: '))
    am_pm = input('am or pm: ')
    am = 'am'
    pm = 'pm'
    try:
      if (am_pm == am) and (1 <= hour <= 12 and 0 <= mint <= 59):
        print('wait...')
        if 1 <= hour <= 11:
          print('\nTime in 12 hour system: '+str(hour)+':'+str(mint)+' am')
          print('Time in 24 hour system: '+str(hour)+':'+str(mint))
        elif hour == 12:
          print('\nTime in 12 hour system: 12:'+str(mint)+' am')
          print('Time in 24 hour system: 00:'+str(mint))
      elif (am_pm == pm) and (1 <= hour <= 12 and 0 <= mint <= 59):
        print('wait...')
        if 1 <= hour <= 11:
          print('\nTime in 12 hour system: '+str(hour)+':'+str(mint)+' pm')
          hour = hour + 12
          print('Time in 24 hour system: '+str(hour)+':'+str(mint))
        elif hour == 12:
          print('\nTime in 12 hour system: '+str(hour)+':'+str(mint)+' pm')
          print('Time in 24 hour system: '+str(hour)+':'+str(mint))
      else:
        raise Exception('Error: TIME IS WRONG !')
    except Exception as Error:
      print(Error)
  else:
    raise Exception('Error: YOUR CHOICE IS INCORRECT !')
except Exception as Error:
  print(Error)
