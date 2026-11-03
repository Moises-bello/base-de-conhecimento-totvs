---
article_id: 37066894258839
category: Financeiro - Contas a Pagar
content_hash: 5cf48ac0097db70b881ef091f7babf3071f0743b90b0ea05919979db6b3d3f8d
fetched_at: '2026-06-28T22:38:08.472802+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Alteração de vencimento
  para títulos contabilizados
type: support-article
updated_at: '2025-12-16T18:25:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37066894258839-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Altera%C3%A7%C3%A3o-de-vencimento-para-t%C3%ADtulos-contabilizados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37066935640599) Tempo aproximado para leitura: **00:05 min**  
  
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
