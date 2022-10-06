import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class servidorInversorComThread {
    public static void main(String args[]) throws Exception {
        try (ServerSocket servidor = new ServerSocket(60000)) {
            System.out.println("Servidor Inversor Com Thread rodando...");
            while (true) {
                Socket s = servidor.accept();
                Worker w = new Worker(s);
                w.start();
            }
        }
    }
}

class Worker extends Thread {
    private Socket s;

    public Worker(Socket s) {
        this.s = s;
    }

    public void run() {
        try {
            Scanner entrada = new Scanner(s.getInputStream());
            PrintWriter saida = new PrintWriter(s.getOutputStream(), true);
            String palavra;
            do {
                palavra = entrada.nextLine();
                String palavraModificada = new StringBuilder(palavra).reverse().toString();
                saida.println(palavraModificada);
            } while (!palavra.equals("fim"));
            s.close();

        } catch (Exception e) {
        }
    }

}
