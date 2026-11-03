---
article_id: 360027917871
category: Escrita Fiscal - Impostos - ICMS
content_hash: faef106169b19e34566bb4d71d014f5331df329b6bf92bdfbe4b69ced961b6d3
fetched_at: '2026-06-28T22:39:24.249561+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Venda para o Ceará
  está reduzindo a base de ICMS
type: support-article
updated_at: '2021-07-28T03:14:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027917871-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Venda-para-o-Cear%C3%A1-est%C3%A1-reduzindo-a-base-de-ICMS
---

**Dúvida**

*VENDA PARA CEARA ESTÁ REDUZINDO A BASE*  
**Ambiente**Protheus - Faturamento - A partir da versão 11.80

**Solução**

Sendo a Venda para Estado do CEARA, verifique se o parâmetro MV\_UFIRCE está preenchido.  
O mesmo deve estar em Branco.

Configuração do Dicionário Padrão para o Parâmetro:  
Nome da Variável = MV\_UFIRCE  
Tipo = Caracter  
Descrição = Posição 1: Qtd máxima de UFIRCEs. Posição 2: Valor unitário da UFIRCE. Referente ao Estado do Ceará.  
Default = {500,3.0407}

Após alterar o parâmetro refaça o pedido de vendas
