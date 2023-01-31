def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name' : 'Grace Kendall',
        'student_id' : '10116872',
        'pizza_toppings' : ['pepperoni', 'bacon', 'sausage'],
        'movie_list' : [ 
            {
                'title' : 'lord of the rings',
                'genre' : 'fantasy fiction'
            },
            {
                'title' : 'harry potter and the goblet of fire',
                'genre' : 'fantasy, adventure'
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {
        'title' : 'nightmare before christmas',
        'genre' : 'animated'
    }
    about_me['movie_list'].append(new_movie)

    
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    first_name = about_me['full_name'].split()[0]
    print(f"My name is {about_me['full_name']}, but you can call me Queen {first_name}.")
    print(f"My student ID is {about_me['student_id']}.")
    return 
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, pizza_toppings):
    about_me['pizza_toppings'].extend(pizza_toppings)
    about_me['pizza_toppings'].sort()
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('\nMy favourite pizza toppings are:')
    for p in about_me['pizza_toppings']:
        print(f'- {p}'.upper())
    print('\nMy favourite pizza toppings are:')
    add_pizza_toppings(about_me, ('chicken', 'more bacon'))
    for p in about_me['pizza_toppings']:
        print(f'- {p}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):

    print('\nI like to watch ', end='')
    movie_genres = [g['genre']for g in about_me['movie_list']]
    movie_csl = ', '.join(movie_genres)
    print(f'{movie_csl} movies.')
       
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):

    print('\nSome of my favourite movies are ', end='')
    movie_titles = [t ['title'].title() for t in movie_list['movie_list']]
    movie_cls = ', '.join(movie_titles)
    print(f'{movie_cls}!')

    return
    
if __name__ == '__main__':
    main()