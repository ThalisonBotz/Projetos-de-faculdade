public class main {
    public static void main(String[] args) throws InterruptedException{
        soma soma = new soma();

        Thread t = new Thread(new tarefa(soma));
        Thread t2 = new Thread(new tarefa(soma));

        t.start();
        t2.start();

        t.join();
        t2.join();

        System.out.println(soma.i);
    }
    
}
