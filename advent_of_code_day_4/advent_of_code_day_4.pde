void setup() {
  String input = string(loadStrings("input.txt"), "\n");
  String[] data = input.split("\n\n");
  String[] stuff = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
  String cid = "cid";
  int count = 0;
  for (String obj : data) {
    if (check(obj, stuff)) {
      count++;
    }
  }
  println(count);
}

String string(String[] arr, String sep) {
  String str = "";
  for (String s : arr) {
    str = str + sep + s;
  }
  return str;
}

boolean check(String pass, String[] par) {
  String[] args = pass.split(" |\n");
  ArrayList<String> toCheck = new ArrayList<String>();  
  for (int i = 0; i < args.length; i++) {
    toCheck.add(args[i].split(":")[0]);
  }
  int count1 = 0;
  for (String p : par) {
    for (String t : toCheck) {
      if (p.equals(t)) {
        count1++;
      }
    }
  }
  boolean cond1 = count1 == par.length ? true : false;
  //if (cond1) {
    
  //}
  return cond1;
}

//ArrayList<String> args = new ArrayList<String>();
  //for (String ar : arguments) {
  //  String[] arr = ar.split("\n");
  //  for (String e : arr) {
  //    args.add(e);
  //  }
  //}
