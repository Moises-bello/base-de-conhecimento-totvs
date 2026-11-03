---
content_hash: 21fa3e1f089d280486b8c011826bff77b520570a1e6fd2d0bdd2674b4a3c844f
fetched_at: '2026-06-29T00:08:45.408834+00:00'
page_id: '311630991'
product: rm
source: tdn-rm
title: DT Configuração da sugestão de disciplinas na parametrização por curso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=311630991
version: 100
---

# CONFIGURAÇÃO DA SUGESTÃO DE DISCIPLINAS NA PARAMETRIZAÇÃO POR CURSO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Sugestão de Disciplinas* | *Sugestão de Disciplinas* | | *Copiar matriz aplicada para outro período letivo* | *Copiar matriz aplicada para outro período letivo* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Cadastro da Parametrização por Curso** | *Cadastro da Parametrização por Curso* | | *Matricula em Disciplinas* | *Matricula em Disciplinas* | |
| **Cadastros Iniciais:** | **Para o cadastro e cópia de SDD(através da cópia de matriz aplicada) é necessário o cadastro dos itens:**   * *Período Letivo;* * *Curso;* * *Habilitação;* * *Matriz curricular;* * *Turno;* |
| **Parâmetro(s):** | *Em Currículo e Oferta | Parametrização por Curso | Aba Configuração para sugestão de turma/disciplina:*   * *Utiliza sugestão de disciplina da parametrização por curso* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-2855* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *SHABILITACAOFILIALPL* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

Na parametrização por curso foi disponibilizado os parâmetros de sugestão de disciplinas, SDD, (os mesmos que existem hoje no parametrizador Configurações | Parâmetros | Matrícula | Sugestão de Disciplinas 1/2 e 2/2).

O objetivo é ofertar turmas com regras diferentes para cada curso, para atender às diferentes demandas das coordenações de curso.

Evolução no processo de copia da matriz aplicada para outro período letivo para que seja copiado as configurações para sugestão de turma/disciplina (SDD) do período letivo de origem para o período letivo de destino

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.19.

## Cadastrando e utilizando a SDD por curso.

Foi criado as parametrizações da Sugestão de Disciplinas na Parametrização por Curso em Currículo e Oferta | Parametrização por Curso | Aba Configuração para sugestão de turma/disciplina, sendo possível utilizar uma parametrização de sugestão de disciplinas por curso, sendo para isso é necessário acessar a aba Configuração para sugestão de turma/disciplina e marcar o item **Utilizar sugestão de disciplinas da parametrização por curso**. Ao marcar este parâmetro a sugestão que passa a valer será a da parametrização por curso e não mais da parametrização geral.

* Acessar o cadastro de Parametrização por Curso em Currículo e Oferta | Parametrização por Curso;
* Acessar a Aba Configuração para sugestão de turma/disciplina;
* Marcar o item **Utilizar sugestão de disciplinas da parametrização por curso**;
* Marcar o item **Selecionar disciplinas optativas / eletivas**conforme abaixo:
* Acessar o processo de matrícula do aluno em Currículo e Oferta | Aluno | Anexo Cursos/Habilitações;
* Neste anexo criar um Curso/Habilitação para o mesmo, sendo este o parametrizado acima;
* Acessar o Processo deste anexo Matricular Aluno | Avançar o processo e acessar o botão de Sugestão de Disciplinas
* Será exibido apenas as disciplinas conforme os parâmetros marcados;
* Independente da parametrização geral da sugestão de disciplinas a regra que vai ser considerada será da parametrização por curso.

  Importante

  Caso o item **Utilizar sugestão de disciplinas da parametrização por curso** esteja desmarcado na parametrização por curso a regra que irá prevalecer será a da parametrização geral.

## Copiando a SDD por curso

* No menu Currículo e Oferta acessar a opção Parametrização por curso para ter acesso aos registros;
* Selecionar um registro no grid para que ele seja o período letivo de origem;
* Escolher o processo copiar matriz aplicada para outro período letivo;
* Observe como na imagem abaixo, as opções escolhidas para a configuração para sugestão de turma/disciplinas, pois ao copiar a matriz aplicada para o outro período letivo essas configurações serão replicadas.

* Selecionar no menu de processo a opção "Copiar matriz aplicada para outro período letivo". Ao abrir o processo selecione o período letivo de destino para qual deseja copiar as informações, como na imagem a baixo:

* Avançar e executar o processo. Ao executar o processo você pode se deparar com a seguinte mensagem no log;
* Mensagem de Alerta:
* Isso indica que o período letivo selecionado como destino já tem uma matriz aplicada e que o processo não copiou as parametrizações do período letivo de origem.
* Mensagem de sucesso:
* Isso indica que o processo de copia foi executado com sucesso e as parametrizações de SDD foram copiadas para o próximo período letivo.

Importante

Caso o item **Utilizar sugestão de disciplinas da parametrização por curso** esteja desmarcado na parametrização por curso a regra que irá prevalecer será a da parametrização geral.

divs
