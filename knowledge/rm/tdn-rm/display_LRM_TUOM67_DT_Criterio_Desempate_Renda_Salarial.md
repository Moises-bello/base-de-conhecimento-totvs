---
content_hash: f56cb31b299f1568a40f160822b48ba5c4c82b473ecc8d1980b79bf5a3bb39a9
fetched_at: '2026-06-29T00:08:12.165426+00:00'
page_id: '243637597'
product: rm
source: tdn-rm
title: TUOM67_DT_Criterio_Desempate_Renda_Salarial
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOM67_DT_Criterio_Desempate_Renda_Salarial
version: 121
---

# CLASSIFICAÇÃO - CRITÉRIO DE DESEMPATE - LEI Nº 13.184

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Processo Seletivo** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Classificar candidatos* | *N/A* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | ***Critérios de desempate*** | *N/A* | |
| **Cadastros Iniciais:** | *Cadastrar um processo seletivo com áreas ofertadas e etapas para que a classificação por nota utilize critérios de desempate.* |
| **Parâmetro(s):** | - |
| **Ponto de Entrada:** | *Sistema:*  *Cadastros | Critérios de desempate*  *Cadastros | Processo Seletivo | Classificar candidatdos* |
| **Chamados Relacionados** | **N/A** |
| **Requisito (ISSUE):** | - |
| **País(es):** | - |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *SPSTIPOCRITERIO* |
| **Sistema(s) Operacional(is):** | - |

## Descrição

O que a lei define:

LEI Nº 13.184, DE 4 DE NOVEMBRO DE 2015: "No caso de empate no processo seletivo, as instituições públicas de ensino superior darão prioridade de matrícula ao candidato que comprove ter renda familiar inferior a dez salários mínimos, ou ao de menor renda familiar, quando mais de um candidato preencher o critério inicial."

Para atendimento da legislação foi criado a função de fórmula "PSDNRendaSalarioQuestSocioEconomico", esta função retorna a resposta do candidato no questionário socioeconômico referente a renda familiar, porém para que a função de fórmula funcione é necessário criar uma fórmula (fórmula descrita no procedimento de utilização deste documento) que informará para a função qual é a questão exata do questionário que contém as informações da renda salarial informada pelo candidato. Com base na ordem da resposta do candidato o sistema irá comparar os candidatos utilizando a renda de referência definida (no caso da lei dez salários) na fórmula e utilizará como critério de desempate quando a fórmula criada for definida como critério de desempate para as áreas ofertadas do processo seletivo.

## Procedimento para Implantação

```
O sistema é atualizado logo após a aplicação do release 12.1.12 ou superior.
```

## Procedimento para Utilização

## Sistema

O critério de desempate de renda salarial por fórmula depende de alguns itens para seu correto funcionamento.

### Questionário (Totvs Avaliação e Pesquisa)

O questionário que foi definido no processo seletivo, deve ter ao menos uma questão com opções que atendam ao mínimo da renda de referência, ou seja, se a lei define que são dez salários, a questão deve ter no mínimo dez opções, uma para faixa salarial, exemplo abaixo:

```
a) Um
```

```
b) Dois
```

```
c) Três
```

```
d) Acima de quatro
```

O critério de desempate utilizará desta ordem para identificar qual a renda do candidato, sendo assim se o candidato marcar a letra 'b' sua renda salarial é de até dois salários mínimos, neste caso a ordem das opções se torna de extrema importância para o funcionamento correto da fórmula.

**OBS:** Caso o questionário já exista e seja inviável a criação de um novo, é possível criar a questão com as definições acima e adicionar no questionário, desativando a questão 'antiga', sendo que também é possível ordenar as questões para melhor interpretação do questionário pelo candidato, utilizando o processo de "ordenar questões" no cadastro de provas.

### Processo Seletivo (Totvs Processo Seletivo)

#### Definição da fórmula

No cadastro de fórmulas, deverá ser cadastrada a fórmula utilizando corretamente o código da área, da matéria e o código da questão, estes dados são extremamente importantes pois garantem à fórmula a obtenção da renda informada pelo candidato.

**OBS**: substitua corretamente na fórmula os códigos destacados em vermelho da área, matéria e da questão  referente a renda salarial do questionário nas linha 5, 6 e 7 da fórmula:

**SETVAR**(CODAREA, '**CODAREA**’); /\*Preencha corretamente este campo\*/

**SETVAR**(CODMATERIA, '**CODMATERIA**'); /\*Preencha corretamente este campo\*/

**SETVAR**(CODQUESTAO, '**CODQUESTAO**'); /\*Preencha corretamente este campo\*/

Segue exemplo da fórmula:

250

#### Critério de desempate

Após a criação da fórmula, deverá ser criado o critério de desempate através do menu "cadastros | critérios de desempate", associando o processo seletivo e as áreas ofertadas do processo seletivo, que serão utilizados no processo se classificação de candidatos por nota.

divs
