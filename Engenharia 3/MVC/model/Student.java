public class Student implements SchoolMember {
    private String name;

    public Student(String name) {
        this.name = name;
    }

    @Override
    public int count() {
        return 1;
    }

    public String getName() {
        return name;
    }
}