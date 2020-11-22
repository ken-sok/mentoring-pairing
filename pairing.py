import csv
import operator

'''
this script is to provide suggested groups for meetings in the mentorship program 
by pairing participants according to area of interests
'''
def controller(): 
    
    # get info on mentors and mentees
    mentors = mentors_interest()
    mentees = mentees_interest()
    
    #get mentees ranking of mentors
    mentees_ranking = mentee_rank_mentor(mentors, mentees)

    #group mentees into groups of 3 
    grouping_mentees(mentees_ranking, mentors)
    

def mentors_interest(): 

    # creating a dictionary of mentors' interests
    mentors_interest_dict = dict()
    with open('mentors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1

            else:

                # column 5 is the name of the mentor
                # column 8 is the interests of the mentor 
                mentors_interest_dict[f'{row[5]}'] = row[8].lower()
                line_count += 1

    return mentors_interest_dict

def mentees_interest(): 

    # creating a dictionary of dictionary of mentees' interests according to rank

    mentees_interest_dict = dict()
    with open('mentees.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                all_cols = list(row)
                line_count += 1
            else:
            
                # column 11 to 17 is the ranking for preferences
                one_student_rankings = dict()
                for i in range(11, 18): 

                    if row[i] not in one_student_rankings: 
                        one_student_rankings[row[i]] = all_cols[i]
                    
                    # to cover for the case when mentees rank the same for at least 2 interest 
                    else: 
                        one_student_rankings[row[i]] = one_student_rankings[row[i]] + ' ' + all_cols[i]
                    
                # column 5 is the name of the mentee
                mentees_interest_dict[f'{row[5]}'] = one_student_rankings
                
                line_count += 1
    
    return mentees_interest_dict

def mentee_rank_mentor(mentors, mentees): 
    
    ''' 
        use mentees' ranking of interest to create a score they would give to mentors
        lower score is the most preferred mentor for the mentee
        outputs a dictionary of students' name as key and value as mentor names and their points sorted ascending
    '''

    #print(mentees['Hung'])
    # dictionary to record the scores all mentees for each mentor
    all_student_scores = dict()
    
    for mentee in mentees: 

        # dictionary to store 1 mentee's score
        scores_one_mentee = dict()
        
        for mentor in mentors: 

            sum_scores_one_mentor = 0

            # there are 7 options of interest choice
            for rank in range(1, 8): 
                
                # add up scores for each mentor for 1 mentee

                # in case of "Hung" and "haodong" there are rankings missing due to duplicate rank
                
                if str(rank) in mentees[mentee]: 
                    if (mentees[mentee][str(rank)].lower() in mentors[mentor].lower()):
                        sum_scores_one_mentor += rank
                                            
            # final score for mentor by mentee
            scores_one_mentee[mentor] = sum_scores_one_mentor 

        # sort mentors with lowest score to the front 
        sorted_dict = dict(sorted(scores_one_mentee.items(), key=operator.itemgetter(1), reverse=False))
        
        # collate all students' rankings
        all_student_scores[mentee] = sorted_dict

    return all_student_scores
    


def grouping_mentees(ranking, mentors): 
    
    '''
    group mentees into mentor group by selecting the students who has sets the lowest scores for the mentors
    '''

    
    for mentor in mentors: 

        # find the students with three lowest scores in ranking dictionary
        for mentee in ranking: 

            
    
    #print('Sevri' in list(ranking['Nicholas'].items())[0])
controller()