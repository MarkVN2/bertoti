package github.markvn2.strategy;

public class Subtraction implements CalculationMethod{
    @Override
    public Float calculate(int a, int b) {
        return (float) (a - b);
    }
}
