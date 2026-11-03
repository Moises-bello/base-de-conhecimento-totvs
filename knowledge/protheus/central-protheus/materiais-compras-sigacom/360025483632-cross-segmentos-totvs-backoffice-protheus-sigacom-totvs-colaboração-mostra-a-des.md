---
article_id: 360025483632
category: Materiais - Compras (SIGACOM)
content_hash: ea006226b36a9ba0cacd14113a008a31c84f2ef8ab575a7ef9e1f4d81cda4158
fetched_at: '2026-06-28T22:41:10.469426+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Totvs Colaboração mostra
  a descrição do código CKO_CODERR na opção reprocessar
type: support-article
updated_at: '2022-05-16T21:00:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025483632-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Totvs-Colabora%C3%A7%C3%A3o-mostra-a-descri%C3%A7%C3%A3o-do-c%C3%B3digo-CKO-CODERR-na-op%C3%A7%C3%A3o-reprocessar
---

**Dúvida**

Totvs Colaboração mostra a descrição do código CKO\_CODERR na opção reprocessar  
  
**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

Deve-se utilizar a função COLERROERP(cCod).

COMXCOL, reprocessar os arquivos, opção 3/CKO\_CODERR , está mostrando arquivos com erro, há o campo virtual onde é apresentado o código de erro para que o cliente possa identificar de onde vem a descrição do código do erro.
