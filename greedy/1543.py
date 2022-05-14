document = input()
keyword = input()
len_keyword = len(keyword)
len_document = len(document)

keyword_amount = 0

for i in range(len_document):
    not_same = False
    for j in range(i, min(i + len_keyword, len_document)):
        if document[j] != keyword[j - i]:
            not_same = True
    if not_same == False and len_keyword + i < len_document:
        keyword_amount += 1

print(keyword_amount)