import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class clienteInvertido {
    public static void main(String ars[]) throws Exception {
        try (Scanner myObj = new Scanner(System.in)) {
            System.out.println("Digite um nome para ser invertido ou frase: ");
            String name = myObj.nextLine();
            Socket s = new Socket("localhost", 60000);
            PrintWriter saida = new PrintWriter(s.getOutputStream(), true);
            saida.println(name);
            Scanner entrada = new Scanner(s.getInputStream());
            String palavraModificada = entrada.nextLine();
            System.out.println(palavraModificada);
            s.close();
        }
    }
}
