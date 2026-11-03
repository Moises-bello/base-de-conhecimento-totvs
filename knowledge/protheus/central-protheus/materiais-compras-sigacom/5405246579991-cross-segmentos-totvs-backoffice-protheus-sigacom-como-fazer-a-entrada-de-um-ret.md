---
article_id: 5405246579991
category: Materiais - Compras (SIGACOM)
content_hash: 0430b5da616a45465dfce0b12b92b5605541dd3c8299c938b06dd0a707c28fde
fetched_at: '2026-06-28T22:41:15.861719+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como fazer a entrada
  de um Retorno de Beneficiamento que não foi aceito pelo cliente?
type: support-article
updated_at: '2022-04-12T18:15:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5405246579991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-fazer-a-entrada-de-um-Retorno-de-Beneficiamento-que-n%C3%A3o-foi-aceito-pelo-cliente
---

**Dúvida**Fiz a entrada de um beneficiamento e posteriormente seu retorno porém o cliente recusou o documento. Agora necessito fazer a entrada desse retorno, como proceder ?

**OBS: CASOS EM QUE IRÁ RETORNAR NOTA FISCAL E PRODUTO ou SOMENTE NOTA FISCAL**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões.

**Solução**Por padrão não temos o conceito de dar entrada em uma devolução sendo o próprio documento uma devolução/retorno de beneficiamento.

Porém um processo paliativo nesse sentido seria:

-Fazer a entrada tipo "B" - Beneficiamento  
-Puxar os dados do cliente, produtos, valores e quantidade manualmente:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5404845591831/mceclip0.png)

-No campo nota fiscal origem na linha do item informar a nota origem e série origem, **somente de forma informativa (o sistema não fará vínculo automático)**, digitar os números da nota e série da nota de retorno (que está querendo cancelar).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5404910471575/mceclip1.png)

- Poderá ser colocada a TES que utilizou na primeira entrada, alimentando o poder de terceiro. Porém o novo retorno deverá ter a amarração dessa segunda entrada.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[PODER DE TERCEIRO](https://tdn.totvs.com/pages/releaseview.action?pageId=285642640)
