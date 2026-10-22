full_dot = '●'
empty_dot = '○'

def create_character (name, strength, intelligence, charisma): 

    if not isinstance (name, str):
        return ('The character name should be a string')
    else: 
        pass

    if name == '':
        return ('The character should have a name')
    else: pass

    if len(name) > 10:
        return ('The character name is too long')

    if ' ' in name:
        return ('The character name should not contain spaces')
    
    if not isinstance (strength, int):
        return ('All stats should be integers')
    elif not isinstance (intelligence, int):
        return ('All stats should be integers')
    elif not isinstance (charisma, int):
        return ('All stats should be integers')
    
    if strength < 1 or intelligence < 1 or charisma < 1:
        return ('All stats should be no less than 1')
    
    if strength > 4:
        return ('All stats should be no more than 4')
    elif intelligence > 4:
        return ('All stats should be no more than 4')
    elif charisma > 4:
        return ('All stats should be no more than 4')
    
    if strength + intelligence + charisma != 7:
        return ('The character should start with 7 points')

    str_line = full_dot * strength + empty_dot * (10 - strength)
    int_line = full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_line = full_dot * charisma + empty_dot * (10 - charisma)
        
    return f'{name}\nSTR {str_line}\nINT {int_line}\nCHA {cha_line}'
