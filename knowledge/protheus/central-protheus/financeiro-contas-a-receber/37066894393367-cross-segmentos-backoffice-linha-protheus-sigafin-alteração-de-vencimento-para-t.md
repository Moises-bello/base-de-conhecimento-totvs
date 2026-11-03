---
article_id: 37066894393367
category: Financeiro - Contas a Receber
content_hash: e71272fc1fb1e15c9effe10b56145c7af1a626a0ae95c3164e9eae5fcfa2929c
fetched_at: '2026-06-28T22:38:13.911269+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Alteração de vencimento
  para títulos contabilizados
type: support-article
updated_at: '2025-12-16T18:25:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37066894393367-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Altera%C3%A7%C3%A3o-de-vencimento-para-t%C3%ADtulos-contabilizados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37066894363415) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Existe alguma rotina que possamos usar para alteração da data de vencimento, de títulos já contabilizados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução:**

Para os casos onde o sistema bloqueia a alteração da data de vencimento devido contabilizações, você pode liberar a alteração do campo usando os PE's abaixo:  

* CONTAS A PAGAR:   
  **F050MCP -**Permite incluir novos campos na opção **Alterar** da rotina **FINA050**.  
  Documentação:[DT\_F050MCP\_Adiciona\_campos\_na\_alteracao\_do\_Contas\_a\_pagar](http://tdn.totvs.com/display/PROT/DT_F050MCP_Adiciona_campos_na_alteracao_do_Contas_a_pagar)
* CONTAS A RECEBER:   
  **F040CPO** - utilizado na manipulação dos campos que terão permissão para alteração nos títulos a receber.  
  <http://tdn.totvs.com/pages/releaseview.action?pageId=6070865>
