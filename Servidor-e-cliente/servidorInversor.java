import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class servidorInversor {
    /**
     * @param args
     * @throws Exception
     */
    public static void main(String args[]) throws Exception {
        Scanner entrada = null;
        PrintWriter saida = null;
        try (ServerSocket servidor = new ServerSocket(60000)) {
            System.out.println("Servidor rodando...");
            while (true) {
                Socket s = servidor.accept();
                System.out.println(s);
                entrada = new Scanner(s.getInputStream());
                String palavra = entrada.nextLine();
                String palavraModificada = new StringBuilder(palavra).reverse().toString();
                saida = new PrintWriter(s.getOutputStream(), true);
                saida.println(palavraModificada);
                s.close();
            }
        }
    }
}