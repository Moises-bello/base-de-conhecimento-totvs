---
article_id: 19571116754199
category: SIGAEST - CUSTOS
content_hash: 465d14249b0cb083a243a034c9217d8981511d707a11a64c37a859d020e9af95
fetched_at: '2026-06-28T22:39:02.301225+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - PE MTA190D1 - Manipulação
  do valor do custo do Documento de Entrada
type: support-article
updated_at: '2025-03-12T12:25:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19571116754199-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-PE-MTA190D1-Manipula%C3%A7%C3%A3o-do-valor-do-custo-do-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19571121730967) Tempo aproximado para leitura: **00:03:20 min****Dúvida**Como efetuar a manipulação do custo de entrada com PE? utilizando o PE MTA190D1?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Descrição:**

Manipula valores de custo da NF de entrada (SD1).

**Localização:**

Function Recalc() - Responsável por recalcular o custo de entrada.

**Em que ponto:**

O ponto é acionado antes de regravar o custo no arquivo de itens de NF de entrada (SD1).

**Programa Fonte:**

MATA190.PRX

**Sintaxe:**

MTA190D1() - Manipulação do valor do custo da NF de entrada ( < PARAMIXB> ) --> aRet

**Parâmetros:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | PARAMIXB[1] |  |  | Vetor |  |  | O programa recebe como parâmetro um array contendo os custos que serão gravados pelo sistema no arquivo SD1. |  |  |  |  |  | X |  |  |  |  |
|  | PARAMIXB[2] |  |  | Vetor |  |  | O programa recebe como parâmetro um array contendo os custos, número da nota, série e número do item. |  |  |  |  |  |  |  |  |  |  |

**Retorno**: aRet

```
#INCLUDE "PROTHEUS.CH"

User Function MTA190D1()

Local aCustEnt := PARAMIXB[1]
Local aItem := PARAMIXB[2]
local nCusto1
local ncusto2
local ncusto3
local ncusto4
local ncusto5
local cDoc
local cSerie
local nitem
local aCusRet

aCusRet := aclone(aCustEnt)
// ordenação do array n = D1_FILIAL+D1_DOC+D1_SERIE+D1_FORNECE+D1_LOJA+D1_COD+D1_ITEM
nCusto1 := aCustEnt[n, 1]
nCusto2 := aCustEnt[n, 2]
nCusto3 := aCustEnt[n, 3]
nCusto4 := aCustEnt[n, 4]
nCusto5 := aCustEnt[n, 5]

// aItem mesma ordenação n = D1_FILIAL+D1_DOC+D1_SERIE+D1_FORNECE+D1_LOJA+D1_COD+D1_ITEM porem com referencia da nota e item
nCusto1 := aItem[n, 1]
nCusto2 := aItem[n, 2]
nCusto3 := aItem[n, 3]
nCusto4 := aItem[n, 4]
nCusto5 := aItem[n, 5]
cDoc := aItem[n, 6, 1]
cSerie := aItem[n, 6, 2]
nItem := aItem[n, 6, 3]

// IMPORTANTE não mudar a ordenação do array de saida
aCusret[n, 1] := aCustEnt[n, 1] // ou aItem[n, 1]
aCusret[n, 2] := aCustEnt[n, 2] // ou aItem[n, 2]
aCusret[n, 3] := aCustEnt[n, 3] // ou aItem[n, 3]
aCusret[n, 4] := aCustEnt[n, 4] // ou aItem[n, 1]
aCusret[n, 5] := aCustEnt[n, 5] // ou aItem[n, 1]

return (aCusret)
```

**Observações:**Cada elemento do PARAMIXB[1] se refere ao item na SD1, a ordenação do index é D1\_FILIAL+D1\_DOC+D1\_SERIE+D1\_FORNECE+D1\_LOJA+D1\_COD+D1\_ITEM. O ponto de entrada deve retornar o array com o custo nas 5 moedas. No PARAMIXB[2], segue o mesmo index do PARAMIXB[1], porém, contém os valores D1\_DOC, D1\_SERIE e D1\_ITEM.

**--Atenção:** Todos os modelos passados, são apenas exemplos, o seu desenvolvedor devera avaliar qual regra melhor se adequa para sua necessidade.

caso utilize estes e o resultado seja diferente do documentado ou apresente falha, caso não disponha de analista programador para realizar os ajustes, dispomos do serviço do time Hub Plataformas ([hub.plataformas@totvs.com.br](mailto:hub.plataformas@totvs.com.br)).

Esta equipe oferece os serviços de criação e manutenção de fontes Protheus, que tem como característica a disponibilidade de um recurso remoto para realização desta atividade em horários comerciais (dias úteis das 08:00 às 18:00).

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
