package github.markvn2.strategy;

public class Addition implements CalculationMethod{
    @Override
    public Float calculate(int a, int b) {
        return (float) (a + b);
    }
}
