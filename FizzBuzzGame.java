public class FizzBuzzGame {
    private final String[] players;
    private final int fizzDiv;
    private final int buzzDiv;
    private final int maxNumber;
    private int currentNumber = 1;
    private int currentPlayer = 0;
    private boolean finished = false;

    public FizzBuzzGame(String[] players, int fizzDiv, int buzzDiv, int maxNumber) {
        this.players = players;
        this.fizzDiv = fizzDiv;
        this.buzzDiv = buzzDiv;
        this.maxNumber = maxNumber;
    }

    private synchronized String getFizzBuzzValue(int n) {
        if (n % fizzDiv == 0 && n % buzzDiv == 0) return "¡fizzbuzz!";
        if (n % fizzDiv == 0) return "¡fizz!";
        if (n % buzzDiv == 0) return "¡buzz!";
        return Integer.toString(n);
    }

    private synchronized void playTurn(int playerIndex) throws InterruptedException {
        while (!finished) {
            while (playerIndex != currentPlayer && !finished) wait();

            if (finished) break;

            System.out.println(players[playerIndex] + " says " + getFizzBuzzValue(currentNumber));
            currentNumber++;

            if (currentNumber > maxNumber) {
                finished = true;
                notifyAll();
                break;
            }

            currentPlayer = (currentPlayer + 1) % players.length;
            notifyAll();
            Thread.sleep(100);
        }
    }

    public void startGame() {
        for (int i = 0; i < players.length; i++) {
            final int index = i;
            new Thread(() -> {
                try {
                    playTurn(index);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }).start();
        }
    }

    public static void main(String[] args) {
        // First Option
        new FizzBuzzGame(new String[]{"Abdul", "Bart", "Claudia", "Divya"}, 3, 5, 20).startGame();

        // Second Option
        new FizzBuzzGame(new String[]{"Matthieu", "Sofía", "Nico"}, 2, 7, 15).startGame();
    }
}
