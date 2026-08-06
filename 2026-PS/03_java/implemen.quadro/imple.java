public class imple {
    public static float calcularMedia(float[] numeros) {
        float S = 0;
        for (float n : numeros) {
            S += n;
        }
        return S / numeros.length;
    }

    public static void main(String[] args) {
        float[] numeros = {8.5f, 3.2f, 10.0f, 5.7f, 12.4f};
        float media = calcularMedia(numeros);
        System.out.printf("A média é: %.2f%\n", media);
    }
}