---
content_hash: 8dc4b0668f8584a054e4448cfa8b8ba31666357e2d94d8a5570e41b9a8e8242e
fetched_at: '2026-06-29T00:08:37.554714+00:00'
page_id: '284880151'
product: rm
source: tdn-rm
title: Avaliações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284880151
version: 30
---

Nesta tela o aluno conseguirá visualizar todas as avaliações disponíveis

## **01. LISTA DE AVALIAÇÕES DISPONÍVEIS**

O sistema irá disponibilizar as aulas dadas seguindo a regra:

Etapa disponível

A etapa esteja com a opção:

* **"Disponível para os aluno"** **marcado**
* **"E**xibe no portal e na central do aluno**"** **marcado**

Ao marcar a opção **"Disponível para os aluno"** de determinada etapa, todas suas avaliações serão liberadas automaticamente. Isso é, quando a etapa de notas é liberada, **TODAS** as avaliações associadas a ela será liberada automaticamente para visualização.

Avaliação disponível

A etapa esteja com a opção:

* **"Disponível para os aluno"** **marcado**

Avaliações com SubTurmas

Para a visualização das notas de avaliações de uma subturma, no qual o aluno está matriculado, segue a seguinte regra:

* Se o aluno estiver matriculado em uma subturma e a turma/disciplina possuir suburma: O sistema deverá exibir apenas as avaliações vinculadas a suburma que está matriculada ou todas que estiverem com a opção "Disponível para todas as Subturmas" **marcada**, ou caso a avaliação não possui nenhuma subturma vinculada;
* Se o aluno estiver matriculado apenas a turma/disciplina e a mesma não possuir suburma: O sistema deverá exibir todas as avaliações da subturma;
* Se o aluno estiver matriculado apenas a turma/disciplina e a mesma possuir subturma: O sistema deverá exibir todas as avaliações da subturma, independente se está ou não vinculada a alguma subturma;
Liberação do professor

O parâmetro "**Permite a visualização das notas das avaliações e faltas somente após a liberação do professor**" caso esteja **marcado**, **o aluno só poderá ter acesso a avaliação e sua nota após liberada.** Este parâmetro se encontra: **Parâmetros | Secretaria | Notas/Faltas**

Imprime no boletim - Ensino Básico**Disponível apenas para o Contexto Ensino Básico**

Ao marcar o parâmetro "**Parâmetros | RM Portal** **| RM Portal - Geral 4/15 |** **Exibir as disciplinas para o aluno de acordo com o campo 'Imprime no boletim' do cadastro de disciplinas da matriz curricular**" , o portal irá apresentar somente as avaliações de disciplinas que estejam com a opção "**Indica se imprime no boletim e exibe no portal do aluno**” **marcada** no cadastro das disciplinas da matriz curricular do aluno.

Casas decimais

A quantidade de "Casas decimais" a ser considerada na tela é configurados conforme o contexto abaixo:

**1º-  Ensino Superior**

No contexto **Ensino Superior**  a informação do número de casas decimais fica disponível dentro do cadastro da disciplina.

**2º-  Ensino Básico**

No contexto **Ensino Básico** a informação do número de casas decimais fica disponível dentro do cadastro da disciplina da grade do aluno. 

**3º-  Itinerário Formativo**

No **Itinerário Formativo** a informação do número de casas decimais fica disponível dentro do cadastro da disciplina do itinerário formativo. 

## **02. LEGENDA**

Será exibido a legenda com informações do status da nota.

* As notas acima da média, serão classificadas com a situação
* As notas abaixo da média, serão classificadas com a situação
* As avaliações que ainda estão aguardando nota, o portal irá considerar a data da prova for menor que a data atual da consulta, e serão classificadas com a situação
* As notas pendentes, o portal irá considerar a data da prova for maior que a data atual da consulta ou com a data da prova em branco, e serão classificadas com a situação
* As notas perdidas, o portal irá considerar que o aluno não obteve nota na avaliação e teve falta no dia em que a mesma foi aplicada, e serão classificadas com a situação
* As avaliações descritivas, são aquelas que no avaliação que estão relacionadas ao TOTVS Avaliação e Pesquisa, e serão classificadas com a situação

## **03. DETALHE DA DISCIPLINA**

Clicando na descrição da disciplina, o aluno poderá ter acesso a listagem da disciplina através no botão “ver mais informações”.

## **04. DETALHE DA AVALIAÇÃO**

Clicando no botão Detalhe, o aluno poderá ter a todas informações da avaliação disponível.

### **04.1 AVALIAÇÃO DESCRITIVA**

Para as avaliações descritivas o portal exibe um nova aba no detalhe da avaliação, onde será exibido a lista de professores que está relacionado com a avaliação descritiva e suas respectivas lista de questões respondidas. Saiba mais sobre

Aluno vinculado a uma avaliação descritiva, porém algum do(s) professor(es) respondeu(am)

O aluno **vinculado a uma avaliação descritiva**, porém **ao algum do(s) professor(es) respondeu(am)**, o portal deverá exibir uma mensagem indicando esta situação.

* Os professores que responderem a avaliação
* Os professores que não responderem a avaliação

Aluno vinculado a uma avaliação descritiva, porém nenhum professor respondeu

O aluno **vinculado a uma avaliação descritiva**, porém **nenhum professor respondeu**, o portal deverá exibir uma mensagem indicando esta situação.

Aluno não vinculado a nenhuma avaliação descritiva

O aluno **não vinculado a nenhuma** **avaliação descrit****iv****a**, o portal deverá exibir uma mensagem indicando esta situação.
