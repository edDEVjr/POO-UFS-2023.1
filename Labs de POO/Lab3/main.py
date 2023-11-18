from professor import Professor

professor1 = Professor("Jose",1,8)
nome = input("Digite o nome")
professor1.setNome(nome)
matricula = input("Digite a Matrícula")

professor1.setMatriculaSIAPE(int(matricula))

carga =input("Digite carga horaria")
 
professor1.setCargaHS(int(carga))

print(professor1.getNome(), professor1.getMatriculaSIAPE(), professor1.getCargaHS())

mais =input("Quantas horas voce quer adicionar?")
professor1.maisHoras(int(mais))

menos = input("Quantas horas voce quer retirar?")

professor1.menosHoras(int(menos))