void setup() {
  String[] data = loadStrings("data.txt");
  int x = 0;
  int xoff = 3;
  int trees = 0;
  for (String line : data) {
    line = expand(line, xoff * data.length);
    String block = Character.toString(line.charAt(x));
    if (block.equals("#")) {
      trees++;
    }
    x += xoff;
  }
  println(trees);
}

String expand(String string, int expander) {
  String temp = string;
  for (int i = 1; i < expander; i++) {
    temp += string;
  }
  return temp;
}
