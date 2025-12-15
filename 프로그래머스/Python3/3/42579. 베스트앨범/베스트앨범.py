from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    play_dict = defaultdict(int)
    genre_dict = defaultdict(list)
    
    for i, (genre, play) in enumerate(zip(genres, plays)) :
        play_dict[genre] += play
        genre_dict[genre].append((i, play))
    
    ## sort by most genre played
    totalPlays = sorted(play_dict.items(), key=lambda x : x[1], reverse=True)
    
    ## sort by plays in each genre
    for _, item in genre_dict.items() :
        item.sort(key=lambda x : x[1], reverse=True)


    ## add 
    for genre, _ in totalPlays :
        if len(genre_dict[genre]) == 1 :
            answer.append(genre_dict[genre][0][0])
        else :
            answer.append(genre_dict[genre][0][0])
            answer.append(genre_dict[genre][1][0])
            
        

    return answer