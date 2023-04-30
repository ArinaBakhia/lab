student_lang = {
    'Алексей': {'en', 'zh'},
    'Иннокентий': {'it', 'fr'},
    'Ибрагим': {'ko', 'zh', 'en'}
}

print(set.union(*student_lang.values()))
for stud, lang in student_lang.items():
    if 'zh' in lang:
        print(stud)
