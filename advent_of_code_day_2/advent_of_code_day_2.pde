String[] data;
int total = 0;

void setup() {
  data = loadStrings("data.txt");
  for (String s : data) {
    String[] cont = s.split(" ");
    String mm = cont[0];
    String letter = cont[1].split("")[0];
    int min = int(mm.split("-")[0]);
    int max = int(mm.split("-")[1]);
    String pass = cont[2];
    min--;
    max--;
    String first = Character.toString(pass.charAt(min));
    String second = Character.toString(pass.charAt(max));
    if ((first.equals(letter) && !second.equals(letter)) || (!first.equals(letter) && second.equals(letter)))
      total++;
    }
  println(total);
}
