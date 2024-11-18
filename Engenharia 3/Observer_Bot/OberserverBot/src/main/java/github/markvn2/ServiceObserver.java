package github.markvn2;

import com.pengrad.telegrambot.TelegramBot;

public class ServiceObserver implements MessageObserver {
    private String name;
    private String status = "unknown";
    public ServiceObserver(String name){
        this.name = name;
        this.status = "new";
    }
    @Override
    public void onMessageReceived(String chatId, String message, TelegramBot bot) {
        System.out.println("Received message: " + message + " from chat: " + chatId);
        Utils.sendMessage(chatId, "Type : Service | Name : " + name + " | Status: " + status, bot);
    }
    @Override
    public String getName() {
        return name;
    }

    public void updateStatus(String newStatus, String chatId, TelegramBot bot) {
        if (!newStatus.equals(this.status)) {
            this.status = newStatus;
            Utils.sendMessage(chatId, "Service " + name + " status updated to: " + newStatus, bot);
        }
    }
}