data = [("username1","phone_number1", "email1"),("usernameX","phone_number1", "emailX"),("usernameZ","phone_numberZ", "email1Z"),("usernameY","phone_numberY", "emailX"),]
print(str(data[0]), type(data[0]))


def create_same_person_list(full_list):
    list_same_person = []
    added_person_index= []
    for i in range(0,len(full_list)):
        person = []
        element = full_list[i]
        if i not in added_person_index:
            person.append(i)
            added_person_index.append(i)
            for j in range(i+1, len(full_list)):
                element2 = full_list[j]
                if j not in added_person_index and len(tuple(set(element2).intersection(set(element))))>0:
                    person.append(j)
                    added_person_index.append(j)
                    element = element + element2
        else:
            pass

        if len(person) > 0:
            list_same_person.append(person)
            print(added_person_index)
    return list_same_person

print(create_same_person_list(data))
