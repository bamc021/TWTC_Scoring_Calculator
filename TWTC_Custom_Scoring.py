# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:20:17 2024

@author: mccol
"""

from pybaseball import pitching_stats
from pybaseball import batting_stats
import pandas as pd
import streamlit as st

#-------------Function to recalculate points based on user inputs--------------
def recalculate_points():
    hitting_ptvalues = [hitter_hits,hitter_singles,hitter_doubles,hitter_triples,hitter_homeruns,hitter_runs,hitter_rbi,
                        hitter_walks,hitter_ks,hitter_hbp,hitter_sacfly,hitter_sachit,hitter_sb,hitter_cs,hitter_ab]
    
    pitching_ptvalues = [pitcher_wins,pitcher_losses,pitcher_qs,pitcher_cg,pitcher_sho,pitcher_saves,pitcher_holds,
                         pitcher_blown,pitcher_innings,pitcher_hits,pitcher_er,pitcher_homeruns,pitcher_walks,pitcher_hbp,
                         pitcher_ks]
    
    
    hitpoints = sum(hittingdata[col] * points for col, points in zip(hittingstats, hitting_ptvalues))
    hittingdata['TWTCpoints'] = sum(hittingdata[col] * points for col, points in zip(hittingstats, TWTC_hitting))
    hittingdata['points'] = hitpoints
    hittingdata['pts/g'] = hittingdata['points']/hittingdata['G']
    hittingdata['matchup_pts'] = hittingdata['pts/g']*7
    formattedhitdata = pd.DataFrame(data=hittingdata,columns=['Rank','TWTCRank','rank_diff','Name','Team','G','points','TWTCpoints','ptsdiff','pts/g','matchup_pts'])

    pitchpoints = sum(pitchingdata[col] * points for col, points in zip(pitchingstats, pitching_ptvalues))
    pitchingdata['TWTCpoints'] = sum(pitchingdata[col] * points for col, points in zip(pitchingstats, TWTC_pitching))
    pitchingdata['points'] = pitchpoints
    pitchingdata['pts/g'] = pitchingdata['points']/pitchingdata['G']
    pitchingdata['matchup_pts'] = pitchingdata['pts/g']*1.4
    formattedpitchdata = pd.DataFrame(data=pitchingdata,columns=['Rank','TWTCRank','rank_diff','Name','Team','G','points','TWTCpoints','ptsdiff','pts/g','matchup_pts'])
    
    finaltable = pd.concat([formattedhitdata,formattedpitchdata])
    finaltable['ptsdiff'] = finaltable['points']-finaltable['TWTCpoints']
    finaltable['Rank'] = finaltable['points'].rank(method='min',ascending=False)
    finaltable['TWTCRank'] = finaltable['TWTCpoints'].rank(method='min',ascending=False)
    finaltable['rank_diff'] = finaltable['Rank']-finaltable['TWTCRank']
    
#------------------------------------------------------------------------------

# #-----------Function to assign point values based on chosen template-----------
# def points_template():
#     if scoringtemplate == "2024 TWTC":
#         hitter_hits.value = float(0)
#         hitter_singles.value = float(1)
#         hitter_doubles.value = float(2)
#         hitter_triples.value = float(3)
#         hitter_homeruns.value = float(5)
#         hitter_runs.value = float(1)
#         hitter_rbi.value = float(1)
#         hitter_walks.value = float(1)
#         hitter_ks.value = float(-1)
#         hitter_hbp.value = float(1)
#         hitter_sacfly.value = float(0)
#         hitter_sachit.value = float(0)
#         hitter_sb.value = float(2)
#         hitter_cs.value = float(-2)
#         hitter_ab.value = float(0)
        
#         pitcher_wins.value = float(7)
#         pitcher_losses.value = float(-3)
#         pitcher_qs.value = float(5)
#         pitcher_cg.value = float(10)
#         pitcher_sho.value = float(0)
#         pitcher_saves.value = float(3)
#         pitcher_holds.value = float(2)
#         pitcher_blown.value = float(-3)
#         pitcher_innings.value = float(1)
#         pitcher_hits.value = float(0)
#         pitcher_er.value = float(-1)
#         pitcher_homeruns.value = float(-2)
#         pitcher_walks.value = float(-1)
#         pitcher_hbp.value = float(0)
#         pitcher_ks.value = float(1)
        
#     elif scoringtemplate == "Standard Fantrax":
#         hitter_hits.value = float(0))
#         hitter_singles.value = float(1)
#         hitter_doubles.value = float(2)
#         hitter_triples.value = float(3)
#         hitter_homeruns.value = float(4)
#         hitter_runs.value = float(1)
#         hitter_rbi.value = float(1)
#         hitter_walks.value = float(1)
#         hitter_ks.value = float(0)
#         hitter_hbp.value = float(1)
#         hitter_sacfly.value = float(0)
#         hitter_sachit.value = float(0)
#         hitter_sb.value = float(2)
#         hitter_cs.value = float(0)
#         hitter_ab.value = float(0)
        
#         pitcher_wins.value = float(10)
#         pitcher_losses.value = float(-5)
#         pitcher_qs.value = float(3)
#         pitcher_cg.value = float(0)
#         pitcher_sho.value = float(0)
#         pitcher_saves.value = float(7)
#         pitcher_holds.value = float(0)
#         pitcher_blown.value = float(0)
#         pitcher_innings.value = float(1)
#         pitcher_hits.value = float(0)
#         pitcher_er.value = float(-1)
#         pitcher_homeruns.value = float(0)
#         pitcher_walks.value = float(0)
#         pitcher_hbp.value = float(0)
#         pitcher_ks.value = float(1)
        
#     elif scoringtemplate == "Standard ESPN":
#         hitter_hits.value = float(0)
#         hitter_singles.value = float(1)
#         hitter_doubles.value = float(2)
#         hitter_triples.value = float(3)
#         hitter_homeruns.value = float(4)
#         hitter_runs.value = float(1)
#         hitter_rbi.value = float(1)
#         hitter_walks.value = float(1)
#         hitter_ks.value = float(-1)
#         hitter_hbp.value = float(0)
#         hitter_sacfly.value = float(0)
#         hitter_sachit.value = float(0)
#         hitter_sb.value = float(1)
#         hitter_cs.value = float(0)
#         hitter_ab.value = float(0)
        
#         pitcher_wins.value = float(2)
#         pitcher_losses.value = float(-2)
#         pitcher_qs.value = float(0)
#         pitcher_cg.value = float(0)
#         pitcher_sho.value = float(0)
#         pitcher_saves.value = float(2)
#         pitcher_holds.value = float(2)
#         pitcher_blown.value = float(0)
#         pitcher_innings.value = float(3)
#         pitcher_hits.value = float(-1)
#         pitcher_er.value = float(-2)
#         pitcher_homeruns.value = float(0)
#         pitcher_walks.value = float(-1)
#         pitcher_hbp.value = float(0)
#         pitcher_ks.value = float(1)
        
#     elif scoringtemplate == "Fangraphs":
#         hitter_hits.value = 5.6
#         hitter_singles.value = float(0)
#         hitter_doubles.value = 2.9
#         hitter_triples.value = 5.7
#         hitter_homeruns.value = 9.4
#         hitter_runs.value = float(0)
#         hitter_rbi.value = float(0)
#         hitter_walks.value = float(3)
#         hitter_ks.value = float(0)
#         hitter_hbp.value = float(3)
#         hitter_sacfly.value = float(0)
#         hitter_sachit.value = float(0)
#         hitter_sb.value = 1.9
#         hitter_cs.value = -2.8
#         hitter_ab.value = float(-1)
        
#         pitcher_wins.value = float(0)
#         pitcher_losses.value = float(0)
#         pitcher_qs.value = float(0)
#         pitcher_cg.value = float(0)
#         pitcher_sho.value = float(0)
#         pitcher_saves.value = float(5)
#         pitcher_holds.value = float(4)
#         pitcher_blown.value = float(0)
#         pitcher_innings.value = float(5)
#         pitcher_hits.value = float(0)
#         pitcher_er.value = float(0)
#         pitcher_homeruns.value = float(-13)
#         pitcher_walks.value = float(-3)
#         pitcher_hbp.value = float(-3)
#         pitcher_ks.value = float(2)
        
#     elif scoringtemplate == "Fangraphs Alt":
#         hitter_hits.value = 5.6
#         hitter_singles.value = float(0)
#         hitter_doubles.value = 2.9
#         hitter_triples.value = 5.7
#         hitter_homeruns.value = 9.4
#         hitter_runs.value = float(0)
#         hitter_rbi.value = float(0)
#         hitter_walks.value = float(3)
#         hitter_ks.value = float(0)
#         hitter_hbp.value = float(3)
#         hitter_sacfly.value = float(0)
#         hitter_sachit.value = float(0)
#         hitter_sb.value = 1.9
#         hitter_cs.value = -2.8
#         hitter_ab.value = float(-1)
        
#         pitcher_wins.value = float(0)
#         pitcher_losses.value = float(0)
#         pitcher_qs.value = float(0)
#         pitcher_cg.value = float(0)
#         pitcher_sho.value = float(0)
#         pitcher_saves.value = float(5)
#         pitcher_holds.value = float(4)
#         pitcher_blown.value = float(0)
#         pitcher_innings.value = 7.4
#         pitcher_hits.value = -2.6
#         pitcher_er.value = float(0)
#         pitcher_homeruns.value = -12.3
#         pitcher_walks.value = float(-3)
#         pitcher_hbp.value = float(-3)
#         pitcher_ks.value = float(2)
# #------------------------------------------------------------------------------

st.set_page_config(
    page_title="TWTC Scoring System Calculator",
    layout="wide"
    )

qualitystarts = pd.read_csv('https://raw.githubusercontent.com/bamc021/TWTC_Scoring_Calculator/refs/heads/main/Pitchers%20QS.csv')

finaltable = pd.DataFrame(columns=['Rank','TWTCRank','rank_diff','Name','Team','G','points','TWTCpoints','ptsdiff','pts/g','matchup_pts'])

pitchingdata = pitching_stats(2024,qual=1)
hittingdata = batting_stats(2024,qual=1)

pitchingdata = pitchingdata.merge(qualitystarts[['Name', 'QS']], on='Name', how='left')

columns = pitchingdata.columns

hittingcolumns = ['IDfg','Name','Team','G','AB','PA','H','1B','2B','3B','HR','R','RBI','BB','SO','HBP','SF','SH','SB','CS','AB']
pitchingcolumns = ['IDfg','Name','Team','G','W','L','QS','CG','ShO','SV','HLD','BS','IP','H','ER','HR','BB','HBP','SO']

hittingstats = ['H','1B','2B','3B','HR','R','RBI','BB','SO','HBP','SF','SH','SB','CS','AB']
pitchingstats = ['W','L','QS','CG','ShO','SV','HLD','BS','IP','H','ER','HR','BB','HBP','SO']

hittingdata = hittingdata[hittingcolumns]
pitchingdata = pitchingdata[pitchingcolumns]

TWTC_hitting = [0.0,1.0,2.0,3.0,5.0,1.0,1.0,1.0,-1.0,1.0,0.0,0.0,2.0,-2.0,0.0]
TWTC_pitching = [7.0,-3.0,5.0,10.0,0.0,3.0,2.0,-3.0,1.0,0.0,-1.0,-2.0,-1.0,0.0,1.0]

h = st.container(border=True)
h.header("Hitting",divider="green")
h.col1,h.col2,h.col3,h.col4,h.col5,h.col6,h.col7,h.col8 = h.columns(8)
with h.col1:
    hitter_hits = st.number_input('H',value=TWTC_hitting[0],format="%0.1f")
    hitter_ks = st.number_input('K',value=TWTC_hitting[8],format="%0.1f")

with h.col2:
    hitter_singles = st.number_input('1B',value=TWTC_hitting[1],format="%0.1f")
    hitter_hbp = st.number_input('HBP',value=TWTC_hitting[9],format="%0.1f")

with h.col3:
    hitter_doubles = st.number_input('2B',value=TWTC_hitting[2],format="%0.1f")
    hitter_sacfly = st.number_input('SF',value=TWTC_hitting[10],format="%0.1f")

with h.col4:
    hitter_triples = st.number_input('3B',value=TWTC_hitting[3],format="%0.1f")
    hitter_sachit = st.number_input('SH',value=TWTC_hitting[11],format="%0.1f")

with h.col5:
    hitter_homeruns = st.number_input('HR',value=TWTC_hitting[4],format="%0.1f")
    hitter_sb = st.number_input('SB',value=TWTC_hitting[12],format="%0.1f")

with h.col6:
    hitter_runs = st.number_input('R',value=TWTC_hitting[5],format="%0.1f")
    hitter_cs = st.number_input('CS',value=TWTC_hitting[13],format="%0.1f")

with h.col7:
    hitter_rbi = st.number_input('RBI',value=TWTC_hitting[6],format="%0.1f")
    hitter_ab = st.number_input('AB',value=TWTC_hitting[14],format="%0.1f")

with h.col8:
    hitter_walks = st.number_input('BB',value=TWTC_hitting[7],format="%0.1f")
    
p = st.container(border=True)
p.header("Pitching",divider="green")
p.col1,p.col2,p.col3,p.col4,p.col5,p.col6,p.col7,p.col8 = p.columns(8)
with p.col1:
    pitcher_wins = st.number_input('W',value=TWTC_pitching[0],format="%0.1f")
    pitcher_innings = st.number_input('IP',value=TWTC_pitching[8],format="%0.1f")

with p.col2:
    pitcher_losses = st.number_input('L',value=TWTC_pitching[1],format="%0.1f")
    pitcher_hits = st.number_input('h',value=TWTC_pitching[9],format="%0.1f")

with p.col3:
    pitcher_qs = st.number_input('QS',value=TWTC_pitching[2],format="%0.1f")
    pitcher_er = st.number_input('ER',value=TWTC_pitching[10],format="%0.1f")

with p.col4:
    pitcher_cg = st.number_input('CG',value=TWTC_pitching[3],format="%0.1f")
    pitcher_homeruns = st.number_input('hr',value=TWTC_pitching[11],format="%0.1f")

with p.col5:
    pitcher_sho = st.number_input('SHO',value=TWTC_pitching[4],format="%0.1f")
    pitcher_walks = st.number_input('bb',value=TWTC_pitching[12],format="%0.1f")

with p.col6:
    pitcher_saves = st.number_input('SV',value=TWTC_pitching[5],format="%0.1f")
    pitcher_hbp = st.number_input('hbp',value=TWTC_pitching[13],format="%0.1f")

with p.col7:
    pitcher_holds = st.number_input('HLD',value=TWTC_pitching[6],format="%0.1f")
    pitcher_ks = st.number_input('SO',value=TWTC_pitching[14],format="%0.1f")

with p.col8:
    pitcher_blown = st.number_input('BS',value=TWTC_pitching[7],format="%0.1f")

col1,col2 = st.columns(2)
# with col1:
#     scoringtemplate = st.selectbox("Scoring System Templates",
#                                ['2024 TWTC','Standard Fantrax','Standard ESPN','Fangraphs','Fangraphs Alt'],
#                                on_change = lambda: points_template()
#                                )
with col2:
    recalculate = st.button("Recalculate",
                            on_click = lambda: recalculate_points()
                            )
hittingdata = hittingdata.loc[:, ~hittingdata.columns.duplicated()]

pointstable = st.dataframe(finaltable)