---
article_id: 360019523532
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1a17dcf590dd5bbe6526fa2f6654353cf6b821cdda5e4db2fb2d0909e5836921
fetched_at: '2026-06-28T22:38:41.271471+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP-FAT -Como ocorre a gravação dos campos C5_USERLGI e C5_USERLGA na inclusão
  do Pedido de Venda
type: support-article
updated_at: '2021-04-28T15:51:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019523532-MP-FAT-Como-ocorre-a-grava%C3%A7%C3%A3o-dos-campos-C5-USERLGI-e-C5-USERLGA-na-inclus%C3%A3o-do-Pedido-de-Venda
---

**Dúvida**Ao incluir um Pedido de Venda o sistema preenche automaticamente os campos **C5\_USERLGI** e **C5\_USERLGA**.  
   
 **Ambiente**

Microsiga Protheus - todas as versões.  
  
**Solução**

Quando um Pedido de Venda é incluído, a rotina analisa a sua liberação e integrações com os módulos de Planejamento e Controle Orçamentário (**SIGAPCO**), Easy Export Control (**SIGAEEC**) e Controladoria (**SIGACTB**). Essas validações/integrações, mesmo ocorrendo de forma automática, atualizam o pedido e, por consequência, o campo **C5\_USERLGA**.

Isso porquê a lógica de atualização dos campos **XX\_USERLGA** ocorre quando o sistema muda alguma informação no registro da tabela, mesmo que essa alteração seja realizada através de outra rotina ou processo automático.
