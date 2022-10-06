import java.net.*;
import java.util.*;
import java.io.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class servidorOitoConexoes {

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(8);
        try (ServerSocket servidor = new ServerSocket(60000)) {
            System.out.println("Servidor de oito conexões Rodando...");
            for (int i = 0; i < 8; i++) {
                Socket s = servidor.accept();
                Worker worker = new Worker(s);
                executor.execute(worker);
                System.out.println("Conexão atual:" + i);
            }
            while (!executor.isTerminated()) {
            }
            executor.shutdown();
            System.out.println("Finished all threads");
        } catch (IOException e) {
            e.printStackTrace();
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
                s.close();
            } while (!palavra.equals("fim"));
            System.out.println("Thread morreu");

        } catch (Exception e) {
        }
    }

}
