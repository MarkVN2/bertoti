package github.markvn2;

import com.pengrad.telegrambot.TelegramBot;

public interface MessageObserver {
    String getName();
    void onMessageReceived(String chatId, String message , TelegramBot bot);

}
