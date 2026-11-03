---
content_hash: 0e763ea781c4c7f46da8ad81d264b05d0320fe3d282a02fb9d0446a98a6b3e6d
fetched_at: '2026-06-29T00:11:16.526640+00:00'
page_id: '673788463'
product: rm
source: tdn-rm
title: Provedor - Análise Curricular do Aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=673788463
version: 1
---

# Objetivo

---

Este provedor de dados é utilizado quando se deseja montar um relatório que exibirá a análise curricular do aluno.

# Optativas/Eletivas

---

Quando não se utiliza o grupo de optativa/eletiva então deve utilizar os campos abaixo:

QTDTOTALDISCELE  
QTDCONCDISCELE   
QTDPENDDISCELE  
QTDTOTALDISCOPT  
QTDCONCDISCOPT   
QTDPENDDISCOPT

Estes campos são utilizados no resumo da análise curricular.

Entretanto para que as casas decimais seja obedecida no retorno dos valores uma expressão deverá ser adicionada e a seguinte instrução deverá ser feita.

# Grupo de Optativas/Eletivas

---

Quando se utiliza o grupo de optativa/eletiva não se deve utilizar os campos abaixo:

QTDTOTALDISCELE  
QTDCONCDISCELE   
QTDPENDDISCELE  
QTDTOTALDISCOPT  
QTDCONCDISCOPT   
QTDPENDDISCOPT

Estes campos não são populados para o cálculo no grupo de optativa/eletiva.

O que se deve fazer é seguir o que o relatório do book EDUREL0018 faz, ou seja, deve existir duas expressões e um campo totalizador no relatório, conforme abaixo.

Cada um destes campos representa respectivamente o número de CH ou créditos ou disciplinas, a quantidade concluída e quantidade pendente.

## Quantidade CH ou Créditos ou Disciplinas

A primeira expressão traz a descrição do tipo de avaliação (CH, crédito ou número de disciplinas) e o mínimo necessário. Observe que o campo TIPOAVALIACAO e os MINCH, MINCREDITOS e MINDISCIPINAS são campos que vieram de uma consulta SQL.

## Quantidade Concluída

O segundo campo é totalizador.

Este totalizador vai somar de acordo com o tipo de avaliação, as disciplinas concluídas.

## Quantidade Pendente

O último campo é uma outra expressão, de acordo com o tipo de avaliação trará o resultado da quantidade mínima (de acordo com o tipo de avaliação) menos o resultado de um totalizador (TotalGrupoOptEletiva).

O totalizador TotalGrupoOptEletiva é o mesmo do segundo campo, segue abaixo.
