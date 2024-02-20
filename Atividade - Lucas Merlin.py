# Lucas Merlin Knoll Da Silva #############################################################################################################################
# Análise e Desenvolvimento de Sistemas #############################################################################################################################

import json

# Aqui está a parte do código que dá as boas vindas: #############################################################################################################################

nome = input("Digite o seu nome: ")
mensagem = "Olá %s, seja bem vindo!" %nome
print(mensagem)

# Aqui ficam armazenadas as variáveis do sistema: #############################################################################################################################

menuTitle = "----- MENU PRINCIPAL -----"
option1 = "(1) Gerenciar estudantes."
option2 = "(2) Gerenciar professores."
option3 = "(3) Gerenciar disciplinas."
option4 = "(4) Gerenciar turmas."
option5 = "(5) Gerenciar matrículas."
option6 = "(6) Sair. "
menuOption = None

action1 = "(1) Incluir."
action2 = "(2) Listar."
action3 = "(3) Atualizar."
action4 = "(4) Excluir."
action5 = "(5) Voltar."
pageName = ''
actionOption = None

studentList = []
teacherList = []
classList = []
subjectList = []
registrationList = []

# Aqui ficam as funções que editam o "banco de dados": #############################################################################################################################

def openData(data):
    try:
        with open(data + '.json','r') as d: 
            return json.load(d) 
    except FileNotFoundError: 
        print("Dados não localizados")

def registerData(data, dataName):
    with open(dataName + '.json', 'w') as d:
        json.dump(data, d)
        d.close()

# Aqui ficam as funções que iniciam o menu principal e o menu secundário, que possibilitam navegar entre as opções: #############################################################################################################################

def init():
    print("")
    global studentList
    global teacherList
    global classList
    global subjectList
    global registrationList
    global menuOption
    studentList = openData('studentData')
    teacherList = openData('teacherData')
    classList = openData('classData')
    subjectList = openData('subjectData')
    registrationList = openData('registrationData')
    menuOption = None
    print(menuTitle)
    print(option1)
    print(option2)
    print(option3)
    print(option4)
    print(option5)
    print(option6)
    print("--------")
    menuOption = float(input("Informe a opção desejada: "))
    selectPage()

def initAction():
    print("")
    global pageName
    print('**** [%s] MENU DE OPERAÇÕES *****' %pageName ) 
    print(action1)
    print(action2)
    print(action3)
    print(action4)
    print(action5)
    print("--------")
    global actionOption 
    actionOption = float(input("Informe a ação desejada: "))
    selectAction()

def selectPage():
    global pageName
    if menuOption == 1:
        pageName = 'ESTUDANTES'
        initAction()
    elif menuOption == 2:
        pageName = 'PROFESSORES'
        initAction()
    elif menuOption == 3:
        pageName = 'DISCIPLINAS'
        initAction()
    elif menuOption == 4:
        pageName = 'TURMAS'
        initAction()
    elif menuOption == 5:
        pageName = 'MATRÍCULAS'
        initAction()
    elif menuOption == 6:
        print("Finalizando Aplicação...")
    else: 
        print("Opção inválida, tente novamente")
        init()

# Esta função seleciona qual outro conjunto de funções será acionado de acordo com a opção selecionada: #############################################################################################################################

def selectAction():
    if pageName == "ESTUDANTES":
        studentAction()
    if pageName == "PROFESSORES":
        teacherAction()
    if pageName == "DISCIPLINAS":
        subjectAction()
    if pageName == "TURMAS":
        classAction()
    if pageName == "MATRÍCULAS":
        registrationAction()
    else: 
        print("")
        print("Opção inválida")
        print("")
        init()

# Aqui ficam as funções de cada opção de ações para estudantes. #############################################################################################################################

def addStudent():
    name = input("Informe o nome do estudante: ")
    code = input("Informe o código do estudante: ") 
    cpf = input ("Informe o cpf do estudante: ")
    stop = False

    for i in range(len(studentList)):
        if studentList[i][1] == code:
            stop = True
            print("Este código de estudante já está cadastrado, utilize outro código")
    if stop == False:
        newStudent = (name, code, cpf)
        studentList.append(newStudent)
        registerData(studentList, "studentData")
        print("")
        print('Estudante incluído com sucesso')
        print("")

def returnStudents():
    if len(studentList) > 0:
        print("")
        for i in range(len(studentList)):
            print(f"Estudante: {studentList[i][1]}. {studentList[i][0]} ({studentList[i][2]})")
        print("")
    else:
        print("") 
        print("Nenhum aluno cadastrado")
        print("")

def editStudent():
    selectedCode = input("Informe o código do estudante que deseja alterar: ")
    index = "null"
    for i in range(len(studentList)):
        if studentList[i][1] == selectedCode:
            index = i
            if index == "null":
                print("")
                print("Estudante não localizado. Tente novamente")
                print("")
            else:    
                name = input("Informe o novo nome do estudante: ")
                code = input("Informe o novo código do estudante: ") 
                cpf = input ("Informe o novo cpf do estudante: ")
                stop = False
                for j in range(len(studentList)):
                    if studentList[j][1] == code:
                        if code != selectedCode:
                            stop = True
                            print("")
                            print("Este código de estudante já está cadastrado, utilize outro código")
                            print("")
                if stop == False:
                    studentList.pop(index)
                    newStudent = (name, code, cpf)
                    studentList.append(newStudent)
                    registerData(studentList, "studentData")
                    print("")
                    print('Estudante editado com sucesso!')
                    print("")
                    break

def deleteStudent ():
    selectedCode = input("Informe o código do estudante que deseja excluir: ")
    index = "null"
    for i in range(len(studentList)):
        if studentList[i][1] == selectedCode:
            index = i
            if index != "null":
                studentList.pop(index)
                break
    registerData(studentList, "studentData")
    print("")
    print("Estudante excluído com sucesso")
    print("")

# Aqui ficam as funções de cada opção de ações para professores. #############################################################################################################################

def addTeacher():
    name = input("Informe o nome do professor: ")
    code = input("Informe o código do professor: ") 
    cpf = input ("Informe o cpf do professor: ")
    stop = False

    for i in range(len(teacherList)):
        if teacherList[i][1] == code:
            stop = True
            print("")
            print("Este código de professor já está cadastrado, utilize outro código")
            print("")
    if stop == False:
        newTeacher = (name, code, cpf)
        teacherList.append(newTeacher)
        registerData(teacherList, "teacherData")
        print("")
        print('Professor incluído com sucesso')
        print("")

def returnTeacher():
    if len(teacherList) > 0:
        print("")
        for i in range(len(teacherList)):
            print(f"Professor: {teacherList[i][1]}. {teacherList[i][0]} ({teacherList[i][2]})")
        print("")
    else: 
        print("")
        print("Nenhum professor cadastrado")
        print("")

def editTeacher():
    selectedCode = input("Informe o código do professor que deseja alterar: ")
    index = "null"
    for i in range(len(teacherList)):
        if teacherList[i][1] == selectedCode:
            index = i
            if index == "null":
                print("")
                print("Professor não localizado. Tente novamente")
                print("")
            else:    
                name = input("Informe o novo nome do professor: ")
                code = input("Informe o novo código do professor: ") 
                cpf = input ("Informe o novo cpf do professor: ")
                stop = False
                for j in range(len(teacherList)):
                    if teacherList[j][1] == code:
                        if code != selectedCode:
                            stop = True
                            print("")
                            print("Este código de professor já está cadastrado, utilize outro código")
                            print("")
                if stop == False:
                    teacherList.pop(index)
                    newTeacher = (name, code, cpf)
                    teacherList.append(newTeacher)
                    registerData(teacherList, "teacherData")
                    print("")
                    print('Professor editado com sucesso!')
                    print("")
                    break

def deleteTeacher ():
    selectedCode = input("Informe o código do professor que deseja excluir: ")
    index = "null"
    for i in range(len(teacherList)):
        if teacherList[i][1] == selectedCode:
            index = i
            if index != "null":
                teacherList.pop(index)
                break
    registerData(teacherList, "teacherData")
    print("")
    print("Professor excluído com sucesso")
    print("")

# Aqui ficam as funções de cada opção de ações para disciplinas. #############################################################################################################################

def addSubject():
    code = input("Informe o código da disciplina: ")
    name = input("Informe o nome da disciplina: ") 
    stop = False

    for i in range(len(subjectList)):
        if subjectList[i][0] == code:
            stop = True
            print("")
            print("Este código de disciplina já está cadastrado, utilize outro código")
            print("")
    if stop == False:
        newSubject = (code, name)
        subjectList.append(newSubject)
        registerData(subjectList, "subjectData")
        print("")
        print('Disciplina incluída com sucesso')
        print("")

def returnSubject():
    if len(subjectList) > 0:
        print("")
        for i in range(len(subjectList)):
            print(f"Disciplina: {subjectList[i][0]}. {subjectList[i][1]}")
        print("")
    else: 
        print("")
        print("Nenhuma disciplina cadastrada")
        print("")

def editSubject():
    selectedCode = input("Informe o código da disciplina que deseja alterar: ")
    index = "null"
    for i in range(len(subjectList)):
        if subjectList[i][0] == selectedCode:
            index = i
            
    if index == "null":
        print("")
        print("Disciplina não localizada. Tente novamente")
        print("")
    else:    
        code = input("Informe o novo código da disciplina: ")
        name = input("Informe o novo nome da disciplina: ") 
        stop = False
        for j in range(len(subjectList)):
            if subjectList[j][1] == code:
                if code != selectedCode:
                    stop = True
                    print("")
                    print("Este código de disciplina já está cadastrado, utilize outro código")
                    print("")
        if stop == False:
            subjectList.pop(index)
            newSubject = (code, name)
            subjectList.append(newSubject)
            registerData(subjectList, "subjectData")
            print("")
            print('Disicplina editada com sucesso!')
            print("")

def deleteSubject ():
    selectedCode = input("Informe o código da disciplina que deseja excluir: ")
    index = "null"
    for i in range(len(subjectList)):
        if subjectList[i][0] == selectedCode:
            index = i
            if index != "null":
                subjectList.pop(index)
                break
    registerData(subjectList, "subjectData")
    print("")
    print("Disciplina excluída com sucesso")
    print("")

# Aqui ficam as funções de cada opção de ações para turmas. #############################################################################################################################

def addClass():
    code = input("Informe o código da turma: ")
    teacherCode = input("Informe o código do professor: ") 
    disciplineCode = input ("Informe o código da disciplina: ")
    stop = False

    for i in range(len(classList)):
        if classList[i][0] == code:
            stop = True
            print("")
            print("Este código de turma já está cadastrado, utilize outro código")
            print("")
    if stop == False:
        newClass = (code, teacherCode, disciplineCode)
        classList.append(newClass)
        registerData(classList, "classData")
        print("")
        print('Turma incluída com sucesso')
        print("")

def returnClass():
    if len(classList) > 0:
        print("")
        for i in range(len(classList)):
            print(f"Turma {classList[i][0]}. Código do professor: {classList[i][1]} Código da disciplina: {classList[i][2]}")
        print("")
    else: 
        print("")
        print("Nenhuma turma cadastrado")
        print("")

def editClass():
    selectedCode = input("Informe o código da turma que deseja alterar: ")
    index = "null"
    for i in range(len(classList)):
        if classList[i][0] == selectedCode:
            index = i
    if index == "null":
        print("")
        print("Turma não localizada. Tente novamente")
        print("")
    else:    
        code = input("Informe o novo código da turma: ")
        teacherCode = input("Informe o novo código do professor: ") 
        disciplineCode = input ("Informe o novo código da disciplina: ")
        stop = False
        for j in range(len(classList)):
            if classList[j][1] == code:
                if code != selectedCode:
                    stop = True
                    print("")
                    print("Este código de turma já está cadastrado, utilize outro código")
                    print("")
        if stop == False:
            classList.pop(index)
            newClass = (code, teacherCode, disciplineCode)
            classList.append(newClass)
            registerData(classList, "classData")
            print("")
            print('Turma editada com sucesso!')
            print("")

def deleteClass ():
    selectedCode = input("Informe o código da turma que deseja excluir: ")
    index = "null"
    for i in range(len(classList)):
        if classList[i][0] == selectedCode:
            index = i
            if index != "null":
                classList.pop(index)
                break
    registerData(classList, "classData")
    print("")
    print("Turma excluída com sucesso")
    print("")

# Aqui ficam as funções de cada opção de ações para matrículas. #############################################################################################################################

def addRegistration():
    classCode = input("Informe o código da turma: ")
    studentCode = input("Informe o nome do estudante: ") 
    stop = False

    for i in range(len(registrationList)):
        if registrationList[i][0] == classCode and registrationList[i][1] == studentCode :
            stop = True
            print("")
            print("Esta matrícula já foi realizada")
            print("")
    if stop == False:
        newRegistration = (classCode, studentCode)
        registrationList.append(newRegistration)
        registerData(newRegistration, "registrationData")
        print("")
        print('Matrícula incluída com sucesso')
        print("")

def returnRegistration():
    if len(registrationList) > 0:
        print("")
        for i in range(len(registrationList)):
            print(f"Código da turma:{registrationList[i][0]}  Código do Estudante: {registrationList[i][1]}")
        print("")
    else: 
        print("")
        print("Nenhuma matrícula registrada")
        print("")

def editRegistration():
    selectedClassCode = input("Informe o código da turma da matrícula que deseja alterar: ")
    selectedStudentCode = input("Informe o código do estudante matriculado que deseja alterar: ")
    index = "null"
    for i in range(len(registrationList)):
        if registrationList[i][0] == selectedClassCode and registrationList[i][1] == selectedStudentCode:
            index = i
            if index == "null":
                print("")
                print("Matrícula não localizada. Tente novamente")
                print("")
            else:    
                classCode = input("Informe o novo código da turma: ")
                studentCode = input("Informe o novo código do estudante: ") 
                stop = False
                for j in range(len(registrationList)):
                    if registrationList[i][0] == classCode and registrationList[i][1] == studentCode:
                        stop = True
                        print("")
                        print("Esta matrícula ja foi realizada")
                        print("")
                if stop == False:
                    registrationList.pop(index)
                    newRegistration = (classCode, studentCode)
                    registrationList.append(newRegistration)
                    registerData(registrationList, "registrationData")
                    print("")
                    print('Matrícula editada com sucesso!')
                    print("")
                    break

def deleteRegistration ():
    classCode = input("Informe o código da turma da matrícula que deseja excluir: ")
    studentCode = input("Informe o código do estudante da matrícula que deseja excluir: ")
    index = "null"
    for i in range(len(registrationList)):
        if registrationList[i][0] == classCode and registrationList[i][1] == studentCode:
            index = i
            print(index)
            if index != "null":
                registrationList.pop(index)
                break
    registerData(registrationList, "registrationData")
    print("")
    print("Matrícula excluída com sucesso")
    print("")

# Aqui ficam as funções que controlam as ações. #############################################################################################################################

def studentAction():
    if actionOption == 1:
       addStudent()
       initAction()
    elif actionOption == 2:
        returnStudents()
        initAction()
    elif actionOption == 3:
        editStudent()
        initAction()
    elif actionOption == 4:
        deleteStudent()
        initAction()
    elif actionOption == 5:
        init()
    else: 
        print("Opção inválida, tente novamente")
        initAction()

def teacherAction():
    if actionOption == 1:
       addTeacher()
       initAction()
    elif actionOption == 2:
        returnTeacher()
        initAction()
    elif actionOption == 3:
        editTeacher()
        initAction()
    elif actionOption == 4:
        deleteTeacher()
        initAction()
    elif actionOption == 5:
        init()
    else: 
        print("Opção inválida, tente novamente")
        initAction()

def classAction():
    if actionOption == 1:
       addClass()
       initAction()
    elif actionOption == 2:
        returnClass()
        initAction()
    elif actionOption == 3:
        editClass()
        initAction()
    elif actionOption == 4:
        deleteClass()
        initAction()
    elif actionOption == 5:
        init()
    else: 
        print("Opção inválida, tente novamente")
        initAction()

def subjectAction():
    if actionOption == 1:
       addSubject()
       initAction()
    elif actionOption == 2:
        returnSubject()
        initAction()
    elif actionOption == 3:
        editSubject()
        initAction()
    elif actionOption == 4:
        deleteSubject()
        initAction()
    elif actionOption == 5:
        init()
    else: 
        print("Opção inválida, tente novamente")
        initAction()

def registrationAction():
    if actionOption == 1:
       addRegistration()
       initAction()
    elif actionOption == 2:
        returnRegistration()
        initAction()
    elif actionOption == 3:
        editRegistration()
        initAction()
    elif actionOption == 4:
        deleteRegistration()
        initAction()
    elif actionOption == 5:
        init()
    else: 
        print("Opção inválida, tente novamente")
        initAction()

# Aqui damos o ponto de partida no projeto: #############################################################################################################################

init()


