---
article_id: 360004835251
category: Materiais - Compras (SIGACOM)
content_hash: 4b467627e073a4a885e648edde1b7c287efe986cb54dcd3d1b2a49e36aa2f17d
fetched_at: '2026-06-28T22:41:10.483605+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus- SIGACOM -  Help A140ESFORP ao
  estornar Documento de Entrada
type: support-article
updated_at: '2022-05-16T22:04:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004835251-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A140ESFORP-ao-estornar-Documento-de-Entrada
---

**Dúvida:**Help A140ESFORP ao estornar Documento de Entrada  
  
**Ambiente:**

Microsiga protheus - Compras – A partir da versão 12.1.017

**Solução**

Para o estorno, a exclusão deverá ser realizada através da rotina Documento de Entrada - MATA103.

Sendo apresentada a mensagem "Não foi possível excluir a(s) nota(as), pois o prazo para o cancelamento da(s) NF-e é de 24 horas", será necessário alterar o parâmetro MV\_SPEDEXC com conteúdo maior que 24.

**Importante:** Após exclusão o parâmetro MV\_SPEDEXC deverá ser retornado ao seu valor default '24'.

**Observação:** Após a exclusão, para o cancelamento do documento na SEFAZ acesse a rotina NFESEFAZ e transmita a numeração da nota excluída, assim o sistema enviará o cancelamento para a SEFAZ.  
Acesse o monitor para verificar se obteve retorno de Cancelamento Autorizado

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
