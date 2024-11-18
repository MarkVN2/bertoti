public class Main {
    public static void main(String[] args) {
        Teacher teacher = new Teacher("Michael");
        teacher.addStudent(new Student("Avery"));
        teacher.addStudent(new Student("Laura"));

        SchoolView view = new SchoolView();
        SchoolController controller = new SchoolController(teacher, view);

        controller.updateView();

        controller.setTeachingStrategy(new LectureStrategy());
        controller.executeTeachingStrategy();

        controller.setTeachingStrategy(new LabStrategy());
        controller.executeTeachingStrategy();
    }
}