int[] rows = new int[128];
int[] cols = new int[8];

void setup() {
  for (int i = 0; i < rows.length; i++) {
    rows[i] = i;
  }
  for (int i = 0; i < cols.length; i++) {
    cols[i] = i;
  }
  String[] input = loadStrings("test.txt");
  int[] id = new int[input.length];
  for (int i = 0; i < input.length; i++) {
    String rseq = input[i].substring(0, 7);
    String cseq = input[i].substring(7, 10);
    int row = findRow(rseq); 
    int col = findCol(cseq);
    id[i] = row * 8 + col;
    println(id[i]);
 }
  
  int greatest = 0;
  for (int i = 0; i < id.length; i++) {
    // println(id[i]);
    if (id[i] > greatest) greatest = id[i];
  }
  // println(greatest);
}

int findRow(String ins) {
  int low = 0;
  int high = 127;
  String[] seq = ins.split("");
  for (int i = 0; i < seq.length; i++) {
    int mid = low + ((high - low) /2);
    if (seq[i].equals("B")) {
      low = mid + 1;
    }
    else if (seq[i].equals("F")) {
      high = mid;
    }
  }
  return (low + ((high - low) / 2));
}

int findCol(String ins) {
  int low = 0;
  int high = 7;
  String[] seq = ins.split("");
  int mid = 0;
  for(String l : seq) {
    mid = low + ((high - low) / 2);
    if (l.equals("R")) {
      low = mid + 1;
    }
    else {
      high = mid;
    }
  }
  return floor(low + ((high - low) / 2));
}

//int findCol(int[] array, String ins) {
//  int len = array.length;
//  int low = 0;
//  int high = len - 1;
//  String[] seq = ins.split("");
//  int answer = 0;
//  for (int i = 0; i < seq.length; i++) {
//    int mid = low + ((high - low) /2);
//    int current = array[mid];
//    if (seq[i].equals("R")) {
//      low = mid + 1;
//    }
//    else if (seq[i].equals("L")) {
//      high = mid;
//    }
//    answer = current;
//  }
//  return answer;
//}

int binarySearch(int[] array, int key){
  int length = array.length;
  int low = 0;
  int high = length - 1;
  while(low < high){
      int mid = low + ((high - low) / 2);
      int current = array[mid];
      if(current == key){
          return array[mid];
      }
      else if(current < key){
          low = mid + 1;
      }
      else{
          high = mid;
      }
  }
  return array[low];
}

long fact(long n) {
  if (n <= 1) return 1;
  else return n * fact(n - 1);
}
