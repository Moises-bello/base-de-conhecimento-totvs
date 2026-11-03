---
content_hash: 865825849ee96678f2ce4530a6cbd1469a70d901e61e8b6d4c3e5f90ccb67748
fetched_at: '2026-06-29T00:10:43.222050+00:00'
page_id: '550313240'
product: rm
source: tdn-rm
title: Geração de Histórico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550313240
version: 14
---

---

---

|  |  |
| --- | --- |
| Descrição | Geração de Histórico |
| Objetivo | A Geração de um documento que comprove que o aluno cumpriu um determinado grupo de disciplinas e está apto ou habilitado em um curso é uma necessidade elementar de uma instituição de ensino. |

Requisitos:

* Matrícula em disciplinas;
* Tipo de Matricula na Matricula na Disciplina é obrigatório;
* Nota/Falta na etapa final;

Sempre que houver a inclusão de uma disciplina diversificada que deva aparecer no histórico, a disciplina deve passar pelo mesmo processo de cadastro das “disciplinas do histórico” tendo muita atenção a ordem de apresentação da mesma.

Histórico do Ensino Básico por Nível de Ensino

A partir da versão 12.1.29, será possível configurar a exclusividade do Curso do Histórico, Grupo de Séries, Disciplinas do Histórico e Partes do Histórico por Nível de Ensino. Através do caminho: Configurações > Parâmetros >15.01 - Secretaria > Geral 3/7 > Parâmetro: Utilizar Histórico por nível de ensino.

Este parâmetro fará com que todo cadastro relacionado ao histórico seja vinculado ao nível de ensino e visualizado apenas pelo mesmo. Caso o mesmo esteja desmarcado, a visualização e utilização do histórico será por coligada.

# Cursos do Histórico

***Currículo e Oferta | Histórico | Cursos do Histórico.***

Cadastre os “Cursos do Histórico” e, em seguida, as “Séries do histórico” que farão parte do Histórico da Instituição de Ensino.

Exemplo:

* Ensino Fundamental e Ensino Médio

O Ensino Médio apresenta as seguintes Séries do histórico (1º Série, 2º Série e 3º Série).  
*Acesse:  Currículo e Oferta / Histórico /Cursos do Histórico. Em Anexos “Séries do histórico”.*

# *Partes do Histórico*

***Currículo e Oferta | Histórico | Partes do histórico.***

Em seguida cadastre as “Partes do Histórico” e as “Disciplinas do histórico” para que seja possível realizar o cadastro do “layout de importação” presente nos “grupos de séries”.

Tais partes já são pré-determinadas pelo ministério da educação como:

* Base Nacional Comum
* Parte diversificada

***Currículo e Oferta | Histórico | Disciplinas do histórico.***

Realize o cadastro das disciplinas do histórico. Essas disciplinas são identificadas no histórico importado do aluno e serão associadas às disciplinas da grade do aluno posteriormente.

Mas, o que seriam as Disciplinas do Histórico e porque não usar as mesmas disciplinas da grade do aluno?  
Exemplo: Temos as seguintes disciplinas da grade do aluno:

* Português
* Redação

No entanto no Histórico do Aluno apresentará apenas a disciplina **Língua Portuguesa,** assim unificamos mais de uma disciplina ou mesmo disciplinas com nomenclaturas diferentes em uma única Identificação.

Importante

**Nessa tela também poderão ser incluídas disciplinas de Itinerário Formativo**

# Disciplinas do Histórico

Todos os registros de histórico devem possuir disciplinas. Se houver algum registro de histórico para o aluno sem disciplina, o relatório "EDUREL0001 - Histórico Escolar - Ensino Fundamental" não apresentará corretamente as notas de cada série.

***Currículo e Oferta | Histórico | Grupos de Séries | Séries.***

Nessa etapa definiremos os “Grupos de Série”, nos quais serão determinados o “Layout de importação” de disciplinas para o histórico com suas respectivas posições.

Vincule o “Curso” e suas “Séries” respectivas.

# Ordem da Série

Todas as séries devem possuir valor para o campo "Ordem". Essa informação é muito importante para a organização das notas no relatório "EDUREL0001 - Histórico Escolar - Ensino Fundamental". Sem essa informação as notas podem ficar fora de ordem.

Importante

**Apenas a ordem das séries pode ser configurada, e a posição irá variar de acordo com as séries existentes. Por exemplo, se não existir cadastrado a "1a Série" com a ordem 1, mas existir a "2a Série" com a ordem 2, o relatório irá apresentar a "2a Série" na primeira posição.**

# Layout de importação

***Currículo e Oferta | Histórico | Grupos de Séries | Layout de importação.***

Determine qual a parte do histórico e posição de cada disciplina do histórico.

***Currículo e Oferta | Disciplinas.***

Vincule as “Disciplinas do histórico” no cadastro de disciplinas (grade, etc.).

***Currículo e Oferta | Curso | Séries***

Vincule o “Curso” e o “Período do histórico” no cadastro do curso.

Assim com todos os cadastros necessários é possível fazer a “Geração do histórico”

Para a importação dos dados para o Histórico, as informações abaixo são indispensáveis.

* Matricula na Disciplina

* Status de resultado Final na Disciplina

* Status de Resultado Final que indica Aprovação

* São Importadas somente Notas gravadas na Etapa Final

* Etapa Final

Acessar o cadastro da Turma disciplina | Etapas e validar se a Flag Etapa Final for marcada

* Tipo de Matricula na Matricula na Disciplina é obrigatório

Importante

As disciplinas de Itinerário Formativo também serão importadas, caso preencham os requisitos acima e possuam uma disciplina correspondente configurada para o histórico.

***Matrícula e Avaliação | Geração do histórico***

Faça o filtro do aluno e/ou curso e/ou Período letivo e/ou etc.

Conceito mín. para aprovação

A partir da 12.1.27, o sistema possuirá o campo de conceito mínimo para aprovação.

    

Caso tenhamos o parâmetro "**Converter faltas e carga horária da disciplinas em horas**" marcado, o sistema irá transformar o valor de minutos para um formato de relógio de "***Horas:Minutos***".

Segue um exemplo da forma de cálculo realizada:

Quantidade de aulas da disciplina: 20,50 aulas

Tempo de aula: 50 minutos

Cálculo da carga horária:

* + Quantidade de aulas \* Tempo de aula = Carga horária em minutos

20,50 aulas \* 50 minutos = 1025 minutos

Cálculo do total de horas:

* 01 hora = 60 minutos
* Carga horária / 60 minutos = Total de horas

1025 minutos / 60 minutos = 17,08333 horas

Valor total de horas: 17,08333 horas

Como o resultado é um número fracionado, o valor precisa ser quebrado para que possamos encontrar a quantidade em minutos da parte fracionada da hora:

Total = 17,08333 horas

Parte inteira: 17 horas

Parte fracionada: 0,08333 horas

O resultado da carga horária convertida será composta do total de horas da parte inteira e o equivalente da parte fracionada em minutos:

Conversão da parte horária fracionada:

* + 01 Hora em minutos \* Parte fracionada da hora = Total em minutos

60 minutos \* 0,08333 horas = 5 minutos

***Resultado da conversão da carga horária:*** 17:05 (Horas:Minutos)
