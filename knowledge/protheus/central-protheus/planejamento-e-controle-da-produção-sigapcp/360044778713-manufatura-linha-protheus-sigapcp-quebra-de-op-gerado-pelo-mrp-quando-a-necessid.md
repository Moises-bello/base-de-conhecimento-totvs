---
article_id: 360044778713
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 55ea4fe4b2b48e8c21efe9ed575b24006ccd107119253298ac3f44af33f2c76c
fetched_at: '2026-06-28T22:42:45.824627+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quebra de OP gerado pelo MRP quando
  a necessidade é por PMP
type: support-article
updated_at: '2021-06-01T17:24:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044778713-Manufatura-Linha-Protheus-SIGAPCP-Quebra-de-OP-gerado-pelo-MRP-quando-a-necessidade-%C3%A9-por-PMP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Por que ao executar o **MATA712 -** **MRP**baseado em um **PMP - Plano Mestre de Produção** as quantidades das **OPs - Ordens de Produções** geradas não são quebradas pelo **lote mínimo** e **econômico**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Como o **PMP** é proveniente da produção, as quantidades informadas não são quebradas, pois pressupõe-se que já estão corretas conforme a capacidade e melhores condições de produção.  
  
**Importante**  
A quantidade dos documentos gerados será quebrada por **lote econômico** ou **mínimo** quando a necessidade do **MRP - Material Requirement Planning** é proveniente de **previsões de vendas**, **pedidos em carteira** ou **estoque**.
