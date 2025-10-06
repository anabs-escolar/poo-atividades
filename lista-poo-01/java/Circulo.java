public class Circulo {
    double raio;

    double area() {
      double area = 3.14 * (raio * raio);
      return area;
    }

    double diametro() {
      double diametro = 2 * raio;
      return diametro;
    }

    // Teste da classe Circulo
    public static void main(String[] args) {
        Circulo c1 = new Circulo();
        c1.raio = 5.0;

        System.out.println("Raio: " + c1.raio);
        System.out.println("Área: " + c1.area());
        System.out.println("Diâmetro: " + c1.diametro());
    }
}

