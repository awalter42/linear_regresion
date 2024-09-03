from train import Model
from predict import estimatePrice


if __name__ == '__main__':
	models = {}
	nb_trained = 0

	print("WARNING: if you want to show the data plot, remember to export QT_QPA_PLATFORM=wayland\n\n")

	while True:
		print ("""What do you want to do?
			1 - Create and train a model
			2 - Train a model for more iterations
			3 - Use a model to predict a value
			4 - Get the plot of a model
			5 - Get the values of a model
			6 - Exit the program
			""")
		action = int(input('> '))

		match action:
			case 1:
				new_model = Model()
				if type(new_model) != Model:
					print('There has been a problem with the training\n')
					continue
				models[nb_trained] = new_model
				nb_trained += 1

			case 2:
				keys = list(models.keys())
				keys.sort()
				if keys == []:
					print('A model has yet to be created')
					continue

				print('Please select a model: \n')
				for k in keys:
					m = models[k]
					print(f'\t\t{k} : trained on {m.getFile()} for {m.getNbItter()} iterations')

				index = int(input('\n> '))
				if index not in keys:
					print('Next time, please choose an index that match an existing model')
					continue

				itter = int(input('Number of iterations: '))
				models[index].loopTrain(itter)

			case 3:
				keys = list(models.keys())
				keys.sort()
				if keys == []:
					print('A model has yet to be created')
					continue

				print('Please select a model: \n')
				for k in keys:
					m = models[k]
					print(f'\t\t{k} : trained on {m.getFile()} for {m.getNbItter()} iterations')

				index = int(input('\n> '))
				if index not in keys:
					print('Next time, please choose an index that match an existing model')
					continue

				mileage = int(input('mileage of the car: '))
				if mileage < 0:
					print ("A mileage cannot be negative")
					continue
				t0 = models[index].getTheta0()
				t1 = models[index].getTheta1()
				est = estimatePrice(mileage, t0, t1)
				print(f'\nThe price is estimated to be {est} units (no intel on the currency)\n')


			case 4:
				keys = list(models.keys())
				keys.sort()
				if keys == []:
					print('A model has yet to be created')
					continue

				print('Please select a model: \n')
				for k in keys:
					m = models[k]
					print(f'\t\t{k} : trained on {m.getFile()} for {m.getNbItter()} iterations')

				index = int(input('\n> '))
				if index not in keys:
					print('Next time, please choose an index that match an existing model')
					continue

				function = input('Plot of function line (Y/N): ').upper()
				match function:
					case 'Y':
						models[index].showData(True)
					case 'N':
						models[index].showData(False)
					case _:
						print('Please respect prompt\n')
						continue


			case 5:
				keys = list(models.keys())
				keys.sort()
				if keys == []:
					print('A model has yet to be created')
					continue

				print('Please select a model: \n')
				for k in keys:
					m = models[k]
					print(f'\t\t{k} : trained on {m.getFile()} for {m.getNbItter()} iterations')

				index = int(input('\n> '))
				if index not in keys:
					print('Next time, please choose an index that match an existing model')
					continue
				print(models[index])

			case 6:
				exit()

			case _:
				print('Make sure to use a number that is valid')
