from turma import turma 
from idade import idade
import webbrowser
list1 = [{
    "nome": "Armando",
    "idade": "19",
    "turma": "3P"
},
{
    "nome": "Lucia",
    "idade": "21",
    "turma": "1P"
},
{
    "nome": "Yandro",
    "idade": "21",
    "turma": "4P"
},
{
    "nome": "Zilderberg",
    "idade": "22",
    "turma": "4P"
}]

#list1 = turma(list1, "4P") 
list1 = idade(list1, "4P")

f = open('create.html','w')

page = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
    <script src='main.js'></script>
</head>
<body>

    <h1>Lista de alunos </h1>
    <h3>Turma: 5P</h3>
    <h3>Ano: 2023</h3>
    <h3>Alunos: </h3>
    <ul>
"""
for x in list1 :
    page += f"""
        <li>{x["nome"]}</li>
    """
page += """
    </ul>
</body>
</html>
"""

f.write(page)
f.close()

webbrowser.open_new_tab('create.html')
