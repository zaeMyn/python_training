def get_format_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name =  first_name+ ' ' + middle_name +' ' +last_name
    else:
        full_name = first_name+ ' ' + last_name
    return full_name
musican = get_format_name('jimi','hendrix')
print(musican)
musican = get_format_name('jimi','hendrix','lee')
print(musican)