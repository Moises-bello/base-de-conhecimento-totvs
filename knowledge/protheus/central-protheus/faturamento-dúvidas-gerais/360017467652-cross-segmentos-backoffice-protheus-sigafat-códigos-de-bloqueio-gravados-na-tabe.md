---
article_id: 360017467652
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 92831cbd11737b57c5bbc1356867310dfe27cdc30fee46aab36d1e8791d984bc
fetched_at: '2026-06-28T22:38:28.793991+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFAT - Códigos de Bloqueio gravados
  na tabela SC9 dos Pedidos de Venda Liberados
type: support-article
updated_at: '2025-03-10T19:24:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017467652-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-C%C3%B3digos-de-Bloqueio-gravados-na-tabela-SC9-dos-Pedidos-de-Venda-Liberados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30542189044759) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**

Como identifico os códigos de bloqueios gravados na tabela SC9 dos Pedidos de Venda Liberado?

**Ambiente**

Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Por meio da tabela SC9, é possível identificar os códigos de bloqueios nos seguintes campos:

**O Campo C9\_BLCRED** indica se o Item possui algum Bloqueio de Crédito, os registros possíveis para este campo são:

* **(   ) Vazio:** Indica que não há nenhum Bloqueio de Crédito registrado para este item do Pedido de Vendas;
* **(01) Bloqueio de Crédito por Valor:** Indica que o Valor do Crédito, disponível para este Cliente, não é suficiente;
* **(02) Bloqueio gerado por falta de Estoque:** Bloqueio gerado quando o parâmetro MV\_BLQCRED esta ativo (T) e não há saldo de Estoque Disponível;
* **(04) Vencimento do Limite de Crédito:** Indica que o Limite de Crédito do Cliente (A1\_VENCLC) está vencido;
* **(09) Liberação de Crédito Rejeitada:** Indica que o Pedido de Vendas estava Bloqueado por Crédito, e o usuário, nas rotinas de Liberação de Crédito, selecionou a opção de Liberação Manual e selecionou "REJEITA";
* **(10) Faturado:** Indica que o Pedido de Vendas já passou por todas as Liberações e foi Faturado;
* **(ZZ) Liberação Tardia:** Indica que Liberação Tardia de Crédito está ativa.

Com a  integração do **Totvs Mais Negócios,** o campo **C9\_BLCRED** também passou a receber os seguintes registros:

* **(80 /92)**: Análise de crédito pela plataforma Risk;
* **(90 /91)**: Bloqueio por regras - plataforma Risk.

**O Campo C9\_BLEST** indica se o Item possui algum Bloqueio de Estoque, os registros possíveis para este campo são:

* **(    ) Vazio:** Indica que não há nenhum Bloqueio de Estoque registrado para este item do Pedido de Vendas;
* **(02) Bloqueio de Estoque:** Indica que o produto não possui saldo disponível no Estoque para venda;
* **(03) Bloqueio Manual de Estoque:** Indica que o Pedido de Vendas estava Liberado, sem Bloqueio de Estoque, porém o usuário alterou o pedido e, ao liberá-lo novamente, o sistema identificou um Bloqueio de Estoque, este registro geralmente é identificado nas linhas deletadas;
* **(10) Faturado:** Indica que o Pedido de Vendas já passou por todas as Liberações e foi Faturado.
* **(ZZ) Liberação Tardia:** Indica que Liberação Tardia de Estoque está ativa.

**O Campo C9\_BLWMS** indica os bloqueios gerados pelo módulo "WMS - Gestão de Armazenagem" (SIGAWMS), caso identifique um destes Bloqueios, entre em contato com a equipe de Suporte ao módulo WMS:

* **(01)** Bloqueio de Endereçamento do WMS/Somente SB2;
* **(02)** Bloqueio de Endereçamento do WMS;
* **(03)** Bloqueio de WMS - Externo;
* **(05)** Liberação para Bloqueio 01;
* **(06)** Liberação para Bloqueio 02;
* **(07)** Liberação para Bloqueio 03.

**Saiba mais:**

**[Bloqueios gravados na Tabela SC9 (Liberação dos Pedidos de Venda)](https://tdn.totvs.com/x/Zk1tDQ)**
