---
article_id: 25473693745175
category: Financeiro - Liquidação a Receber
content_hash: a329f9fda9392f699f453b62e94bad0094de725837a7eb5536ea65e16b09fa6a
fetched_at: '2026-06-28T22:37:42.284692+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA460 - Liquidação
  a Receber
type: support-article
updated_at: '2026-05-19T17:20:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25473693745175-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA460-Liquida%C3%A7%C3%A3o-a-Receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25479330474007) Tempo aproximado para leitura: **00:04:00 min**

**Ocorrência**  
Como efetuar a Liquidação a Receber (FINA460)?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**  
Esta rotina é responsável pela quitação das dívidas pendentes com Clientes. Após a negociação, poderá resultar na criação de um ou mais títulos a receber, conforme os termos de pagamento acordados.

**Contabilização**:  
A contabilização dos títulos gerados por esta rotina pode ser realizada por meio dos lançamentos padrão

• **LP 500** - Na inclusão de títulos no Contas a Receber.

• **LP 505** - No exclusão de títulos do Contas a Receber.

• **LP 520** - Na baixa de títulos Cobrança Simples/Protesto/Acordo no Contas a Receber (0/F/G).

• **LP 521** - Na baixa de títulos Cobrança Simples/Cartório no Contas a Receber (1/H).

• **LP 522** - Na baixa de títulos Cobrança Descontada no Contas a Receber (2).

• **LP 523** - Na baixa de títulos Cobrança Caucionada no Contas a Receber (3).

• **LP 524** - Na baixa de títulos Cobrança Vinculada no Contas a Receber (4).

• **LP 525** - Na baixa de títulos Cobrança Advogado no Contas a Receber (5).

• **LP 526** - Na baixa de títulos Cobrança Judicial no Contas a Receber (6).

• **LP 527** - No cancelamento da baixa de títulos no Contas a Receber.

• **LP 528** - Na baixa de títulos Cobrança Caucionada Descontada no Contas a Receber (7).

• **LP 598** - Na geração de variação monetária, ou seja, liquidação e geração de novos títulos na mesma moeda (exceto quando moeda 1) (apenas online)

**Importante**  
A rotina de **Contabilização de Variação Monetária (FINA350)** é a responsável por gerar os registros referentes à **variação monetária nas tabelas SE5 e FK6** dos títulos baixados pela **Liquidação de contas a receber (FINA460)**. Portanto, a contabilização do **LP 598** sempre será online na liquidação.

Caso a pergunta **"Mostra lançamento contábil?**" da rotina de **liquidação a receber (FINA460)** esteja configurada como **"Sim"**, a tela de **lançamento contábil** do **LP 598** será exibida, porém, à parte dos demais lançamentos, por se tratar de um processo executado paralelamente pela rotina de **Contabilização de Variação Monetária (FINA350)**. Utilizar a variável privada **VALOR** ou a tabela **FK6** para contabilizar o valor da **variação monetária** nesse LP.

• **LP 59A** - No estorno da variação monetária (apenas online).

**Liquidação**

**![liquidação fina460.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25473725591447)**

**Reliquidação**

Os títulos gerados por essa rotina também podem ser renegociados. Nesse caso, a ação é denominada reliquidação.

**![Gravar_2024_08_07_11_53_17_663.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25473725592983)**

**Estorno Liquidação ou Reliquidação**

**![Gravar_2024_08_07_11_55_57_186.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25473693729047)**

**Base reduzida de impostos**  
Em situações de renegociação, os impostos retidos na baixa e suas respectivas bases serão transferidos para os novos títulos gerados, sempre que a **Natureza da Liquidação** permitir o cálculo desses impostos. Os impostos que não forem calculados pela **Natureza da Liquidação** serão desconsiderados.

A rotina apresenta certas particularidades que podem ser verificadas no link oficial abaixo.

**Saiba mais**  
[Liquidação a Receber - FINA460](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275)
