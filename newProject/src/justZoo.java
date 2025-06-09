interface Animal {
    default void sayHello() {
        System.out.println("Привет");
    }
}

class Dog implements Animal {
    public void bark() {
        System.out.println("Гав-гав!");
    }
}

class Cat implements Animal {
    public void meow() {
        System.out.println("Мяу!");
    }
}

public class justZoo {

    public static void main(String[] args) {
        Dog dog = new Dog();
        Cat cat = new Cat();
        dog.sayHello(); // Привет
        dog.bark(); // Гав-гав!
        cat.sayHello(); // Привет
        cat.meow(); // Мяу!
    }

}
