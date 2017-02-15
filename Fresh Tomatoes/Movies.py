import webbrowser
import fresh_tomatoes

class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



Days_of_Summer = Movie('500 Days of Summer', 'Not a Love Story',
                       'https://images-na.ssl-images-amazon.com/images/I/61%2BeskJahYL.jpg',
                       'https://www.youtube.com/watch?v=PsD0NpFSADM')

Gangster_Squad = Movie('Gangster Squad', 'A group of vigilantes form to fight of gang crime in their city',
                       'http://cdn.collider.com/wp-content/uploads/gangster-squad-poster-emma-stone.jpg',
                       'https://www.youtube.com/watch?v=qilrVR0miPU')

Silver_Linings_Playbook = Movie('Silver Linings Playbook', 'A Movie About Mental Health and Love',
                                'http://cdn.movieweb.com/img.site/PH5xI87Iye5d85_1_l.jpg',
                                'https://www.youtube.com/watch?v=3ZLKfYQ_Wyo')

movies = [Days_of_Summer, Gangster_Squad, Silver_Linings_Playbook]

fresh_tomatoes.open_movies_page(movies)

