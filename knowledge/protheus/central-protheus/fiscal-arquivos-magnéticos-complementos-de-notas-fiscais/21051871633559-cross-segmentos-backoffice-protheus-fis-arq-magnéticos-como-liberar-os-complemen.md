---
article_id: 21051871633559
category: 'Fiscal Arquivos Magnéticos - Complementos de Notas Fiscais '
content_hash: 43c830dd8a46eb09e82247ee2d9207b5c0496fdb9da8b80fa5aa5fcf8a43506e
fetched_at: '2026-06-28T22:41:59.448473+00:00'
product: protheus
section_id: 7707613209239
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como liberar
  os complementos de Importação na NF manual de Entrada?
type: support-article
updated_at: '2024-02-01T20:21:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21051871633559-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-liberar-os-complementos-de-Importa%C3%A7%C3%A3o-na-NF-manual-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21051876097815) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como liberar os complementos de Importação na NF manual de Entrada?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Para que os complementos de Importação seja liberado, o Fornecedor **(SA2)** deve estar com a seguinte configuração:  
  
Estado **A2\_EST** = EX  
Tipo **A2\_TIPO** = X - Outros  
Município **A2\_CODMIN** = 99999 (estrangeiro)

![](https://totvssuporte.zendesk.com/attachments/token/kzYKV6BLB9OsuH5lbInnKkyT7/?name=inline-1384246873.png)

Logo após a liberação , é preciso preencher todas as informações das linhas do complemento de importação conforme print abaixo:

***Livros Fiscais>>Rotina MATA910 - NF Entrada Manual>>Selecionar nota Fiscal>>Ações Relacionadas>>Complementos>>Importação***

![](https://totvssuporte.zendesk.com/attachments/token/BvUo9vZUDynvLE1vLoA0vxLHj/?name=inline1716787813.png)
