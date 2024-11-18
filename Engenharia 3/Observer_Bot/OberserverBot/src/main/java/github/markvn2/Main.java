package github.markvn2;

public class Main {
    public static void main(String[] args) {
        String token = "7346345972:AAGQleGzpcU0QQRZqVvgIJ3V-_aTNGJetEo";

        ChatBot bot = new ChatBot(token);

        ProductObserver product = new ProductObserver("Shampoo");
        bot.addObserver(product);
        bot.addObserver(new ServiceObserver("Lavagem"));
        bot.pollUpdates();

    }
}