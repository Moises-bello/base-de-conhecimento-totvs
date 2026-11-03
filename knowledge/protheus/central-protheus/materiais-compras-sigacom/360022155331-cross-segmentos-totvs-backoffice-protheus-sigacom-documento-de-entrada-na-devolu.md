---
article_id: 360022155331
category: Materiais - Compras (SIGACOM)
content_hash: 56bf29f91fdbbdc1983f2483c4cb197d38e0c83e2a8518ce9714112d83999ea8
fetched_at: '2026-06-28T22:41:17.345658+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de Entrada
  - Na Devolução de uma Venda serem listadas somente notas ainda não retornadas
type: support-article
updated_at: '2022-03-23T18:23:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022155331-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-Entrada-Na-Devolu%C3%A7%C3%A3o-de-uma-Venda-serem-listadas-somente-notas-ainda-n%C3%A3o-retornadas
---

**Dúvida**Como parametrizar o sistema para que ao fazer uma **nota de devolução de vendas/ retorno de beneficiamento** no **D****ocumento de Entrada** seja apresentada para **seleção** somente as notas que ainda não foram retornadas.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS - Gestão de Compras.  
  
**Solução**  
Para que seja apresentado somente as notas que tenham saldo a serem devolvidos, poderá habilitar o parâmetro : **MV\_FLAGDEV**.  
  
O parâmetro foi criado para que haja melhora na **performance** do retorno de notas de venda, pois ao filtrar todas as notas, sendo as já devolvidas ou não, em um ambiente que apresentem muitos **registros na tabela SD2**, o sistema apresentava lentidão.

Também é controlado o retorno de beneficiamento de nota que já foram retornadas. (**Controle Poder de Terceiro**)

***Saiba mais :***

[3777355 DMANMAT02-12838 DT Lentidão ao retornar nota de venda](http://tdn.totvs.com/pages/releaseview.action?pageId=439704124)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
