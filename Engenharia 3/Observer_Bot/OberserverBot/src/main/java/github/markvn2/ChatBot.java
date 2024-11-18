package github.markvn2;

import com.pengrad.telegrambot.TelegramBot;
import com.pengrad.telegrambot.model.Update;
import com.pengrad.telegrambot.request.GetUpdates;
import com.pengrad.telegrambot.request.SendMessage;
import com.pengrad.telegrambot.response.GetUpdatesResponse;

import java.util.ArrayList;
import java.util.List;

public class ChatBot {
    private TelegramBot bot;
    private List<MessageObserver> observers = new ArrayList<>();
    private int lastUpdateId = 0;

    public ChatBot(String botToken) {
        this.bot = new TelegramBot(botToken);
    }

    public void addObserver(MessageObserver observer) {
        observers.add(observer);
    }

    public void removeObserver(MessageObserver observer) {
        observers.remove(observer);
    }

    private void notifyObservers(String chatId, String message) {
        for (MessageObserver observer : observers) {
            observer.onMessageReceived(chatId, message, bot);
        }
    }

    private void handleCommand(String chatId, String command) {
        if (command.equalsIgnoreCase("/list")) {
            listObserverTypes(chatId);
        } else if (command.equalsIgnoreCase("/observed")) {
            listObservers(chatId);
        } else if (command.startsWith("/add ")) {
            String[] parts = command.substring(5).trim().split(" ", 2);
            if (parts.length == 2) {
                String observerType = parts[0].trim();
                String name = parts[1].trim();
                addObserverByType(chatId, observerType, name);
            } else {
                bot.execute(new SendMessage(chatId, "Invalid command format. Use /add <observerType> <name>"));
            }
        } else if (command.startsWith("/status ")) {
            String[] parts = command.substring(8).trim().split(" ", 2);
            if (parts.length == 2) {
                int observerId = Integer.parseInt(parts[0].trim());
                String newStatus = parts[1].trim();
                updateServiceStatus(chatId, observerId, newStatus);
            } else {
                bot.execute(new SendMessage(chatId, "Invalid command format. Use /status <observerId> <newStatus>"));
            }
        } else if (command.startsWith("/remove ")) {
            int observerId = Integer.parseInt(command.substring(8).trim());
            removeObserverById(chatId, observerId);
        } else {
            notifyObservers(chatId, command);
        }
    }

    private void listObserverTypes(String chatId) {
        String message = "Available to add:\n1. Service\n2. Product";
        bot.execute(new SendMessage(chatId, message));
    }

    private void listObservers(String chatId) {
        StringBuilder message = new StringBuilder("Current observers:\n");
        for (int i = 0; i < observers.size(); i++) {
            MessageObserver observer = observers.get(i);
            message.append(i).append(". ").append(observer.getClass().getSimpleName())
                    .append(" (Name: ").append(observer.getName()).append(")\n");
        }
        bot.execute(new SendMessage(chatId, message.toString()));
    }

    private void addObserverByType(String chatId, String observerType, String name) {
        MessageObserver observer = null;
        switch (observerType.toLowerCase()) {
            case "service":
                observer = new ServiceObserver(name);
                break;
            case "product":
                observer = new ProductObserver(name);
                break;
            default:
                bot.execute(new SendMessage(chatId, "Unknown observer type: " + observerType));
                return;
        }
        addObserver(observer);
        bot.execute(new SendMessage(chatId, observerType + " " + name + " added successfully."));
    }

    private void updateServiceStatus(String chatId, int observerId, String newStatus) {
        if (observerId >= 0 && observerId < observers.size()) {
            MessageObserver observer = observers.get(observerId);
            if (observer instanceof ServiceObserver) {
                ((ServiceObserver) observer).updateStatus(newStatus, chatId, bot);
            } else if (observer instanceof ProductObserver) {
                ((ProductObserver) observer).updateStatus(newStatus, chatId, bot);
            }
            notifyObservers(chatId, "Status updated to: " + newStatus);
        } else {
            bot.execute(new SendMessage(chatId, "Invalid observer ID: " + observerId));
        }
    }

    private void removeObserverById(String chatId, int observerId) {
        if (observerId >= 0 && observerId < observers.size()) {
            MessageObserver observer = observers.remove(observerId);
            bot.execute(new SendMessage(chatId, "Removed observer: " + observer.getName()));
        } else {
            bot.execute(new SendMessage(chatId, "Invalid observer ID: " + observerId));
        }
    }

    public void pollUpdates() {
        while (true) {
            GetUpdates getUpdates = new GetUpdates()
                    .offset(lastUpdateId + 1)
                    .limit(100)
                    .timeout(10);

            GetUpdatesResponse updatesResponse = bot.execute(getUpdates);
            List<Update> updates = updatesResponse.updates();

            for (Update update : updates) {
                lastUpdateId = update.updateId();
                String chatId = String.valueOf(update.message().chat().id());
                String message = update.message().text();
                if (message.startsWith("/")) {
                    handleCommand(chatId, message);
                } else {
                    notifyObservers(chatId, message);
                }
            }

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }
}