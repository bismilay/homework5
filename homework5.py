immutable_var = (1, 2, 3, 'trap', 'crack' )
print(immutable_var)
#immutable_var[2]= 'banana' #я закомментирую эту строку,чтобы сделать остальные задания
print(immutable_var) #МЫ не можем изменить кортеж так, как он является неизменяемым объектом то, есть содержит не сам список а его ссылку,особенность в изменении заключается во внедрении в кортеж списка,тем самым можно обойти данный этап
mutable_list = [1.4, 2, 5, 'run', 'six']
print(mutable_list)
mutable_list[3] = 'five'
mutable_list.append('cat')
print(mutable_list)