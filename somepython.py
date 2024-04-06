#I created a python file successfully
print ("I CREATED THE FILE 'SOMEPYTHON.PY'")
bool = input ("Do you want to finish your maths times tables homework? (Y/N)")
if (bool === "Y" || "y") {
  mn = input ("What is the number you want to multiply?")
  nt = input ("How many times to multiply the first number?")
  for (tt = 0; tt<=nt; tt++) {
    print (mn, " X ", tt, " = ", mn*tt)
  }
}
