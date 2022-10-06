public class tarefa implements Runnable {
    private soma armazena;

    public tarefa(soma armazena){
        this.armazena = armazena;
    }
    @Override
    public void run(){
        for(int i=0; i<50000; i++){
            this.armazena.somar();
        }
    }
}
