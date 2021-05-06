class Music:  # defining the parent class
    total_songs = 100


class Rock(Music):  # defining the child class
    total_songs = 30

    def display(self):
        print(self.total_songs)

        print(super().total_songs)


genre = Rock()  
genre.display()