scores_list = [
    {'school_class':'4a','scores':[3,4,4,5,2]},
    {'school_class':'4b','scores':[4,5,3,3,4]},
    {'school_class':'3a','scores':[5,5,5,5,5]},
    {'school_class':'5b','scores':[2,3,4,4,3]}
    ]

school_score_summ = 0 #Без этого не работало
school_score_count = 0 #

for class_nmb in scores_list:
    class_score_summ = 0 #Обнуление для каждого класса
    class_score_count = 0 #
    
    for each_score in class_nmb['scores']:    
        class_score_summ += each_score
        class_score_count += 1 #Вместо этого наверн можно использовать len
        school_score_summ += each_score
        school_score_count += 1
    class_score_average = class_score_summ / class_score_count 
    print(class_nmb['school_class']+': '+str(class_score_average))
    
school_score_average = school_score_summ / school_score_count
print(f'School average: {school_score_average}')