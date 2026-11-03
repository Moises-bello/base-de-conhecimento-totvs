---
article_id: 33238793301143
category: Rental by ItUp Business
content_hash: 96e42adcabdd09681a2fdefda48e48b385ac73b9da1bdf387308636d900327f9
fetched_at: '2026-06-28T22:36:20.644085+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - HELP LOCM013-001 ao excluir
  item no pedido de venda
type: support-article
updated_at: '2025-07-03T20:36:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33238793301143-Cross-Segmentos-Backoffice-Protheus-SIGALOC-HELP-LOCM013-001-ao-excluir-item-no-pedido-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33238793277463) Tempo aproximado para leitura: **00:05:00 min**

**Ocorrência:**  
Ao excluir um item no pedido de venda gerado pela rotina **LOCA021 (Faturamento Automático)**, o sistema apresenta o erro "***HELP LOCM013-001**. **Problema:** O pedido foi gerado pelo módulo **SIGALOC** e não permite a exclusão de itens. **Solução:** Desmarque as linhas selecionadas para deleção antes de continuar."*

**Ambiente:**  
Cross Segmentos - Backoffice Protheus - SIGALOC - A partir da release P12.1.2310  
  
**Causa:**  
O HELP é apresentado porque o campo **C5\_XTIPFAT** está preenchido.

**Solução:**  
**1-** É necessário verificar se o preenchimento está ocorrendo devido à configuração de inicializador padrão e, se for o caso, removê-la. Assim, ao gerar o pedido de venda pela rotina **LOCA021 (Faturamento Automático)**, o pedido será criado com o campo em branco.
