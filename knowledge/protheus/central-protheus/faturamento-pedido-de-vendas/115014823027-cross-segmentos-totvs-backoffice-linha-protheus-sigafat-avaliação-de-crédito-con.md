---
article_id: 115014823027
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 58a305622d51daf31c655bc161552cc90977c467c8b22137676dec0a18a263a4
fetched_at: '2026-06-28T22:38:41.095541+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Avaliação de
  Crédito considerando Impostos
type: support-article
updated_at: '2022-08-31T13:56:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115014823027-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Avalia%C3%A7%C3%A3o-de-Cr%C3%A9dito-considerando-Impostos
---

**Dúvida**

Gostaria de saber se existe alguma parametrização no sistema para que o mesmo faça a avaliação de crédito do pedido de venda considerando o valor de Impostos.  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- versão 11 e versão 12

**Solução**

Não há como parametrizar, por que no momento da análise de crédito os impostos não foram calculados, você só tem uma prévia desse cálculo na visualização da planilha financeira, mas o cálculo mesmo somente será efetuado na geração da nota de saída.

Se há necessidade de compor o saldo do cliente com impostos, você terá que tratar via ponto de entrada, no momento de liberar o pedido via mata440, podendo utilizar MAAVCREFIN <https://tdn.totvs.com/x/xAdxEg> .

Segue também outros pontos para utilização na avaliação de crédito:  
  
MAAVCRPR: <https://tdn.totvs.com/x/LYVn>   
MAAVCRED: <https://tdn.totvs.com/x/LIVn>   
MTVALAVC -<https://tdn.totvs.com/x/sYVn>

**Saiba mais sobre avaliação de crédito:**

**[MP - FAT -Como identificar a causa de o Pedido de Venda ter sido liberado/bloqueado por Crédito "indevidamente"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001428228-MP-FAT-Como-identificar-a-causa-de-o-Pedido-de-Venda-ter-sido-liberado-bloqueado-por-Cr%C3%A9dito-indevidamente-)**

**[MP - FAT - Configurações para bloqueio de crédito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017748031-MP-FAT-Configura%C3%A7%C3%B5es-para-bloqueio-de-cr%C3%A9dito)**

**[MP - FAT - Qual a funcionalidade do parâmetro MV\_GERABLQ na liberação do Pedido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047411193-MP-FAT-Qual-a-funcionalidade-do-par%C3%A2metro-MV-GERABLQ-na-libera%C3%A7%C3%A3o-do-Pedido)**
