package github.markvn2;

import com.pengrad.telegrambot.TelegramBot;
import com.pengrad.telegrambot.request.SendMessage;
import com.pengrad.telegrambot.response.SendResponse;

public class Utils {
    public static void sendMessage(String chatId, String text, TelegramBot bot) {
        SendMessage request = new SendMessage(chatId, text);
        SendResponse response = bot.execute(request);

        // Check if the message was successfully sent
        if (response.isOk()) {
            System.out.println("Message sent successfully to chat: " + chatId);
        } else {
            System.err.println("Failed to send message: " + response.description());
        }
    }
}
