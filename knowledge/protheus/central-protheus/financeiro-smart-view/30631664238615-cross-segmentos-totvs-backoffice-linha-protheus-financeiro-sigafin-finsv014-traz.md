---
article_id: 30631664238615
category: Financeiro - Smart View
content_hash: 96533596933669a6668f4c4fba7502ca3d0d0f9f322fb43f34c55f7aae028456
fetched_at: '2026-06-28T22:37:44.866643+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) Financeiro - SIGAFIN -
  FINSV014 - Trazendo movimentações excluídas como canceladas
type: support-article
updated_at: '2026-01-07T18:51:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30631664238615-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-SIGAFIN-FINSV014-Trazendo-movimenta%C3%A7%C3%B5es-exclu%C3%ADdas-como-canceladas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30631664216087) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Porque o relatório FINSV014 - Smart View - Relatório de Extrato bancário está trazendo movimentações excluídas na visualização dos dados de movimentação, diferente do relatório FINR470 que não demonstra essas movimentações?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2310

**Solução**

Diferentemente do relatório extrato bancário do legado (FINR470) que era baseado na tabela SE5, o Smart View é baseado na tabela FK5. Conforme as regras de negócio e modelagem das tabelas FK's disponível neste link

[Reestruturação Financeiro - Baixas e Movimento Bancário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=181965434)

A tabela FK5 não possui exclusão de movimento, apenas estorno.   
  
Por esse motivo, os movimentos bancários, mesmo excluídos, serão apresentados.

É possível personalizar os filtros dos objetos de negócio do Smart View conforme as necessidades da empresa. Para orientá-lo nesse processo, disponibilizamos a seguinte documentação:

[Exportação/Importação de recursos](https://tdn.totvs.com/pages/releaseview.action?pageId=861277826)

Se ainda houver dúvidas sobre a personalização do objeto de negócios, é possível abrir um chamado junto ao time de framework para apoiá-lo.  
  
**Saiba mais**  
[Smart View - Relatório de Extrato bancário](https://tdn.totvs.com/pages/releaseview.action?pageId=759953066)
