---
article_id: 26081793860247
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: efd8a10326909cba318b5059c18a58613398949f260d01350ba2c841312bb11e
fetched_at: '2026-06-28T22:39:20.334035+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como o sistema busca
  a origem do Produto?
type: support-article
updated_at: '2024-09-02T21:02:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26081793860247-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-o-sistema-busca-a-origem-do-Produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26081793855127) Tempo aproximado para leitura: 03:00**min** **Dúvida**Como o sistema busca a origem do Produto?

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

A origem do Produto é tratada na sequencia abaixo:  
 

1. Através do campo CFD\_ORIGEM, caso o produto possua um código de FCI - Ficha de Conteúdo de Importação;
2. Através do campo D1\_CLASFIS, caso encontre um Documento de Entrada referente ao Lote/SubLote; e Parâmetro MV\_FISFRAS = .T. determina a origem de acordo com a informada no campo D1\_CLASFIS.
3. Através dos campos B1\_ORIGEM ou BZ\_ORIGEM dos Cadastros de Produtos e de Indicadores.

A origem influência no calculo do ICMS nas vendas fora do estado.

O sistema tributa a alíquota do ICMS de acordo com origem do Produto.

Produtos Nacionais  
B1\_origem = 0/4/5/6 e 7 de acordo com a configuração do parâmetro MV\_NORTE

   
Produtos Importados  
B1\_origem = 1/2/3 e 8 alíquota de 4%

<https://tdn.totvs.com/pages/releaseview.action?pageId=672568241>

<https://tdn.totvs.com/pages/releaseview.action?pageId=498719605>
