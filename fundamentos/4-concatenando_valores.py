name = input("Digite o nome do filme:\n")
yeardLaunch = int(input("Digite o ano de lançamento:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))

print(f"O filme {name} foi lançado em {yeardLaunch} com nota {noteMovie}")
print(f"O filme {name}\n" 
      f"foi lançado em {yeardLaunch}\n"
      f"com nota {noteMovie:.1f}"
      )