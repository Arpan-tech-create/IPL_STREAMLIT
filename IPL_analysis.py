import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.rcParams.update({'font.size': 16})

st.header('ANALYSIS ON ')
st.image('download.jpg')
st.write('---------------------------')
st.write('---------------------------')
#load the Data

st.info('Dataset')
read=pd.read_csv('IPL Matches 2008-2020.csv')

st.write(read)
st.write('---------------------------')


st.sidebar.subheader('TOSS_DECISION')

#counting Features......

#1 . TOSS

toss=read['toss_decision'].value_counts()

st.sidebar.write(toss)


fig=plt.figure(figsize=(10,5))

plt.pie(read['toss_decision'].value_counts(),labels=read['toss_decision'].value_counts().index,autopct='%1.1f%%')

st.sidebar.pyplot(fig)

st.sidebar.write('-------------------------')

#result margin

st.subheader('Distribution of RESULT_MARGIN')

fig=plt.figure(figsize=(10,5))
sns.distplot(read['result_margin'])
st.pyplot(fig)

st.write('-------------------------')
st.write('-------------------------')

#team_winner Counts
st.subheader('MOST_WINNING_TEAM')
fig=plt.figure(figsize=(10,5))

team=read['winner'].value_counts()
bar=sns.barplot(x=read['winner'].value_counts().index,y=read['winner'].value_counts(),palette='magma')
for p in bar.patches:
    bar.annotate(format(p.get_height(), '.2f'),
                 (p.get_x() + p.get_width() / 2,
                  p.get_height()), ha='center', va='center',
                 size=10, xytext=(0, 8),
                 textcoords='offset points', color='purple')
plt.xticks(rotation=80)
st.pyplot(fig)


#toss_winner Counts....
st.sidebar.subheader('TOSS_WINNER')
toss_win=read['toss_winner'].value_counts()
st.sidebar.write(toss_win)
st.sidebar.image('mi.jpg')