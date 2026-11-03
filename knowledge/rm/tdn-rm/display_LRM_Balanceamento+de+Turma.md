---
content_hash: 578cf9eda2b0fcf1b2deefba4d60f9cd9b8e8e626b4d30c11f9f90fcaffc85a6
fetched_at: '2026-06-29T00:11:36.766491+00:00'
page_id: '773516533'
product: rm
source: tdn-rm
title: Balanceamento de Turma
type: documentation
url: https://tdn.totvs.com/display/LRM/Balanceamento+de+Turma
version: 41
---

## **01**. **VISÃO GERAL**

O balanceamento de turma na matricula de ingressante consiste em distribuir os candidatos entre as turmas respeitando a classificação e a ordem de balanceamento da turma.

Esta funcionalidade está disponível a partir da versão **12.1.2306.115** (será necessário executar o RM Atualizador).

Á partir da versão **12.1.2506.184** foi incluída a implementação que irá permitir o balanceamento de turmas utilizando matrizes curriculares que utilizem controle de vagas "**Por disciplina da turma**" (definições para utilização abaixo).

Exemplo 1

**Matriz aplicada:** Sistema de Informação **Período Letivo:** 2023/1

**Turmas habilitadas para o balanceamento:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| SI 01 - ordem 1 | SI 02 - ordem 2 | SI 03 - ordem 3 | SI 03 - ordem 4 | SI 04 - ordem 5 | SI 05 - ordem 6 |

**Alunos classificados**

1º - Antônio Carlos

2º - Maria Antônia

3º - Flávia Rabelo

4º - Eduardo Silva

5º - João Vitor

6º - Pedro Augusto

7º - Tatiana Alves

8º - Yuri Santana

9º - Jonas Silveira

10º - Mateus Sá

11º - Ana Carolina

12º - Rodrigo Santos

13º - Marcia Andrade (excedente)

14º - Douglas Silva (excedente)

Para simplificar nosso exemplo vamos considerar que cada turma possui 2 vagas **(Nº Máximo de Alunos)**

Veja como ficarão as matriculas dos alunos considerando o balanceamento.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **SI 01** | **SI 02** | **SI 03** | **SI 04** | **SI 05** | **SI 06** |
| 1º - Antônio Carlos | 2º  -Maria Antônia | 3º - Flávia Rabelo | 4º - Eduardo Silva | 5º - João Vitor | 6º - Pedro Augusto |
| 7º - Tatiana Alves | 8º - Yuri Santana | 9º - Jonas Silveira | 10º - Mateus Sá | 11º - Ana Carolina | 12º - Rodrigo Santos |

Exemplo 2

**Matriz aplicada:** Administração **Período Letivo:** 2018/2

**Turmas habilitadas para o balanceamento:**

|  |  |  |
| --- | --- | --- |
| Turma 1 - ordem 1 | Turma 2- ordem 2 | Turma 3 - ordem 3 |

**Alunos classificados**

1º - Isabella Priscila

2º - Ricardo Gabriel

3º - Ian Sérgio

4º - Esther Sônia

5º - Lorenzo Noah

6º - Laís Aparecida

7º - Isabella Helena

8º - Márcia Antônia

9º - Renato Júlio

10° - Lucas Isaac

11° - Tatiane Emanuelly

12° - Jennifer Catarina

Para simplificar nosso exemplo vamos considerar que a Turma 1 possui 6 vagas **(Nº Máximo de Alunos).**

A Turma 2 e  Turma 3 cada uma possui 3 vagas **(Nº Máximo de Alunos)**

**Observação:**caso a matriz aplicada utilize controle de vagas "**Por disciplina da turma**", o número de vagas disponíveis irá considerar a turma/disciplina com menor valor do campo "**Nº Máximo de Alunos**" permitidos ou "**Vagas para calouros**" caso esteja preenchido.

Veja como ficarão as matriculas dos alunos considerando o balanceamento.

|  |  |  |
| --- | --- | --- |
| **Turma 1** | **Turma 2** | **Turma 3** |
| 1º - Isabella Priscila | 2º - Ricardo Gabriel | 3º - Ian Sérgio |
| 4º - Esther Sônia | 5º - Lorenzo Noah | 6º -Laís Aparecida |
| 7º - Isabella Helena | 8º - Márcia Antônia | 9º - Renato Júlio |
| 10º - Lucas Isaac |  |  |
| 11º - Tatiane Emanuelly |  |  |
| 12º - Jennifer Catarina |  |  |

Observe que quando o **número máximo de alunos** da turma for atingida os demais alunos serão alocados nas turmas que ainda possuem vaga, sempre respeitando a ordem de balanceamento da turma e classificação.

## **02. CADASTRO DE TURMA**

Para que a turma faça parte do balanceamento será necessário que a mesma esteja devidamente configurada.

Na aba "**Balanceamento**" deverá ser marcada a opção "**Habilitar balanceamento**" e informar a "**Ordem da turma no balanceamento**".

Conforme a imagem acima será possível visualizar a ordem/turmas já habilitadas para o balanceamento para a mesma matriz aplicada e período letivo.

Regras para permitir o balanceamento:

* O controle de vagas da matriz aplicada está definido como "**Por turma**"
  + O  Nº máximo de alunos deve ser maior que zero
  + Não poderá ter mais de uma turma apontando para a mesma ordem.
  + Não será permitido habilitar o balanceamento para turmas sem matriz aplicada.
* O controle de vagas da matriz aplicada está definido como "**Por disciplina da turma**
  + Não poderá ter mais de uma turma apontando para a mesma ordem.
  + Não será permitido habilitar o balanceamento para turmas sem matriz aplicada.
  + O "**Nº máximo de alunos"**da **turma** será ignorado e será utilizado o "**Nº máximo de alunos**" ou o "**Vaga para calouros**" das turmas/disciplinas cadastradas na turma
  + O "**Nº máximo de alunos"**  ou "**Vagas para calouros"** deve ser maior que zero nas turmas/disciplinas das turmas
  + Caso o campo "**Vagas para calouros"** esteja preenchido, todas as turmas/disciplinas devem ter este campo preenchido, *ele será o padrão utilizado para contagem de vagas disponíveis da turma* e todas as turmas/disciplinas de todas as turmas utilizadas para o balanceamento da mesma matriz aplicada devem ter este campo preenchido.
  + O processo considera o número de vagas disponíveis da turma como sendo a turma/disciplina que tiver menor a quantidade de vagas disponíveis, valor calculado com base no número de vagas da turma/disciplina (**Nº máximo de alunos** ou "**Vaga para calouros)** subtraindo o total de matriculados em cada turma/disciplina (Vagas disponíveis - alunos matriculados), assim ele usa como padrão a turma/disciplina que tiver menos vagas disponível como o padrão de vagas disponível da turma, caso uma única turma/disciplina não tenha mais vagas, a turma será ignorada no balanceamento.
  + Exemplo:
    - Cenário 1: utilizando "**Nº máximo de alunos**" das turmas/disciplinas

      * considerando os dados abaixo, concluímos que a Turma 1 tem 3 vagas disponíveis, a Turma 2, uma vaga e a Turma 3, 0 vagas, ou seja a turma 3 será ignorada no balanceamento por ter pelo menos uma turma/disciplina que tem 0 vagas.

        |  | Turma 1  Qtde de vagas disponíveis = 3 | | | Turma 2  Qtde de vagas disponíveis = 1 | | | Turma 3  Qtde de vagas disponíveis = 0 | | |
        | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
        |  | Nº máximo de alunos | Alunos matriculados | Vagas disponíveis | Nº máximo de alunos | Alunos matriculados | Vagas disponíveis | Nº máximo de alunos | Alunos matriculados | Vagas disponíveis |
        | Disciplina 1 | 5 | 0 | 5 | 5 | 0 | 5 | 5 | 0 | 5 |
        | Disciplina 2 | 5 | 2 | 3 | 5 | 0 | 5 | 5 | 5 | 0 |
        | Disciplina 3 | 5 | 1 | 4 | 5 | 4 | 1 | 5 | 2 | 3 |
    - Cenário 2: utilizando "**Vagas para calouros**" das turmas/disciplinas
      * considerando os dados abaixo, concluímos que a Turma 1 tem 3 vagas disponíveis, a Turma 2, uma vaga e a Turma 3, 2 vagas.

        |  | Turma 1  Qtde de vagas disponíveis = 3 | | | Turma 2  Qtde de vagas disponíveis = 1 | | | Turma 3  Qtde de vagas disponíveis = 2 | | |
        | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
        |  | Vagas para calouros | Alunos matriculados | Vagas disponíveis | Vagas para calouros | Alunos matriculados | Vagas disponíveis | Vagas para calouros | Alunos matriculados | Vagas disponíveis |
        | Disciplina 1 | 5 | 0 | 5 | 5 | 0 | 5 | 5 | 0 | 5 |
        | Disciplina 2 | 5 | 2 | 3 | 5 | 0 | 5 | 5 | 3 | 2 |
        | Disciplina 3 | 5 | 4 | 1 | 5 | 4 | 1 | 5 | 2 | 3 |

**Facilitador:**

Ao marcar a opção "**Habilitar balanceamento**" o campo "**Ordem da turma no balanceamento**" será preenchido automaticamente com a próxima ordem levando em consideração as turma já habilitadas para o mesmo período letivo e matriz aplicada.

## **03. MATRÍCULA**

O balanceamento de turma será aplicado durante a matricula somente se a opção "**Realizar enturmação aplicando o balanceamento de turmas**" estiver marcada.

**Processo Seletivo RM / Matricular:**

**Processo Seletivo RM / Matricular em lote:**

Ao selecionar o período letivo é verificado se existe alguma turma habilitada para o balanceamento, caso exista alguma turma a opção "**Realizar enturmação aplicando o balanceamento de turmas**" será marcada automaticamente e será apresentada a mensagem abaixo.

Lembrando que a opção é marcada de forma sugestiva, podendo o usuário desmarcar caso opte por não aplicar o balanceamento.

Após o processamento da matrícula os alunos serão matriculados nas turmas conforme o balanceamento processado pelo sistema levando em consideração a ordem de classificação e ordem de balanceamento das turma.

Ao executar a matricula são carregadas as turmas habilitadas para o balanceamento, consideradas somente aquelas vinculadas a matriz aplicada da área ofertada e período letivo que foi informado no processo de matrícula.

Posteriormente será executado o balanceamento conforme as regras descritas no inicio deste documento .

Ao término da matricula será apresentado um log, onde será possível visualizar a alocação dos alunos nas turmas conforme o balanceamento aplicado.

Se a opção "**Realizar enturmação aplicando o balanceamento de turmas**" não for marcada a matrícula será processada considerando a turma informada no processo.

Ao marcar o parâmetro abaixo será possível matricular mais alunos em turmas que já excederam o máximo de alunos parametrizados. O balanceamento continuará acontecendo normalmente até que todos alunos sejam matriculados.

**Área de interesse ofertada / Matrícula / Perfil do Usuário**

**Processo Seletivo RM / Matricular / Perfil do usuário**

## **04. MATRÍCULA EM DISCIPLINAS COM SUBTURMAS**

Caso nas turmas em que o balanceamento distribuiu os alunos possuam disciplinas e estas disciplinas possuam subturmas, o processo de matrícula também irá distribuir de forma balanceada os alunos nas subturmas das disciplinas. 

Importante

Esta funcionalidade está disponível a partir da versão **12.1.2306.134.**

A distribuição dos alunos será sempre buscando equilibrar as subtumas, ordenando as subturmas pelo nome, conforme exemplo abaixo:

Exemplo

**Turma**: Turma 1 |  **disciplina**: Laboratório

| Laboratório - SubTurma1 | Laboratório - SubTurma2 | Laboratório - SubTurma3 |
| --- | --- | --- |

**Alunos matriculados na Turma 1 e na disciplina Laboratório que possui três subturmas:**

1º - Isabella Priscila

2º - Ricardo Gabriel

3º - Ian Sérgio

4º - Esther Sônia

5º - Lorenzo Noah

6º - Laís Aparecida

7º - Isabella Helena

8º - Márcia Antônia

9º - Renato Júlio

10° - Lucas Isaac

Distribuição dos alunos após o balanceamento:

| Laboratório - SubTurma1 | Laboratório - SubTurma2 | Laboratório - SubTurma3 |
| --- | --- | --- |
| 1º - Isabella Priscila | 2º - Ricardo Gabriel | 3º - Ian Sérgio |
| 4º - Esther Sônia | 5º - Lorenzo Noah | 6º - Laís Aparecida |
| 7º - Isabella Helena | 8º - Márcia Antônia | 9º - Renato Júlio |
| 10° - Lucas Isaac |  |  |

### Choque de horários na subturmas

Se na matrícula o parâmetro "Matriculas alunos com choque de horários" esteja desmarcada, caso ocorra choque de horários, ou seja, caso existam disciplinas da turma que possuam subturmas com horários que conflitem com outras subturmas de outras disciplinas da mesma turma, o sistema irá fazer a realocação do aluno em outra subturma até que não exista choque de horário em nenhuma subturma das disciplinas, porém, caso ainda sim o sistema não encontre uma subturma que não irá conflitar com outras o processo será abortado com o log informando o conflito de horário da subturma.
