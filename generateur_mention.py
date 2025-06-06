while True:
  try:
      moyenne = float(input("Entre ta moyenne :"))
      break
  except ValueError:
    print('Entre une Note Valide')
if moyenne > 20 or moyenne == 0:
  print("Ta moyenne est invalide")
elif 12 <= moyenne < 14:
  print("Assez Bien")
elif 14 <= moyenne < 16:
  print("Bien")
elif 16 <= moyenne < 18:
  print("Très Bien")
elif 18 <= moyenne <= 21:
  print("Felicitation du Jury")
else:
  print("Pas de Mention")
