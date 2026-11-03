---
article_id: 4414389641623
category: Faturamento - Integrações
content_hash: fb25dbe1240be1d75f859718150df29991c0de51f0082f15486755f82db981db
fetched_at: '2026-06-28T22:38:26.549311+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - TES Inteligente
  duplica o financeiro Vtex x Protheus
type: support-article
updated_at: '2021-11-29T14:55:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414389641623-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-TES-Inteligente-duplica-o-financeiro-Vtex-x-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao utilizar o TES Inteligente em um pedido de venda incluído pelo Vtex, o sistema esta gerando os títulos novamente, fazendo com que o financeiro fique duplicado.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões  
  
**Causa**O TES utilizado na venda pelo Vtex é informado no parâmetro **[MV\_LJTESPE](https://tdn.totvs.com/x/lQV_HQ)**, esse TES não deve gerar movimento financeiro, campo **"Gera Dupl." (F4\_DUPLIC)** igual a "**Não**". Pois o financeiro é gerado pelas rotinas de varejo (GravaBatch) no momento que o pedido é criado, colocando para não gerar, não será gerado no momento que o pedido for faturado no módulo de faturamento.

Para utilização da TES Inteligente, onde o Pedido gerado no Loja deverá gerar financeiro e o Pedido gerado no Faturamento não deverá gerar, o TOTVS Connector deve enviar o tipo de operação (tag OperationCode) diferente de "V".  Para seguir o padrão do Loja, enviar a tag com "01".

**Solução**Para evitar a Duplicidade na geração do Financeiro no processo de integração do Vtex com o Protheus:

1. O TES informado no parâmetro **MV\_LJTESPE** não deve gerar Financeiro "Gera Dupl." (**F4\_DUPLIC**) igual a "Não";

2. O TES sugerido pelo TES Inteligente, também não deve gerar financeiro "Gera Dupl." (F4\_DUPLIC) igual a "Não";

O Título será gerado pela rotina automática do SIGALOJA (GravaBatch), os demais movimentos executados no sistema não devem conter movimentação financeira.

**Saiba mais**: **[Guia de uso - Integração do Pedido Loja(Venda Assistida) com VTEX](https://tdn.totvs.com/x/tNrvI)**
