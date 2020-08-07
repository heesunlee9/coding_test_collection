import java.util.LinkedList;
import java.util.List;

class animalShelter {
	
	List animals = new LinkedList();



	public boolean enqueue(Animal animal) {

		return animals.add(animal);

	}



	public Animal dequeueAny() {

		return animals.remove();

	}



	public Dog dequeueDog() {

		return dequeue(dog);

	}



	public Cat dequeueCat() {

		return dequeue(dog);

	}

}
