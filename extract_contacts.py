import re

input_example_text = '''
Welcome to @ISI. If you need any help from HR you can write to @Milo#Minderbinder. For any technical problems you should contact
@Major#Major or @Hristo#sTOIchkov. If you need any smart advises, please contact @Ali#Baba or @John#Yossarian. When you are sick, please stay at #Home.
'''


def return_contacts(input_text):
    search_pattern = r'@([A-Z][a-z]+)#([A-Z][a-z]+)'  # Regex search pattern to find #Word@Anotherword
    result = re.finditer(search_pattern, input_text)
    valid_contacts = []
    print('Valid contacts:')
    for i in result:
        contact = i.group()
        valid_contacts.append(contact)
        print(i.group())
    return valid_contacts


print(return_contacts(input_example_text))
# print(return_contacts(input()))
