package github.markvn2.strategy;

public class Calculator {
    private CalculationMethod calculationMethod;

    public Calculator(CalculationMethod calculationMethod) {
        this.calculationMethod = calculationMethod;
    }
    public void setCalculationMethod(CalculationMethod calculationMethod) {
        this.calculationMethod = calculationMethod;
    }

    public Float calculate(int a, int b) {
        return calculationMethod.calculate(a, b);
    }
}
