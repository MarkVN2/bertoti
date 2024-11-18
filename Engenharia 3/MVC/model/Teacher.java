import java.util.ArrayList;
import java.util.List;

public class Teacher implements SchoolMember {
    private String name;
    private List<SchoolMember> students;

    public Teacher(String name) {
        this.name = name;
        this.students = new ArrayList<>();
    }

    public void addStudent(SchoolMember student) {
        students.add(student);
    }

    @Override
    public int count() {
        int count = 0;
        for (SchoolMember s : students) {
            count += s.count();
        }
        return count;
    }

    public String getName() {
        return name;
    }

    public List<SchoolMember> getStudents() {
        return students;
    }
}