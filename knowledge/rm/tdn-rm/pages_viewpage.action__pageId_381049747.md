---
content_hash: 2f7491b702bd3fd15cb5f6a068621585caf4f577bff2d5ae71195bd75c0dcd39
fetched_at: '2026-06-29T00:09:03.557475+00:00'
page_id: '381049747'
product: rm
source: tdn-rm
title: Plano de Aula.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381049747
version: 100
---

A tela de Plano de Aula, tem o objetivo de exibir todas as aulas disponíveis para o aluno, de todas as disciplinas do período letivo em um determinado dia.

## **01.****ACESSO A TELA**

O acesso para esta tela pode ser através de três lugares acessos:

### **01.1** Menu de Plano de Aula

Através do menu lateral "Plano de aula" a tela será redirecionado para a tela de plano de aula **filtrando o data atual**.

Essa funcionalidade está disponível a partir do patch 12.1.2205.227

### 

### **01.2** Tela de Calendário

Através do botão "Visualizar todas as aulas do dia" contido no modal de informações da Aula, acessada através de um duplo clique em um determinado dia do Calendário. A tela será redirecionado para a tela de plano de aula filtrando a **data selecionada no calendário**.

### **01.3**  Widget "Acontecendo hoje"

Através do link chamado "Detalhar aulas do dia" contido no Widget "Acontecendo hoje". A tela será redirecionado para a tela de plano de aula **filtrando o data atual**.

## **02.** **LISTA DE PLANOS DE AULAS**

Serão listados todas as aulas do aluno daquele dia, de todas as disciplinas do período letivo selecionado no contexto.

Informações do plano de aula

Serão exibidos as seguintes informações de cada aula do aluno:

* Número da aula
* Nome da disciplina
* Turma
* Sub-turma: Somente se possuir a sub-turma cadastrada no plano de aula
* Tipo da aula
* Horário de início e fim da aula
* Local (Prédio, Bloco e Sala): Somente se possuir o Local (Ou prédio, ou bloco ou sala) cadastrado no plano de aula
* Conteúdo previsto
* Conteúdo realizado
* Lição de casa
* Arquivos da disciplina para download

As informações de conteúdo previsto, conteúdo realizado, lição de casa e arquivos da disciplina serão exibidos ocultos para otimizar a visualização da lista de aulas. Se possuir algumas das informações de conteúdo previsto, conteúdo realizado, lição de casa ou arquivos disponíveis para download, será exibido um subgrupo com um link chamado "**Exibir detalhes**" para expandir a visualização destas informações de cada disciplina.

Anexo

Aulas que possuem algum arquivo disponível para download terão a identificação de um ícone de clips ao lado do número da aula, indicando para o aluno que esta aula possui um arquivo disponível para download. Isso facilita a identificação rápida de aulas que possuem arquivos disponíveis.

Detalhe da aula

Essa funcionalidade está disponível a partir do patch 12.1.2205.227

O portal possui a funcionalidade de visualizar todos os detalhe da aula através do clique sobre o número do plano de aula. Sendo assim redirecionando para um nova tela com mais detalhes da aula.

**IMPORTANTE:**

* Caso o aluno possua o parametro de **horário independentes** (**MARCADO**) deve ficar atento a seguinte regra:
  + Caso o parâmetro esteja marcado e o aluno **NÃO** possua subturma deve mostrar apenas os horários das disciplinas em que o aluno foi matriculado.
  + Caso o parâmetro esteja marcado os horários apresentados devem ser todos os relacionados a turma/disciplina no qual o aluno esta matriculado e todos os horários das subturmas que o aluno esta matriculado.

* Caso o aluno possua o parametro de **horário independentes** (**DESMARCADO**) deve ficar atento a seguinte regra:
  + - Caso o parâmetro esteja marcado e o aluno **NÃO**esteja matriculado em nenhuma subturma, deve trazer os horários vinculados a turma/disciplina.
      * Caso o aluno esteja matriculado em uma subturma, segue as regras:
        + Se a subturma possuir horário vinculado, traz os horários vinculados a subturma e a turma/disciplina.
        + Se a subturma **NÃO**possuir horário vinculado, traz os horários vinculados a turma/disciplina.

**OBS:**

* O parâmetro de horário independentes fica localizado em:
  + Educacional → Educacional → Ambiente → Parâmetros → Educacional → Secretaria → Geral 2/7

*divs*
