---
content_hash: 314d189c269716ce7efe1e68d0200f5b745420a6aee41f74883feb81a2ca1213
fetched_at: '2026-06-29T00:08:37.530860+00:00'
page_id: '284880137'
product: rm
source: tdn-rm
title: Faltas por Etapa
type: documentation
url: https://tdn.totvs.com/display/LRM/Faltas+por+Etapa
version: 45
---

Nesta tela o aluno conseguirá visualizar as faltas por etapa, podendo também agrupar as colunas que ele deseja arrastando para o cabeçalho.

## **01. LISTA DE FALTAS DISPONÍVEIS**

O sistema irá disponibilizar as aulas dadas seguindo a regra:

Etapa disponível

A etapa esteja com a opção:

* **"Disponível para os alunos"** **marcado**
* **"E**xibe no portal e na central do aluno**"** **marcado**

A opção "Disponível para os alunos" **só é válida**, caso o parâmetro **Parâmetros| Secretaria | Notas/Faltas |Permitir a visualização das notas e faltas da etapa somente após liberação do professor** estiver **marcado**.

Liberação do professor

O parâmetro "**Permite a visualização das notas e faltas da etapa somente após a liberação do professor**" caso esteja **marcado**, **o aluno só poderá ter acesso a avaliação e sua nota após liberada.** Este parâmetro se encontra: **Parâmetros | Secretaria | Notas/Faltas**

Imprime no boletim - Ensino Básicofalse

**Disponível apenas para o Contexto Ensino Básico**

Ao marcar o parâmetro "**Parâmetros | RM Portal** **| RM Portal - Geral 4/15 |** **Exibir as disciplinas para o aluno de acordo com o campo 'Imprime no boletim' do cadastro de disciplinas da matriz curricular**", o portal irá apresentar somente as avaliações de disciplinas que estejam com a opção "**Indica se imprime no boletim e exibe no portal do aluno**” **marcada** no cadastro das disciplinas da matriz curricular do aluno.

Exibir no gráfico

O parâmetro **não** tem nenhuma relação com qualquer funcionalidade do portal, ele é utilizado apenas no RM.

## **02. PERCENTUAL DE FALTAS**

A coluna de percentual de faltas é calculada sobre a quantidade de faltas do aluno sobre a carga horária da disciplina, podendo levar em consideração também a duração da aula na turma/disciplina dependo da parametrização. Para exibir a coluna com o percentual de faltas deverá estar parametrizado o limite de faltas**.**

Carga horária

Cada disciplina deve possuir a carga horária **preenchida**. A carga horária pode ser da disciplina na grade (ensino básico) ou no cadastro da disciplina (ensino superior).

Cálculo do percentual de faltas apenas com a carga horária da disciplina

Para realizar o cálculo do percentual de faltas utilizando **apenas com a carga horária da disciplina**, o parâmetro "**Configurações | Parâmetros | Secretaria | Geral 2/7 | Considerar a carga horária da disciplina como horas**" deve estar **desmarcado** e o parâmetro "**Configurações | Parâmetros | Secretaria | Geral 2/6 | Exibir aviso de frequência por tipo de aula"** deve estar **desmarcado**. 

Regra de cálculo

Cálculo da porcentagem de faltas será: **(QUANTIDADE DE FALTAS NA ETAPA****/ CARGA HORARIA DA DISCIPLINA) \* 100**

Cálculo de percentual de faltas para considerar a carga horária como horasfalse

**Disponível apenas para o Contexto Ensino Superior**

Para realizar o cálculo do percentual de faltas utilizando **a carga horária da disciplina como horas**, o parâmetro "**Configurações | Parâmetros | Secretaria | Geral 2/7 | Considerar a carga horária da disciplina como horas**" deve estar **marcado** e o parâmetro **"Configurações | Parâmetros | Secretaria | Geral 2/6 | Exibir aviso de frequência por tipo de aula"** deve estar **desmarcado.**

Neste caso é utilizada no cálculo o campo de **"Duração da aula"** da turma/disciplina.

Regra de cálculo

Cálculo da porcentagem de faltas será: **(QUANTIDADE DE FALTAS NA ETAPA / (CARGA HORARIA DA DISCIPLINA \* 60 / DURAÇÃO DA AULA DA TURMADISCIPLINA)) \* 100**

Cálculo de percentual de faltas por tipo de aulafalse

**Disponível apenas para o Contexto Ensino Superior**

Para realizar o cálculo do percentual de faltas por tipo de aula considerada no plano de aula correspondente, o parâmetro "**Configurações | Parâmetros | Secretaria | Geral 4/7 | Exibir aviso de frequência por tipo de aula**" deve estar **marcado.**

Regra de cálculo

Cálculo da porcentagem de faltas será: **(QUANTIDADE DE FALTAS DIÁRIA / CARGA HORARIA DA DISCIPLINA DO TIPO DE AULA) \* 100**

Não é utilizada a carga horária da disciplina como horas

Neste caso **não é utilizada a carga horária da disciplina como horas**, o parâmetro **"Configurações | Parâmetros | Secretaria | Geral 2/7 | Considerar a carga horária da disciplina como horas" não é considerado neste caso**

Todos os tipo de aula da turma/disciplina devem ser iguais

Para que o cálculo do percentual de faltas por tipo de aula funcione corretamente **é necessário que todos os tipos de aulas dos planos de aulas considerados na turma/disciplina devem ser iguais.** Caso seja diferente o cálculo será exibido com base no primeiro tipo de aulas encontrado.

Utilizar a etapa final da turma/disciplina para consultar a frequência mínima sem etapa final

Caso o parâmetro "**Configurações | Parâmetros | Secretaria | Geral 4/7 | Utilizar a etapa final da turma/disciplina para consultar a frequência mínima"** estaja **marcado**, mas não existe a etapa final, a coluna ficará nula.

Tipo de aula informado no plano de aula

Caso o campo "Tipo aula" do plano de aula **não esteja preenchido**, o sistema irá utilizar para o cálculo o tipo de aula padrão definido no parâmetro **"Configurações | Parâmetros | Secretaria | Geral 4/7 | Classificação padrão do tipo de aula quando não preenchida"**

Carga horária do tipo de aula do plano de aula não preenchida

Caso o campo da carga horária do tipo de aula do plano de aula **não esteja preenchida**, o portal **não irá exibir** a informação de percentual de falta

## 

## **03. SITUAÇÃO DE FALTAS**

A coluna de situação de falta é calculada a partir do percentual de faltas do aluno sobre um limite de faltas geral ou um limite de frequência mínima exigida de cada etapa final da turma/disciplina.

Utilizar a etapa final da turma/disciplina para consultar a frequência mínima

Para realizar o cálculo da **situação do percentual de falta**, será considerado o **p****ercentual de presença do aluno** e a **frequência mínima** cadastrada na etapa final da turma/disciplina. Neste caso o parâmetro "**Configurações | Parâmetros | Secretaria | Geral 4/7 | Utilizar a etapa final da turma/disciplina para consultar a frequência mínima"** deve estar **marcado.**

Parâmetro disponível a partir da versão 12.1.2402Regra de cálculo da situação de falta

Cálculo da situação de falta será:

**Faltas dentro do limite = PERCENTUAL DE FREQUÊNCIA MÍNIMA DA ETAPA FINAL DA TURMA/DISC < PERCENTUAL DE PRESENÇA\***

**Faltas próximas do limite = (PERCENTUAL DE FREQUÊNCIA MÍNIMA DA ETAPA FINAL DA TURMA/DISC > (PERCENTUAL DE PRESENÇA\* X 0.93)) E** **PERCENTUAL DE PRESENÇA\* >= PERCENTUAL DE FREQUÊNCIA MÍNIMA DA ETAPA FINAL DA TURMA/DISC**

**Faltas acima do limite =** **PERCENTUAL DE FREQUÊNCIA MÍNIMA DA ETAPA FINAL DA TURMA/DISC > PERCENTUAL DE PRESENÇA\***

**\*** O valor de percentual de presença não é exibido no portal do aluno, ela é calculada **PERCENTUAL DE PRESENÇA = 100 - PERCENTUAL DE FALTA DO ALUNO**

#### 

Campos necessários na etapa para o cálculo da situação do percentual de falta

Para a etapa é necessário que os campos na etapa para o cálculo da situação do percentual de falta:

* **"Freq. mínima (%)"** **preenchida**
* **"Etapa final"** **marcada**

Utilizar um único limite de falta padrão para todas as turma/disciplina

Para realizar o cálculo da **situação do percentual de falta**, será considerado o **p****ercentual de faltas do aluno** e a um único limite de falta padrão para todas as turma/disciplina. Neste caso o parâmetro "**Configurações | Parâmetros | Secretaria | Geral 4/7 | Utilizar a etapa final da turma/disciplina para consultar a frequência mínima"** deve estar **desmarcado.**

Regra de cálculo da sitiuação de falta

Cálculo da situação de falta será:

**Faltas dentro do limite = PERCENTUAL DE FALTA DO ALUNO < PERCENTUAL DE LIMITE DE FALTA\***

**Faltas próximas do limite = PERCENTUAL DE FALTA DO ALUNO >= (PERCENTUAL DE LIMITE DE FALTA\* X 0.8) E (PERCENTUAL DE FALTA DO ALUNO <= PERCENTUAL DE LIMITE DE FALTA\*)**

**Faltas acima do limite = PERCENTUAL DE FALTA DO ALUNO >** **PERCENTUAL DE LIMITE DE FALTA\***

**\*** O valor de **PERCENTUAL DE LIMITE DE FALTA** corresponde ao valor do parâmetro **"% Limite de Faltas"**, disponível em: **Configurações | Parâmetros | Secretaria | Geral 4/7**

#### 

## **04. LEGENDA**

Será exibido a legenda com informações sobre o limite de faltas, caso esteja parametrizado para exibir o percentual de faltas.

* As faltas que ainda não atingiram o limite e não estão próximas disso, serão classificadas com a situação **"Faltas dentro do limite"**
* As faltas acima do percentual limite serão classificadas com a situação  **"Faltas próximas do limite"**
* As faltas próximas do percentual limite serão classificadas com a situação  **"Faltas acima do limite"**
* Quando não for possível realizar o cálculo do percentual de faltas serão classificadas com a situação **"Não foi possível calcular o percentual"**, caso isso ocorra, favor verificar se a carga horária da disciplina está preenchida com um valor maior que zero, se existe uma etapa final cadastrada para a turma/disciplina e se nesta etapa o campo frequência mínima está preenchido com um valor maior que zero.

## **05. DETALHE DA DISCIPLINA**

Clicando na descrição da disciplina, o aluno poderá ter acesso a listagem da disciplina através no botão “ver mais informações”.

## **06. FALTAS POR AULA**

Para ter acesso as faltas de cada aula, basta clicar no link "Ver faltas" para ser redirecionado diretamente para a aba **Faltas por aula**. Para saber mais acesse:
