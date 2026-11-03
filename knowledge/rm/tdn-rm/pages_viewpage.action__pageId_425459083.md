---
content_hash: 4855ab4054dd438284116e56ad1e61978c3e32c690934419a5e187dd0a2bb500
fetched_at: '2026-06-29T00:09:33.921845+00:00'
page_id: '425459083'
product: rm
source: tdn-rm
title: Geração do Histórico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459083
version: 17
---

É a geração de um documento que comprove que o aluno cumpriu um determinado grupo de disciplinas e está apto ou habilitado em um curso.

Para a realização da importação dos dados para o Histórico, as informações abaixo são indispensáveis.

* **Matricula na Disciplina**

 

* **Status de resultado Final na Disciplina**

* **Status de Resultado Final que indica Aprovação**

* **São Importadas somente Notas gravadas na Etapa Final**

* **Etapa Final**

Acessar o cadastro da Turma disciplina | Etapas e validar se a Flag Etapa Final for marcada

* **Tipo de Matricula na Matricula na Disciplina é obrigatório**

**Importante!**

As disciplinas de Itinerário Formativo também serão importadas, caso preencham os requisitos acima e possuam uma disciplina correspondente configurada para o [histórico](https://tdn.totvs.com/pages/viewpage.action?pageId=740687296).

***Matrícula e Avaliação | Geração do histórico***

Faça o filtro do aluno e/ou curso e/ou Período letivo e/ou etc.

A partir da versão 12.1.27, o sistema possui um campo de conceito mínimo para aprovação.

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

A partir das versões **12.1.2302.125** (necessário rodar todos os scripts do patch)e **12.1.2306**, ao realizar a geração de histórico, o sistema exibe as informações referente ao itinerário formativo para as disciplinas que tenham essa informação, caso esta associação esteja configurada no [histórico](https://tdn.totvs.com/pages/viewpage.action?pageId=740687296).

A partir das versões **12.1.2302.134** (necessário rodar todos os scripts do patch)e **12.1.2306** são exibidas as áreas de conhecimentos vinculadas a disciplinas do histórico que possui associação, configurada no [histórico](https://tdn.totvs.com/pages/viewpage.action?pageId=740687296).

Veja Também

---

[Como fazer - Geração do Histórico](http://tdn.totvs.com/x/MJglE)
