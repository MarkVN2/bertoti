class Composite {
    public static void main (String[] args){
        Teacher m1 = new Teacher("Michael");
        Teacher m2 = new Teacher("Halmilton");
        Teacher m3 = new Teacher("Amanda");

        Student s1 = new Student("Avery");
        Student s2 = new Student("Laura");
        Student s3 = new Student("Bella");

        Student s4 = new Student("Cindy");
        Student s6 = new Student("Eva");
        Student s5 = new Student("Diana");

        m3.AddStudent(s1);
        m3.addStudent(s2);
        m3.addStudent(s3);

        System.out.println(m3.name + " lessiona " + m3.count() + " na escola");

        m2.addStudent(s4);
        m2.addStudent(s5);
        m2.addStudent(m3);

        System.out.println(m2.name + " lessiona " + m2.count() + " na escola");

        m1.addStudent(s6);
        m1.addStudent(m2);

        System.out.println(m1.name + " lessiona " + m1.count() + " na escola");
    }
}