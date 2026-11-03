---
article_id: 360046826433
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: bff18fca9a435d7b681e7e25798a9cd30dac266cb87700543d7410290d743628
fetched_at: '2026-06-28T22:38:40.988904+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Tamanho dos campos de Número
  do Pedido de Vendas (C5_NUM, C6_NUM)
type: support-article
updated_at: '2025-04-22T11:12:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046826433-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Tamanho-dos-campos-de-N%C3%BAmero-do-Pedido-de-Vendas-C5-NUM-C6-NUM
---

### time.png Tempo aproximado para leitura: **00:01:40 min**

**Dúvida**

Campos de Número do Pedido de Vendas C5\_NUM e C6\_NUM podem sofrer alterações de tamanho?

**Ambiente**Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Os campos **C5\_NUM** e **C6\_NUM**, que representam o número do Pedido de Venda e seus respectivos itens, possuem tamanho fixo de 6 caracteres e não podem ser alterados.

Esses campos são alfanuméricos e fazem parte do controle de numeração do sistema, o que significa que não fazem parte de um grupo de campos e a alteração de tamanho é bloqueada no dicionário de dados, porém possibilitam gerar uma combinação superior a **2 bilhões** de códigos únicos.

**Exemplo:**

Os campos C5\_NUM e C6\_NUM utilizam **26 letras (A - Z)** e **10 números (0 - 9**), o que totaliza 36 possibilidades por caractere.  
Sendo assim, o número total de combinações possíveis em um campo de 6 posições é:

**36⁶ = 2.176.782.336 combinações**

**Observação:** Esse comportamento se aplica também a outros campos de controle de numeração com as mesmas características, como exemplo:

A1\_COD – Código do Cliente

A3\_COD – Código do Vendedor

C7\_NUM – Número do Pedido de Compra

B1\_COD – Código do Produto

**Saiba mais**: [Limite de campos chave e possíveis combinações](https://tdn.totvs.com/x/W7LSHg)
