void setup() {
  String[] data = loadStrings("data.txt");
  int[] trees = {0, 0, 0, 0, 0};
  int[] rights = {1, 3, 5, 7, 1};
  int[] downs =  {1, 1, 1, 1, 2};
  for (int j = 0; j < rights.length; j++) {
    int x = 0;
    for (int i = 0; i < data.length; i += downs[j]) {
      String line = data[i];
      line = expand(line, rights[j] * data.length);
      String block = Character.toString(line.charAt(x));
      if (block.equals("#")) {
        trees[j]++;
      }
      x += rights[j];
    }
    println(trees[j]);
  }
  println(mult(trees));
}

String expand(String string, int expander) {
  String temp = string;
  for (int i = 1; i < expander; i++) {
    temp += string;
  }
  return temp;
}

double mult(int[] numbers) {
  double result = 1;
  for (int n : numbers) {
    result = result * n;
  }
  return result;
}

/*
array of answers:
  [0] 77
  [1] 218
  [2] 65
  [3] 82
  [4] 43
the answer:
  3847183340
*/
