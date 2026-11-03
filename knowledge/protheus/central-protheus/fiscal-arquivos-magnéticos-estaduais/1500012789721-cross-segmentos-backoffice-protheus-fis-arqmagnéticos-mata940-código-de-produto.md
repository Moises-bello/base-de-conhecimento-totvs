---
article_id: 1500012789721
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 096063edcdf64cfece751a43e5bcbbdc2b195a863ec707d3c10c0307a8aef0b0
fetched_at: '2026-06-28T22:42:11.788960+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - MATA940 - CÓDIGO
  DE PRODUTO NO ARQUIVO DO SINTEGRA
type: support-article
updated_at: '2022-08-18T14:16:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012789721-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-MATA940-C%C3%93DIGO-DE-PRODUTO-NO-ARQUIVO-DO-SINTEGRA
---

**Dúvida**Quando código de produto é superior à 14 posições, sistema carrega o RECNO da tabela SB1 + Informações do NCM no arquivo do Sintegra. Como carregar o código do produto diferente desta regra no arquivo do Sintegra?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Para retornar no arquivo do Sintegra a composição do código de produto diferente da regra do RECNO + NCM, é necessário utilizar o ponto de entrada A940PRD, conforme documentação abaixo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6077000>  
  
O layout do Sintegra aceita apenas 14 posições para o código do Produto, no registro tipo 54,por exemplo, sendo necessário que retornem apenas estas posições.
