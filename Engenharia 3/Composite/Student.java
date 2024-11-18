public class Student implements SchoolMember {
    private String name;
    public Student(String name){
        this.name = name;
    }
    public int count(){
        return 1;
    }
}
