import spacy

nlp = spacy.load('en_core_web_md')


def watch_next(description):
    with open("movies.txt", "r") as movies_file:
        similarity_list = []
        description = nlp(description)

        movie_list = movies_file.readlines()
        movies_file.seek(0)

        # appends similarity percentages to similarity list
        for movie in movies_file:
            similarity = nlp(movie).similarity(description)
            similarity_list.append(similarity)

        # finds max value from similarity list
        max_sim = max(similarity_list)

        # finds index of max_sim in similarity list
        max_sim_index = similarity_list.index(max_sim)
        print(max_sim_index)

        # prints movie with same index as max sim
        print(movie_list[max_sim_index])

hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

watch_next(hulk)