class Person {

    private String name;

    public Person(String name) {

        this.name = name;

    }

    public void greeting() {

        System.out.println("Hello, my name is " + name + "!");

    }

}

public class App1 {

    public static void main(String[] args) {
        Person person = new Person("Matthew");
        person.greeting();
    }

}