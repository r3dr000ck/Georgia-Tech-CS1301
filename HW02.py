"""
Georgia Institute of Technology - CS1301
Homework 2 - Conditionals
"""

#########################################

"""
Function Name: buyTickets()
Parameters: num_people (int), ticket_section (str), days_before (int)
Returns: total_price (str)
"""

def buyTickets(num, section, days):
    base = 50.0
    if section == "Loge":
        base *= 1.5
    if section == "Courtside":
        base *= 2.5
    sum = base * num
    if days <= 3:
        sum += (num * 50.0)
    elif days <= 7:
        sum += (num * 20.0)
    print(f"Base price: ${round(base, 2)}/ticket")
    return f"The total for {num} people is: ${round(sum, 2)}"

#########################################

"""
Function Name: matchStatus()
Parameters: player_games_won (int), opponent_games_won (int)
Returns: status (str)
"""

def matchStatus(player, opp):
    if player >= 6:
        if player == 6 and opp == 6:
            return "Time for the tiebreak."
        if opp < player - 1:
            return "Player wins the set!"
        elif opp > player + 1:
            return "Player loses the set."
        else:
            return "Set still in progress."
    else:
        if opp >= 6 and opp > player + 1:
            return "Player loses the set."
        else:
            return "Set still in progress."

#########################################

"""
Function Name: tiebreak()
Parameters: player_1 (str), player_2 (str), score_1 (int), score_2 (int)
Returns: winner (str)
"""

def tiebreak(pl1, pl2, sc1, sc2):
    print(f'Score gap: {abs(sc1 - sc2)}')
    if max(sc1, sc2) >= 7:
        if abs(sc1 - sc2) >= 2:
            if sc1 > sc2:
                return f"{pl1} wins the tiebreak!"
            else:
                return f"{pl2} wins the tiebreak!"
    elif max(sc1, sc2) >= 6:
        if abs(sc1 - sc2) >= 1:
            if sc1 > sc2:
                return f"{pl1} is one point from winning!"
            else:
                return f"{pl2} is one point from winning!"
    
    if sc1 == sc2 and sc1 >= 6:
        return "Tiebreak is intense!"
    
    return "Tiebreak in progress!"

#########################################

"""
Function Name: playerStats()
Parameters: player_name (str), aces (int), double_faults (int), winners (int), unforced_errors (int)
Returns: player_performance (str)
"""

def playerStats(player_name, ace, db, win, fe):
    if ace < 0 or db < 0 or win < 0 or fe < 0:
        return f'Invalid stats for {player_name}.'
    
    serve = ace - (2 * db)
    ral = win - fe

    if serve >= 10 and ral >= 15:
        return f'{player_name} dominated the match! (Serve: {serve}, Rally: {ral})'
    elif serve >= 5 and ral >= 5:
        return f'{player_name} played a solid match. (Serve: {serve}, Rally: {ral}'
    elif serve < 5 and ral < 5:
        return f'{player_name} struggled in this match. (Serve: {serve}, Rally: {ral})'
    else:
        return f'{player_name} had a mixed performance. (Serve: {serve}, Rally: {ral})'

#########################################

"""
Function Name: tennisPredictor()
Parameters: player_1 (str), player_2 (str), stats_1 (int), stats_2 (int), head_to_head (str), matches_played_1 (int), matches_played_2 (int)
Returns: prediction (str)
"""

def tennisPredictor(pl1, pl2, st1, st2, hth, mp1, mp2):
    if st1 - st2 >= 15 and hth == "P1" and mp1 < 4:
        return f"{pl1} is predicted to win!"
    if st2 - st1 >= 15 and hth == "P2" and mp2 < 4:
        return f"{pl2} is predicted to win!"

    if st1 - st2 >= 15 and st1 >= 70 and hth in ["P1", "Tie"]:
        return f"{pl1} is predicted to win!"
    if st2 - st1 >= 15 and st2 >= 70 and hth in ["P2", "Tie"]:
        return f"{pl2} is predicted to win!d"
    
    if abs(st1 - st2) <= 5 and hth == "Tie":
        if mp1 < mp2:
            return f"{pl1} is predicted to win!"
        elif mp2 < mp1:
            return f"{pl2} is predicted to win!"
        else:
            return "Close match!"

    if abs(st1 - st2) <= 5:
        if hth == "P1" and st1 >= 60:
            return f"{pl1} is predicted to win!"
        if hth == "P2" and st2 >= 60:
            return f"{pl2} is predicted to win!"
    
    if hth == "Tie":
        return "Close match!"
    
#########################################
