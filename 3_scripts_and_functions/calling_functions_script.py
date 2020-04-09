import example_source

summed_numbers = example_source.my_sum_function(42, 3.14)
substracted_numbers = example_source.my_substraction_function(42, 3.14)
substracted_reverse_numbers = example_source.my_substraction_function(42, 3.14, reverse=True)

print('The result of adding my favorite numbers is ' + str(summed_numbers) + '. Their substraction equals ' + str(substracted_numbers) + ', but some people prefer to see them substracted in a reverse order, which results in ' + str(substracted_reverse_numbers) + '. I don\'t like that people, I think they are plain ' + example_source.random_insult())