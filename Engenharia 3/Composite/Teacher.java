import java.util.ArrayList;
import java.util.List;

public class Teacher implements SchoolMember {
    public String name;
    private List<SchoolMember> students;

    public Teacher(String name) {
        this.name = name;
        students = new ArrayList<SchoolMember>();
    }

    public void addStudent(SchoolMember student) {
        students.add(student);
    }

    public int count() {
        int count = 0;
        for (SchoolMember s : students) {
            count += s.count();
        }
        return count;
    }
}