public class SchoolController {
    private Teacher model;
    private SchoolView view;
    private TeachingStrategy strategy;

    public SchoolController(Teacher model, SchoolView view) {
        this.model = model;
        this.view = view;
    }

    public void setTeachingStrategy(TeachingStrategy strategy) {
        this.strategy = strategy;
    }

    public void updateView() {
        view.printTeacherDetails(model.getName(), model.count());
    }

    public void executeTeachingStrategy() {
        if (strategy != null) {
            strategy.teach();
        } else {
            System.out.println("No teaching strategy set.");
        }
    }
}