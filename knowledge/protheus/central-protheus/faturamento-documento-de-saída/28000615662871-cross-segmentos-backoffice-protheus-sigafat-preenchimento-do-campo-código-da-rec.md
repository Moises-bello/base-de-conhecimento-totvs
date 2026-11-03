---
article_id: 28000615662871
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: e0b212310bdd80150f00a50defc2e6e59fee71be590cc1c65d983131017abb72
fetched_at: '2026-06-28T22:38:44.140167+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Preenchimento do campo "Código
  da Receita - IRRF (E1_CODIRRF)" ao faturar
type: support-article
updated_at: '2024-11-22T19:27:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28000615662871-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Preenchimento-do-campo-C%C3%B3digo-da-Receita-IRRF-E1-CODIRRF-ao-faturar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28000663066263) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Tem como efetuar o preenchimento do campo "Código da Receita - IRRF (E1\_CODIRRF)" ao faturar?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Passo a passo:

1 - Criar o campo ED\_CODPERD igual ao campo E1\_CODIRRF conforme documentação: [DSERFAT-3170 DT Faturamento - Gravação E1\_CODIRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=316998437)

2 - Incluir a informação (no campo ED\_CODPERD) na natureza que esta sendo utilizada para venda "Natureza (C5\_NATUREZ ou A1\_NATUREZ)" [Depende do parâmetro MV\_1DUPNAT]  
  
3 - Incluir um Pedido de Venda e faturar  
  
4 - Valide o título gerado olhando o campo "Código da Receita - IRRF (E1\_CODIRRF)"  
  
**Resultado:**

* O campo "Código da Receita - IRRF (E1\_CODIRRF)" receberá o campo "Código da Receita - IRRF (ED\_CODPERD)"
