import pandas as pd

names = ['user_id', 'item_id', 'rating', 'timestamp']
ratings = pd.read_table('ml-100k/ml-100k/u.data',sep='\t',header=None, names=names, encoding="ISO-8859-1")
ratings['item_id']=ratings['item_id'].astype(int)

movie_labels = ['item_id', 'movie title', 'release date',
				'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation',
				'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama',
				'Fantasy', 'Film-Noir', 'Horror', 'Mystery', 'Romance',
				'Sci-Fi', 'Thriller', 'War', 'Western']
movies = pd.read_table('ml-100k/ml-100k/u.item',sep='\t',header=None,names=movie_labels, encoding = "ISO-8859-1")
print(movies['item_id'])
user_labels = ['user_id', 'age', 'gender', 'occupation', 'zip code']
users = pd.read_table('ml-100k/ml-100k/u.user', sep='|', header=None, names=user_labels, encoding="ISO-8859-1")
#print(users.head())

#data = pd.merge(pd.merge(ratings, users), movies)
#print(data.head())