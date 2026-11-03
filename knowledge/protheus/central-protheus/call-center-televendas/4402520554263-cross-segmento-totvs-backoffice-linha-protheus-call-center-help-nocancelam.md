---
article_id: 4402520554263
category: Call Center - Televendas
content_hash: 95604bdfeabcf72b9562f2458ffcef688a230a30da47d540c1016ae2f86d74b9
fetched_at: '2026-06-28T22:41:30.187711+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - Help NOCANCELAM
type: support-article
updated_at: '2025-01-06T19:24:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402520554263-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Call-Center-Help-NOCANCELAM
---

**Ocorrência**Ao tentar cancelar o atendimento sistema apresenta o help **NOCANCELAM.**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center - Todas as versões  
  
**Causa**O help é apresentado quando sistema identifica que o atendimento não pode ser cancelado.  
  
**Solução**Para tratar o help analise as opções abaixo que ele valida:

1. Pode ocorrer caso o ponto de entrada **TMKMEX**/**TMKVEX** esteja configurado;

2. Ocorre caso o pedido gerado esteja liberado no faturamento, o sistema valida o campo  
**UA\_NUMSC5** e verifica se existe liberação na tabela **SC9.** Caso sim, ele também gera o help **TLVLIBSC9**. Para excluir o atendimento estorne a liberação do Pedido para cancelar o atendimento;

3. Se o pedido gerado **UA\_NUMSC5** estiver faturado, apresenta o Help. Para excluir o atendimento, exclua o pedido de vendas;

4. Se o operador não tiver acesso à excluir o pedido (permissões do   
cadastro de operador) **UA\_OPER**, realize a liberação conforme o passo a passo abaixo:

        4.1 Altere o cadastro do operador > Outras ações > Toolbar > Marque a opção **Cancele o Atendimento**;

![image__3_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402507655831/image__3_.png)

5. Se o campo **UA\_STATUS** estiver igual a "CAN" significa que já esta cancelado.
