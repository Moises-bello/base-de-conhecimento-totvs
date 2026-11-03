---
article_id: 33250571706007
category: Materiais - Compras (SIGACOM)
content_hash: ed8b132781c99162bc5f91a5f8b22d17817cb190c7d60de2b97e11336f808216
fetched_at: '2026-06-28T22:41:10.110712+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ocorre o erro variable
  is not array - Type [C] ao executar a rotina SCHEDCOMCOL.
type: support-article
updated_at: '2025-07-04T12:51:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33250571706007-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ocorre-o-erro-variable-is-not-array-Type-C-ao-executar-a-rotina-SCHEDCOMCOL
---

**Dúvida**  
Ocorre o erro variable is not array - Type [C] ao executar a rotina SCHEDCOMCOL.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Solução**

Esse erro ocorre quando o conteúdo do parâmetro MV\_COLEDI está fora do colchete, desse modo o sistema considera o conteúdo do parâmetro como caracter, enquanto deveria considerar como uma lista (array).

Para correção do erro basta alterar o parâmetro MV\_COLEDI, colocando o seu conteúdo entre colchetes{}, conforme o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33250571702679)

***Saiba Mais:***

[Parâmetros Importador XML](https://tdn.totvs.com/pages/releaseview.action?pageId=485869217)

[Pontos de Entrada disponíveis no Importador XML](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)

[CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
