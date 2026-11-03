---
article_id: 360044388894
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1cb3962a388cf20a37496a789e07c448d67d51ec23b811cf134f06c5b306f8d1
fetched_at: '2026-06-28T22:38:39.717080+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como habilitar o botão "Lote
  e endereços" na opção "Nova Liberação" da rotina de Liberação de Estoque
type: support-article
updated_at: '2026-05-07T14:50:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044388894-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-habilitar-o-bot%C3%A3o-Lote-e-endere%C3%A7os-na-op%C3%A7%C3%A3o-Nova-Libera%C3%A7%C3%A3o-da-rotina-de-Libera%C3%A7%C3%A3o-de-Estoque
---

**Dúvida**  
Como habilitar o botão "**Lote e endereços**" na opção "Nova Liberação" da rotina de Liberação de Estoque (**MATA455**)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**  
Ao utilizar, na rotina de **Pedidos de Venda** (**MATA410**), um produto que controla **Lote** (**B1\_RASTRO**) e **Endereço** (**B1\_LOCALIZ**), quando não há saldo no lote ou endereço informados, ao liberar o pedido, o sistema irá gerar um **bloqueio de Estoque**.

Para que não seja necessário alterar o pedido de vendas, é possível **selecionar** outro **Lote e Endereço** para faturamento, para isso basta acessar a rotina **Liberação de Estoque (MATA455)** e acessar “**Outras Ações**” -> "**Nova Liberação**", o sistema apresentará uma tela com a opção "**Lote e endereços**":

![01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360060483354)

Para que o botão fique **habilitado** é necessário configurar o **parâmetro** **MV\_SELLOTE** com conteúdo **1**, o parâmetro **MV\_SELPLOT** irá determinar se nesta opção será possível selecionar outro Lote ou apenas outros **endereços do lote informado**.

Observação: Esta opção ficará disponível **apenas** para itens que possuam **controle de Lote e Endereçamento**.

O parâmetro **MV\_SELTNEW** permite a seleção de **diferentes lotes** na liberação manual de estoque e na opção "**Nova Liberação**" da rotina de Liberação de Estoque **(MATA455)**.

**Saiba mais**: [**https://tdn.totvs.com/x/TqxZE**](https://tdn.totvs.com/x/TqxZE)
