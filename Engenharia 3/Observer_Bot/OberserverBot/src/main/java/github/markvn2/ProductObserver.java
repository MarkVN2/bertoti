package github.markvn2;

import com.pengrad.telegrambot.TelegramBot;
import com.pengrad.telegrambot.request.SendMessage;
import com.pengrad.telegrambot.response.SendResponse;

public class ProductObserver implements MessageObserver {
    private String name;
    private String status = "unknown";
    public ProductObserver(String name){
        this.name = name;
        this.status = "new";
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void onMessageReceived(String chatId, String message, TelegramBot bot) {
        System.out.println("Received message: " + message + " from chat: " + chatId);
        Utils.sendMessage(chatId, "Type : Product | Name : " + name + " | Status: " + status, bot);
    }

    public void updateStatus(String newStatus, String chatId, TelegramBot bot) {
        if (!newStatus.equals(this.status)) {
            this.status = newStatus;
            Utils.sendMessage(chatId, "Product " + name + " status updated to: " + newStatus, bot);
        }
    }
}
