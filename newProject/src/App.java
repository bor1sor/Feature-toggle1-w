class Person {
    private String name;
    private int age;

    Person(String n, int a) {
        name = n;
        age = a;

    }

    void showDetails() {
        System.out.println(name + ", возраст: " + age);
    }
}

public class App {
    public static void main(String[] args) {
        Person p1 = new Person("Петя Петечков", 27);
        Person p2 = new Person("Анна Анова", 33);

        p1.showDetails();
        p2.showDetails();

    }

}
