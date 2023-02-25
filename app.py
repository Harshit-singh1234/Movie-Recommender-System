from urllib import response
import webbrowser
import streamlit as st
import  pickle
import  pandas as pd
import  requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=3f07eb54d5c504d2afdda35c1593d05b&language=en-US".format(
        movie_id)
    data = requests.get(url)
    #print(data)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies ['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list :
        movie_id=movies.iloc[i[0]].	movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters



movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')
selected_movie_name=st.selectbox(
    'Select Movie',
    movies['title'].values)
if st.button('Recommend Me' ):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5,col6 = st.columns(6)
    st.balloons()
    with col1:
        movie_name_str = " ".join(names[0])
        youtube_url =f"https://www.youtube.com/results?search_query="+movie_name_str.replace(" ", "")+"full_movie"
        st.text(names[0])
        st.image(posters[0])
        #print(youtube_url)
        st.write("**Movie** [link](%s)" % youtube_url)
    with col2:
        movie_name_str = " ".join(names[1])
        youtube_url = f"https://www.youtube.com/results?search_query=" + movie_name_str.replace(" ", "") + "full_movie"
        st.text(names[1])
        st.image(posters[1])
        #print(youtube_url)
        st.write("**Movie** [link](%s)" % youtube_url)
    with col3:
        movie_name_str = " ".join(names[2])
        youtube_url = f"https://www.youtube.com/results?search_query=" + movie_name_str.replace(" ", "") + "full_movie"
        st.text(names[2])
        st.image(posters[2])
        print(youtube_url)
        st.write("**Movie** [link](%s)" % youtube_url)
    with col4:
        movie_name_str = " ".join(names[3])
        youtube_url = f"https://www.youtube.com/results?search_query=" + movie_name_str.replace(" ", "") + "full_movie"
        st.text(names[3])
        st.image(posters[3])
        #print(youtube_url)
        st.write("**Movie** [link](%s)" % youtube_url)
    with col5:
        movie_name_str = " ".join(names[4])
        youtube_url = f"https://www.youtube.com/results?search_query=" + movie_name_str.replace(" ", "") + "full_movie"
        st.text(names[4])
        st.image(posters[4])
        #print(youtube_url)
        st.write("**Movie** [link](%s)" % youtube_url)
    with col6:
        movie_name_str = " ".join(names[5])
        youtube_url = f"https://www.youtube.com/results?search_query=" + movie_name_str.replace(" ", "") + "full_movie"
        st.text(names[5])
        st.image(posters[5])
        #print(youtube_url)
        st.write("**Movie** [link](%s)" % youtube_url)

