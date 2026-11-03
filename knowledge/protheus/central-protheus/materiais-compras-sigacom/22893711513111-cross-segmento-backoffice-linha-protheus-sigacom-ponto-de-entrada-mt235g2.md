---
article_id: 22893711513111
category: Materiais - Compras (SIGACOM)
content_hash: 0b5ee3e006f023d088ffbf7d0877e4fa01e00fef8afee1d3a762a2114b8a97b1
fetched_at: '2026-06-28T22:41:11.483964+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Ponto de Entrada -
  MT235G2
type: support-article
updated_at: '2024-04-18T15:06:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22893711513111-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Ponto-de-Entrada-MT235G2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22893691567255) Tempo aproximado para leitura: **00:03:SS min** **Dúvida**

Como podemos validar se haverá a eliminação de resíduos no pedido de compras?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões  
  
**Solução**

O Ponto de Entrada MT235G2 permite validar se haverá ou não eliminação de resíduo no pedido de compras

O Ponto de entrada é executado antes da eliminação de resíduo, item por item, conforme parametrização realizada antes de processar.

Descrição :

**Exemplo do Ponto MT235G2:**

User Function MT235G2( )

Local aPram := ParamIXB  
Local lRet := .T.

If lRet  
            Alert("Passou pelo PE MT235G2")  
Endif

Return(lRet)

**F =** Não elimina resíduo do item, **T =** Continua com o processo de eliminação de resíduo do item;

![000MT235G2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22893711502359)

Saiba mais em :

[Ponto de entrada MT235G2](https://tdn.totvs.com/display/public/PROT/MT235G2)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
