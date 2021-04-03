String[] stuff = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};

void setup() {
  String input = string(loadStrings("test.txt"), "\n");
  String[] data = input.split("\n\n");
  String cid = "cid";
  int count = 0;
  for (String obj : data) {
    if (check(obj)) {
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

boolean check(String str) {
  String[] tokens = str.split(" |\n");
  ArrayList<String> keys = new ArrayList<String>();
  ArrayList<String> validKeys = new ArrayList<String>();
  ArrayList<String> values = new ArrayList<String>();
  ArrayList<String> validValues = new ArrayList<String>();
  for (String token : tokens) {
    String[] pair = token.split(":");
    if (pair.length < 2) {println(token); continue;}
    keys.add(pair[0]);
    values.add(pair[1]);
  }
  int[] successes = new int[keys.size()];
  for (int i = 0; i < keys.size(); i++) {
    String key = keys.get(i);
    for (int j = 0; j < stuff.length; j++) {
      String toCompare = stuff[j];
      if (key.equals(toCompare)) {
      validKeys.add(key + toCompare);
    }
    }
  }
  boolean cond = validKeys.size() >= tokens.length-1;
  if (!cond) return false;
   for (int i = 0; i < stuff.length; i++) {
     int o = 0;
     for (int j = 0; j < stuff.length; j++) {
       if (keys.get(i).equals(stuff[j])) {
         o = j;
         break;
       }
     }
     String v = values.get(o);
     //println("i", i);
     //println("value: ", v);
     if (o == 0) {
       int byr = int(v);
       if (bet(byr, 1920, 2002)) {
         validValues.add(v);
       }
     } else if (o == 1) {
       int iyr = int(v);
       if(bet(iyr, 2010, 2020)) {
         validValues.add(v);
         successes[o]++;
       }
     } else if (o == 2) {
       int eyr = int(v);
       if (bet(eyr, 2020, 2030)) {
         validValues.add(v);
         successes[o]++;
       }
     } else if (o == 3 && v.length() > 2) {
       int hgt = int(v.substring(0, v.length()-2));
       String unit = v.substring(v.length()-2);
       if (unit.equals("cm")) {
         if (bet(hgt, 150, 193)) {
           validValues.add(v);
           successes[o]++;
         }
       } else if (unit.equals("in")) {
          if (bet(hgt, 59, 76)) {
             validValues.add(v);
             successes[o]++;
           } 
       }
     } else if (o == 4) {
       String hcl = v.substring(1);
       if (v.substring(0, 1).equals("#") && hcl.length() == 6) {
         if (isHex(hcl)) {
           validValues.add(v);
           successes[o]++;
         }
       }
     } else if (o == 5) {
       String[] ecls = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
       String ecl = v;
       for (String ec : ecls) {
         if (ec.equals(ecl)) {
           validValues.add(v);
           successes[o]++;
           break;
         }
       }
     } else if (o == 6) {
       String pid = v;
       if (pid.length() < 9) {
         validValues.add(v);
         successes[o]++;
          println(pid);
       }
     }
   }
   //println(successes);
   return validValues.size() >= stuff.length-1;
  }

//boolean check(String pass, String[] par) {
//  String[] args = pass.split(" |\n");
//  ArrayList<String> toCheck = new ArrayList<String>();
//  ArrayList<String> toCheckv = new ArrayList<String>();
//  for (int i = 0; i < args.length; i++) {
//    String[] sargs = args[i].split(":");
//    toCheck.add(sargs[0]);
//    if (sargs.length > 1) {
//      toCheckv.add(sargs[1]);
//    } else {
//      return false;
//    }
//  }
//  int count1 = 0;
//  int[] order = new int[par.length];
//  for (int i = 0; i < par.length; i++) {
//    for (int j = 0; j < toCheck.size(); j++) {
//      String t = toCheck.get(j);
//      if (par[i].equals(t)) {
//        count1++;
//        order[i] = j;
//      }
//    }
//  }
//  return true;
//}
  
boolean bet(int x, int min, int max) {
  if (x >= min && x <= max) {
    return true;
  }
  return false;
}

public static boolean isHex(String text) {
    if(text.length() < 1)
        throw new IllegalArgumentException("Text cannot be empty.");

    char[] hexDigits = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F' };

    for (char symbol : text.toCharArray()) {
        boolean found = false;
        for (char hexDigit : hexDigits) {
            if (symbol == hexDigit) {
                found = true;
                break;
            }
        }
        if(!found)
            return false;
    }
    return true;
}
//ArrayList<String> args = new ArrayList<String>();
  //for (String ar : arguments) {
  //  String[] arr = ar.split("\n");
  //  for (String e : arr) {
  //    args.add(e);
  //  }
  //}
  
  
  //boolean cond1 = count1 == par.length ? true : false;
  //int count2 = 0;
  //if (cond1) {
  //   for (int i = 0; i < par.length; i++) {
  //     int o = order[i];
  //     String v = toCheckv.get(o);
  //     println("i", i);
  //     println("value: ", v);
  //     if (o == 0) {
  //       int byr = int(v);
  //       if (bet(byr, 1920, 2002)) {
  //         validValues.add(v);
  //       }
  //     } else if (o == 1) {
  //       int iyr = int(v);
  //       if(bet(iyr, 2010, 2020)) {
  //         validValues.add(v);
  //       }
  //     } else if (o == 2) {
  //       int eyr = int(v);
  //       if (bet(eyr, 2020, 2030)) {
  //         validValues.add(v);
  //       }
  //     } else if (o == 3 && v.length() > 2) {
  //       int hgt = int(v.substring(0, v.length()-2));
  //       String unit = v.substring(v.length()-2);
  //       if (unit.equals("cm")) {
  //         if (bet(hgt, 150, 193)) {
  //           validValues.add(v);
  //         }
  //       } else if (unit.equals("in")) {
  //          if (bet(hgt, 59, 76)) {
  //             validValues.add(v);
  //           } 
  //       }
  //     } else if (o == 4) {
  //       String hcl = v.substring(1);
  //       if (v.substring(0, 1).equals("#") && hcl.length() == 6) {
  //         if (isHex(hcl)) {
  //           validValues.add(v);
  //         }
  //       }
  //     } else if (o == 5) {
  //       String[] ecls = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
  //       String ecl = v;
  //       for (String ec : ecls) {
  //         if (ec.equals(ecl)) {
  //           validValues.add(v);
  //           break;
  //         }
  //       }
  //     } else if (o == 6) {
  //       String pid = v;
  //       if (pid.length() == 9) {
  //         validValues.add(v);
  //       }
  //     }
  //   }
  //}
  //boolean cond2 = count2 == par.length ? true : false;
  //return cond2;
