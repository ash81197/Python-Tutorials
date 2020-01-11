def something(name = 'ASH', action = 'just ate his', item='breakfast'):
    print(name, action, item)


something('ASH', 'just ate his', 'breakfast')
something('ASH', 'just ate his', item='\0')
something('ASH', 'just ate his', '\0')
something('', 'just ate his', item='\0')
something(item='lunch')
something(action='didn\'t ate')
something(name='Someone')
