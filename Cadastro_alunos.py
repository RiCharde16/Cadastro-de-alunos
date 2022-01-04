import PySimpleGUI as gui

gui.theme("DarkAmber")
def janela_menu():
    estilo = [
        [gui.Button("Cadastrar",size=(10,1))],
        [gui.Button("Consultar",size=(10,1))],
        [gui.Button("Editar",size=(10,1))],
    ]
    return gui.Window("CADASTRO ALUNOS", layout=estilo,finalize=True,size=(200,100),element_justification="center")
def janela_Cadastro():
    estilo = [
        [gui.Text("nome do aluno:")],
        [gui.Input(key="Nome")],
        [gui.Text("RA do aluno:")],
        [gui.Input(key="RA")],
        [gui.Text("data nascimento do aluno:")],
        [gui.Input(key="Data_nasc")],
        [gui.Button("Cadastrar"), gui.Button("Voltar")],
    ]
    return gui.Window("Cadastrar", layout=estilo,finalize=True)
def janela_consulta():
    arquivo2 = open("Alunos.txt",'r',encoding="UTF-8")
    linha = [
        [gui.Text(arquivo2.read())],
    ]
    estilo = [
        [gui.Text("\t\tTABELA DE ALUNOS")],
        [gui.Column(layout=linha, scrollable=True, vertical_scroll_only=True)],
        [gui.Button("Voltar")],
    ]
    arquivo2.close()
    return gui.Window("Consultar",layout=estilo, finalize=True)
def janela_Editar():
    frame = [
        [gui.Text("Digite o RA do aluno que deseja editar:")],
        [gui.Input(key="RA_p")],

    ]
    estilo = [
        [gui.Frame(title="",layout=frame,key="cont")],
        [gui.Button("Voltar"), gui.Button("Pesquisar"), gui.Button("Excluir"),],
    ]
    return gui.Window("Editar",layout=estilo, finalize=True)
# janela incial
janela1, janela2, janela3, janela4 = janela_menu(), None, None, None
while True:
    window, event, value = gui.read_all_windows()
    if window == janela1 and event == gui.WIN_CLOSED:
        break
    elif window == janela2 and event == gui.WIN_CLOSED:
        break
    elif window == janela3 and event == gui.WIN_CLOSED:
        break
    elif window == janela4 and event == gui.WIN_CLOSED:
        break
    elif window == janela1 and event == "Cadastrar":
        janela1.Hide()
        janela2 = janela_Cadastro()
    elif window == janela1 and event == "Consultar":
        janela1.Hide()
        janela3 = janela_consulta()
    elif janela1 == window and event == "Editar":
        janela1.Hide()
        janela4 = janela_Editar()
    elif window == janela2 and event == "Voltar":
        arquivo3.close()
        janela1.UnHide()
        janela2.Hide()
    elif window == janela3 and event == "Voltar":
        janela3.Hide()
        janela1.UnHide()
    elif window == janela4 and event == "Voltar":
        janela4.Hide()
        janela1.UnHide()
# Extrair os dados
    elif window == janela2 and event == "Cadastrar":
        arquivo3 = open("Alunos.txt","r")
        texto = arquivo3.read()
        Nome = value["Nome"]
        Ra = str(value["RA"])
        data_nasc = value["Data_nasc"]
        if Ra in texto and Ra != "" and Nome != "" and data_nasc != "":
            gui.popup(" ESSE RA JA EXISTE!")
        elif Ra == "" or Nome == "" or data_nasc == "":
            gui.popup(" PORFAVOR DIGITE OS CAMPOS RESTANTES")
        else:
            arquivo = open("Alunos.txt", 'a+',encoding="UTF-8")
            arquivo.writelines("\n")
            arquivo.writelines("NOME: "+Nome+" RA: "+Ra+" DATA NASC: "+data_nasc+"\n")
            gui.popup(" !ALUNO CADASTRADO!")
            arquivo.close()
    elif window == janela4 and event == "Pesquisar":
        arquivo = open("Alunos.txt","r")
        RA = value["RA_p"]
        texto = arquivo.read()
        if RA in texto and RA != "" and "/" not in RA and "a" not in "RA":
            janela4.close()
            janela4 = janela_Editar()
            janela4.extend_layout(janela4["cont"],[[gui.Text("Digite o novo nome:")],
            [gui.Input(key="Nome_n")], [gui.Text("Digite a nova data de nascimento:")],
            [gui.Input(key="data_n")], [gui.Button("enviar")],
            ])
        else:
            gui.popup(" ESSE RA NÃO EXISTE")
        arquivo.close()
    elif window == janela4 and event == "Excluir":
        RA = value["RA_p"]
        if RA == "":
            gui.popup(" !DIGITE UM RA! ")
        else:
            valor = gui.popup_ok_cancel("Deseja excluir o aluno?")
            if valor == "OK":
                arquivo = open("Alunos.txt","r")
                texto = arquivo.readlines()
                for linha in range(len(texto)):
                    if RA in texto[linha] and RA != "":
                        texto.remove(texto[linha])
                        pos = linha
                        arquivo2 = open("Alunos.txt","w",encoding="UTF-8")
                        for linha in texto:
                            if pos > (len(texto)-1):
                                pos = len(texto)-1
                            else:
                                texto[pos] = end=""
                                arquivo2.writelines(linha)
                        arquivo2.close()
                        arquivo.close()
                        break
                gui.popup(" !ALUNO EXCLUIDO! ")
            else:
                continue
    elif window == janela4 and event == "enviar":
        arquivo = open("Alunos.txt","r")
        Nome_n = value["Nome_n"]
        data_n = value["data_n"]
        texto = arquivo.readlines()
        for linha in range(len(texto)):
            if RA in texto[linha]:
                pos = texto[linha]
                texto.remove(texto[linha])
                texto.insert(linha,"NOME: "+Nome_n+" RA: "+RA+" DATA NASC: "+data_n+"\n")
                arquivo2 = open("Alunos.txt","w",encoding="UTF-8")
                for linha in texto:
                    arquivo2.writelines(linha)
                arquivo2.close()
                arquivo.close()
        gui.popup(" !ALUNO ALTERADO!")
            
