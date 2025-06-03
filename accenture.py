#!/usr/bin/env python
# coding: utf-8

# In[189]:


import pandas as pd


# In[190]:


df=pd.read_csv('Location1.csv')


# In[191]:


df2=pd.read_csv('User1.csv')


# In[192]:


#reaction,content,location,user,profile,session


# In[193]:


df


# In[194]:


df.rename(columns = {'User ID':'UserID'}, inplace = True)


# In[195]:


df2.rename(columns={'User ID':'UserID'},inplace=True)


# In[196]:


df


# In[197]:


df.UserID.nunique()


# In[198]:


df.head()


# In[199]:


df2.head()


# In[200]:


df.shape


# In[201]:


df2.shape


# In[202]:


data=df.merge(df2,how='outer') 


# In[203]:


merged_inner = pd.merge(left=df, right=df2, left_on='UserID', right_on='UserID')


# In[204]:


merged_inner.head()


# In[205]:


merged_inner.columns


# In[206]:


dw=merged_inner.dropna(subset=['Unnamed: 0_x','Unnamed: 0_y'],inplace=True)


# In[207]:


merged_inner.head()


# In[208]:


merged_inner.drop('Unnamed: 0_x',axis=1,inplace=True)
merged_inner.drop('Unnamed: 0_y',axis=1,inplace=True)


# In[209]:


merged_inner.head()


# In[210]:


#[user,location,session,profile],reaction,content,reactiontype


# In[211]:


reaction=pd.read_csv('Reactions.csv')


# In[212]:


reaction.shape


# In[213]:


content=pd.read_csv('Content.csv')


# In[214]:


content.shape


# In[215]:


session=pd.read_csv('Session.csv')


# In[216]:


session.columns


# In[29]:


session.rename(columns={'USERID':'UserID'},inplace=True)


# In[30]:


session.rename(columns={'User ID':'UserID'},inplace=True)


# In[31]:


session.head()


# In[32]:


df=pd.merge(left=merged_inner,right=session,left_on='UserID',right_on='UserID')


# In[33]:


df.head()


# In[34]:


df.drop('Unnamed: 0',axis=1,inplace=True)


# In[35]:


df.head()


# In[36]:


profile=pd.read_csv('Profile.csv')


# In[37]:


profile.rename(columns={'User ID':'UserID'},inplace=True)


# In[38]:


profile.head()


# In[39]:


df=pd.merge(left=df,right=profile,left_on='UserID',right_on='UserID')


# In[40]:


df.head()


# In[41]:


df.drop('Unnamed: 0',axis=1,inplace=True)


# In[42]:


df.head()


# In[43]:


reaction.shape


# In[44]:


content.shape


# In[45]:


content.rename(columns={'Content ID':'ContentID'},inplace=True)


# In[46]:


content.rename(columns={'User ID':'UserID'},inplace=True)


# In[47]:


reaction.rename(columns={'Content ID':'ContentID'},inplace=True)
reaction.rename(columns={'User ID':'UserID'},inplace=True)


# In[48]:


content.columns


# In[49]:


content.ContentID.nunique()


# In[50]:


df.head()


# In[51]:


reaction.columns


# In[52]:


df3=pd.merge(left=content,right=reaction,left_on='ContentID',right_on='ContentID')


# In[53]:


df3.drop('Unnamed: 0_x',axis=1,inplace=True)
df3.drop('Unnamed: 0_y',axis=1,inplace=True)
df3.drop('UserID_x',axis=1,inplace=True)


# In[54]:


df3.head(100)


# In[55]:


df3.shape


# In[56]:


output=pd.merge(left=df3,right=df,left_on='UserID_y',right_on='UserID')


# In[57]:


final1=output.drop('Device',axis=1)
final1.drop('Email',axis=1,inplace=True)
final1.drop('Name',axis=1,inplace=True)
final1.drop('URL',axis=1,inplace=True)
final1.drop('Duration',axis=1,inplace=True)


# In[58]:


final1.head()#userid


# In[59]:


final1.shape


# In[60]:


output = final1.duplicated(keep='first')


# In[61]:


output.head()


# In[62]:


output=final1[~output]


# In[63]:


output.head(100)#contentid


# In[64]:


output.rename(columns={'Type_y':'Reaction'},inplace=True)


# In[ ]:





# In[65]:


output.rename(columns={'Interests':'user_interest'},inplace=True)


# In[66]:


output.rename(columns={'Type_x':'Type'},inplace=True)


# In[67]:


final=output[['ContentID','Type','Category','Reaction','UserID','Datetime','user_interest','Age']]


# In[68]:


final.shape


# In[69]:


final1 = final.duplicated(keep='first')


# In[70]:


final1.shape


# In[71]:


final1.head()


# In[72]:


final[~final1]


# In[73]:


final.head()


# In[74]:



final['sentiment'] = final['Reaction'].replace(['disgust'],'Negative')
final['sentiment'] = final['sentiment'].replace(['hate'],'Negative')
final['sentiment'] = final['sentiment'].replace(['dislike'],'Negative')
final['sentiment'] = final['sentiment'].replace(['scared'],'Negative')
final['sentiment'] = final['sentiment'].replace(['worried'],'Negative')
final['sentiment'] = final['sentiment'].replace(['interested'],'positive')
final['sentiment'] = final['sentiment'].replace(['heart'],'positive')
final['sentiment'] = final['sentiment'].replace(['want'],'positive')
final['sentiment'] = final['sentiment'].replace(['love'],'positive')
final['sentiment'] = final['sentiment'].replace(['super love'],'positive')
final['sentiment'] = final['sentiment'].replace(['cherish'],'positive')
final['sentiment'] = final['sentiment'].replace(['adore'],'positive')
final['sentiment'] = final['sentiment'].replace(['like'],'positive')
final['sentiment'] = final['sentiment'].replace(['intrigued'],'positive')
final['sentiment'] = final['sentiment'].replace(['indifferent'],'neutral')
final['sentiment'] = final['sentiment'].replace(['peeking'],'neutral')
output=final


# In[75]:


output.shape


# In[76]:


final.sentiment.unique()


# In[77]:


final['score'] = final['Reaction'].replace(['disgust'],0)
final['score'] = final['score'].replace(['hate'],5)
final['score'] = final['score'].replace(['dislike'],10)
final['score'] = final['score'].replace(['scared'],15)
final['score'] = final['score'].replace(['worried'],12)
final['score'] = final['score'].replace(['interested'],30)
final['score'] = final['score'].replace(['heart'],60)
final['score'] = final['score'].replace(['want'],70)
final['score'] = final['score'].replace(['love'],65)
final['score'] = final['score'].replace(['super love'],75)
final['score'] = final['score'].replace(['cherish'],70)
final['score'] = final['score'].replace(['adore'],72)
final['score'] = final['score'].replace(['like'],50)
final['score'] = final['score'].replace(['intrigued'],45)
final['score'] = final['score'].replace(['indifferent'],20)
final['score'] = final['score'].replace(['peeking'],35)


# In[78]:


final.head(50)


# In[79]:


final.sentiment.unique()


# In[80]:


final.head()


# In[81]:


final.columns


# In[82]:


final=final[['ContentID', 'Type', 'Category', 'Reaction','sentiment', 'score','UserID','user_interest','Age','Datetime']]


# In[83]:


final.head()


# In[84]:


final.shape


# # Visuali

# In[ ]:





# In[ ]:





# In[85]:


popular_category=final.Category.value_counts()


# In[86]:


popular_category=popular_category.head(16)


# In[87]:


popular_category


# In[88]:


grouped_df = final.groupby("Category")


# In[89]:


sum = grouped_df.sum()


# In[90]:


sum = sum.reset_index()


# In[91]:


sum


# In[92]:


final.head(100)


# In[93]:


final.Category.unique()


# In[94]:


import nltk
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()


# In[95]:


def stem(text):
    y=[]
    
    for i in text.split():
        y.append(ps.stem(i))
        
    return " ".join(y)


# In[96]:


final['Category']=final['Category'].apply(stem)


# In[97]:


final.Category.unique()


# In[98]:


grouped_df = final.groupby("Category")


# In[99]:


sum = grouped_df.sum()


# In[100]:


sum = sum.reset_index()


# In[101]:


sum


# In[102]:


df=(final.Category=='anim')


# In[103]:


final.loc[df,'Category']='"animals"'


# In[104]:


final.Category.nunique()


# In[105]:


df=(final.Category=='cook')
final.loc[df,"Category"]='"cooking"'


# In[106]:


final.Category.nunique()


# In[107]:


df=(final.Category=='cultur')
final.loc[df,"Category"]='"culture"'
df=(final.Category=='dog')
final.loc[df,"Category"]='"dogs"'
df=(final.Category=='educ')|(final.Category=='studi')
final.loc[df,"Category"]='"Studying"'
df=(final.Category=='food')
final.loc[df,"Category"]='"food"'
df=(final.Category=='public speak')
final.loc[df,"Category"]='"public speaking"'


# In[108]:


final.Category.nunique()


# In[109]:


df=(final.Category=='scienc')
final.loc[df,"Category"]='"science"'
df=(final.Category=='soccer')
final.loc[df,"Category"]='"soccer"'
df=(final.Category=='educ')|(final.Category=='technolog')
final.loc[df,"Category"]='"technology"'
df=(final.Category=='vegan')
final.loc[df,"Category"]='"veganism"'
df=(final.Category=='"studying"')
final.loc[df,"Category"]="studying"


# In[110]:


final.Category.unique()


# In[ ]:





# In[111]:


grouped_df = final.groupby("Category")
sum = grouped_df.sum()
sum = sum.reset_index()
sum


# In[112]:


final.head(100)


# In[162]:


final[["Category",'user_interest']].replace({
    'tenni': 'tennis', 
    'healthi eat': 'healthy eating', 
    '"animals"': 'animals', 
    '"culture"': 'culture', 
    '"dogs"': 'dogs', 
    '"food"': 'food', 
    '"public speaking"': 'public speaking', 
    '"speaking"': 'speaking', 
    '"technology"': 'technology', 
    '"veganism"': 'veganism',
    '"Studying"':'studying',
    '"soccer"':"soccer",
    '"science"':"science",
    '"cooking"':"cooking"
  },inplace=True)


# In[163]:


final.Category.unique()


# In[164]:


final.head()


# In[165]:


final.Category.nunique()


# In[166]:


grouped_df = final.groupby("Category")
sum = grouped_df.sum()
sum = sum.reset_index()
sum


# In[167]:


import seaborn as sns


# In[168]:


final.head(50)


# In[169]:


final.Category.unique()


# In[170]:


sns.countplot(x=final['Category'])


# In[171]:


import seaborn as sns
import matplotlib.pyplot as plt
 
# count plot on single categorical variable
plt.figure(figsize=(15,8))
sns.countplot(x ='Category', data = final)
 
# Show the plot
plt.show()


# In[172]:


final.to_csv('accenture1.csv')


# In[173]:


final.shape


# In[174]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[175]:


final.head()


# In[ ]:


sns.histplot(final.Age, kde=True)
plt.show()
sns.set_theme(style="darkgrid")


# In[ ]:


final['user_interest']=final['user_interest'].apply(stem)


# In[178]:


final.user_interest.nunique()


# In[179]:


grouped_df = final.groupby("Category")


# In[180]:


sns.histplot(final.user_interest, kde=True)
plt.show()
sns.set_theme(style="darkgrid")


# In[181]:


x=final.user_interest.unique()


# In[182]:


from collections import Counter


# In[183]:


split_it = x.split()


# In[ ]:


from collections import Counter
y=Counter(" ".join(final["user_interest"]).split()).most_common(200)


# In[184]:


y


# In[ ]:


z=y.apply(stem)


# In[ ]:


print(final.user_interest.tolist())


# In[ ]:


final.user_interest.unique()


# In[188]:


final.columns


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




