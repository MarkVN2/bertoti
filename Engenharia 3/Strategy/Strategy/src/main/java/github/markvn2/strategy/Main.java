package github.markvn2.strategy;

class Main {
    public static void main (String[] args){
        Calculator calculator = new Calculator(new Addition());
        System.out.println(calculator.calculate(5, 3));
        calculator.setCalculationMethod(new Subtraction());
        System.out.println(calculator.calculate(5, 3));
        calculator.setCalculationMethod(new Multiplication());
        System.out.println(calculator.calculate(5, 3));
    }
}